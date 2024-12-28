# syntax=docker/dockerfile:1
ARG NODE_VERSION=18
ARG PYTHON_VERSION=3.12

##-------------------------------------------------------build web-------------------
FROM --platform=${BUILDPLATFORM} node:${NODE_VERSION} AS frontend-builder
ENV BUILD_NO_SERVER=true \
    BUILD_NO_HASH=true \
    BUILD_NO_CHUNKS=true \
    BUILD_MODULE=true \
    YARN_CACHE_FOLDER=/root/.yarn \
    NX_CACHE_DIRECTORY=/root/.nx \
    NODE_ENV=production

WORKDIR /label-studio/web
RUN yarn config set registry https://registry.npmmirror.com/
RUN yarn config set cache-folder ${YARN_CACHE_FOLDER} 
RUN yarn config set network-timeout 1200000 # HTTP timeout used when downloading packages, set to 20 minutes

COPY web/package.json .
COPY web/yarn.lock .
COPY web/tools tools
#Yarn 包缓存 (${YARN_CACHE_FOLDER})
#Nx 构建缓存 (${NX_CACHE_DIRECTORY})
#sharing=locked 确保缓存在并发构建时的安全访问
RUN --mount=type=cache,target=${YARN_CACHE_FOLDER},sharing=locked \
    --mount=type=cache,target=${NX_CACHE_DIRECTORY},sharing=locked \
    yarn install --prefer-offline --no-progress --pure-lockfile --frozen-lockfile --ignore-engines --non-interactive --production=false

COPY web .
COPY pyproject.toml ../pyproject.toml
RUN --mount=type=cache,target=${YARN_CACHE_FOLDER},sharing=locked \
    --mount=type=cache,target=${NX_CACHE_DIRECTORY},sharing=locked \
    yarn run build
##-------------------------------------------------------install python lib-------------------
RUN echo "web build ok,build python"
FROM python:${PYTHON_VERSION}-slim AS venv-builder
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    PIP_CACHE_DIR="/root/.cache/pip" 
ENV VENV_PATH="/label-studio/.venv"
ENV PATH="$VENV_PATH/bin:$PATH"


RUN --mount=type=cache,target="/var/cache/apt",sharing=locked \
    --mount=type=cache,target="/var/lib/apt/lists",sharing=locked \
    set -eux; \
    apt-get update; \
    #--no-install-recommends: 只安装必需依赖，不安装推荐的包
    apt-get install --no-install-recommends -y \
    #安装构建工具和 Git build-essential: 包含基本的编译工具（gcc, make 等）
            build-essential git; \
    #删除不再需要的依赖包
    apt-get autoremove -y
    
WORKDIR /label-studio
COPY requirements.txt .
COPY label_studio label_studio
COPY label_studio_sdk label_studio_sdk

RUN --mount=type=cache,target=$PIP_CACHE_DIR,sharing=locked \
    python3 -m venv --copies $VENV_PATH &&\
    pip install --cache-dir $PIP_CACHE_DIR -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/ &&\
    python3 label_studio/manage.py collectstatic --no-input



##-------------------------------------------------------build production-------------------
FROM python:${PYTHON_VERSION}-slim AS production

ENV LS_DIR=/label-studio \
    HOME=/label-studio \
    LABEL_STUDIO_BASE_DATA_DIR=/label-studio/data \
    DJANGO_SETTINGS_MODULE=core.settings.label_studio \
    PATH="/label-studio/.venv/bin:$PATH" \
    #禁用 Python 的输出缓冲
    PYTHONUNBUFFERED=1 \
    #阻止 Python 生成 .pyc 文件（字节码缓存）
    PYTHONDONTWRITEBYTECODE=1 
  
WORKDIR $LS_DIR

# install nginx
RUN --mount=type=cache,target="/var/cache/apt",sharing=locked \
    --mount=type=cache,target="/var/lib/apt/lists",sharing=locked \
    set -eux; \
    apt-get update; \
    apt-get install --no-install-recommends -y nginx; \
     # 验证 Nginx 安装
    nginx -v; \
    # 清理不需要的依赖
    apt-get autoremove -y


RUN set -eux; \
    mkdir -p $LS_DIR $LABEL_STUDIO_BASE_DATA_DIR && \
    chown -R 1001:0 $LS_DIR $LABEL_STUDIO_BASE_DATA_DIR /var/log/nginx /etc/nginx


COPY --chown=1001:0 deploy/default.conf /etc/nginx/nginx.conf

# Copy essential files for installing Label Studio and its dependencies
COPY --chown=1001:0 README.md .
COPY --chown=1001:0 deploy deploy

# Copy files from build stages
COPY --chown=1001:0 --from=venv-builder               $LS_DIR                                           $LS_DIR
COPY --chown=1001:0 --from=frontend-builder           $LS_DIR/web/dist                                  $LS_DIR/web/dist

USER 1001

EXPOSE 8080

ENTRYPOINT ["./deploy/docker-entrypoint.sh"]
CMD ["label-studio"]