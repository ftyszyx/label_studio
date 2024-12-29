# label_studio

frok from https://github.com/HumanSignal/label-studio

label_studio

# install

python 3.10

```
conda activate p310
pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/

```

## run

```
python label_studio/manage.py migrate
python label_studio/manage.py collectstatic
# Start the server in development mode at http://localhost:8080
python label_studio/manage.py runserver

```

##

```
docker run -it -p 8080:8080  heartexlabs/label-studio:latest label-studio --log-level DEBUG
```

## 未处理问题

docker 运行后：
File "<frozen os>", line 225, in makedirs
label_studio-app-1 | PermissionError: [Errno 13] Permission denied: '/label-studio/data/media'
