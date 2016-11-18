# coffee

## Deploy

```shell
# Install virtualenv
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple virtualenv
virtualenv env

source env/bin/activate
# install gunicron
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple gunicorn

pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt

# run
gunicorn --workers=8 --bind=127.0.0.1:9080 --worker-class=gevent --name=coffee wsgi:application

```

## validate

api : http://127.0.0.1:9080/coffee/api/spec.html