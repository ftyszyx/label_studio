SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

# if bash ${SCRIPT_DIR}/../deploy/prebuild.sh; then
# fi
docker build -t heartexlabs/label-studio-zyx ${SCRIPT_DIR}/..