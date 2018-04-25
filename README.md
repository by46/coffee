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
api : http://127.0.0.1:9080/coffee/portal/
api: http://localhost:8080/coffee/api/v1/api/spec.html#!/spec

sudo supervisorctl status
sudo supervisorctl signal HUP hello

EAAFzZBBlBpoYBAOBDVmhVbRELztCcaXvdD4abyLLkvG6KKn3eRmnyZAq6pGpLAmo5JKzo92A9LKZCPQlfeuYIyrrEIzGlxsna1ZAS182ku77iiPiN0UQddZAkYi5hMujHhM5KtZA8z0vUUYxpuyqMp3px147rd6uuL4cloZBgz4HcWZAovHIIYFYEwpa70euaY1BdZCPqp7ddvWhMfu0Y4cZCgpEd8ySxszSQZD

https://graph.facebook.com/oauth/access_token?client_id=408984389527174&client_secret=b3bd6ecc54013006ad8cab038c22e2f5&grant_type=client_credentials

https://graph.facebook.com/debug_token?input_token=EAAFzZBBlBpoYBAOBDVmhVbRELztCcaXvdD4abyLLkvG6KKn3eRmnyZAq6pGpLAmo5JKzo92A9LKZCPQlfeuYIyrrEIzGlxsna1ZAS182ku77iiPiN0UQddZAkYi5hMujHhM5KtZA8z0vUUYxpuyqMp3px147rd6uuL4cloZBgz4HcWZAovHIIYFYEwpa70euaY1BdZCPqp7ddvWhMfu0Y4cZCgpEd8ySxszSQZD&access_token=408984389527174|FercuuAloXRIRxAZQ6BVOHGkr3M