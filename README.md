# label_studio

frok from https://github.com/HumanSignal/label-studio

label_studio

# install

python 3.10

```
conda activate p310
pip install -r requirement.txt -i https://mirrors.aliyun.com/pypi/simple/

```

## run

```
python label_studio/manage.py migrate
python label_studio/manage.py collectstatic
# Start the server in development mode at http://localhost:8080
python label_studio/manage.py runserver

```
