# Project
    - python 3.11.4
    - celery
    - alwaysdata
    - flask
    - migration
    - postgres

# Install dependencies
    - python3 pip install -r .\requirements.txt


# Create virtual env
```sh
$ cd my-project

$ python3 -m venv .venv311
# window 
$ ./venv311/Scripts/activate/Activate.ps1
$ ./venv311/Scripts/activate
$ & e:/Desenvolvimento/python/Em_py3/rq-test/venv39/Scripts/Activate.ps1

# linux 
source ./venv311/bin/activate
source venv311/bin/activate


$ virtualenv --python C:\Path\To\Python\python.exe venv
$ virtualenv -p  C:\Python311\ venv311
$ virtualenv --python C:\Python311\python.exe venv311
$ .\venv311\Scripts\activate

$ .\venv311\Scripts\activate

# install packages
$ pip install -r requirements.txt

# migration
flask db init
flask db migrate -m "Initial migration."
flask db upgrade

# postgres
pip install psycopg2-binary
```

# WSGI file

```py
#
# Conteudo do arquivo `wsgi.py`
#
import os
import sys

# sys.path.insert(0, "/home/seu-usuario/projetos/flask-test")
# sys.path.insert(0, "E:/Desenvolvimento\python/py_flask_celery/")
# sys.path.append(os.path.dirname(__file__))
from app import app as application
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002, debug=False)
    application.run(host="0.0.0.0", debug=False)
```

```sh
# run
flask run --debug

- uvicorn main:app --port 8100 --host '::' --proxy-headers --forwarded-allow-ips "::1"
- gunicorn --bind 0.0.0.0:5002 wsgi:app

# Start worker instance.
celery worker -A celery_worker.celery --loglevel=INFO -Q cache
$ celery --app=proj worker -l INFO

$ celery -A proj worker -l INFO -Q hipri,lopri

$ celery -A proj worker --concurrency=4

$ celery -A proj worker --concurrency=1000 -P eventlet

$ celery worker --autoscale=10,0


# Running the Celery worker server

```powershell
# run worker
$ celery --app worker.tasks.celery_app worker --loglevel=info
$ celery -A worker.tasks.celery_app worker --loglevel=INFO
$ celery -A worker.tasks.celery_app worker -l INFO -E
$ celery -A worker.tasks.celery_app worker --without-heartbeat --without-gossip --without-mingle
# tasks = app clery name
$ celery -A tasks worker -l debug

celery --app worker.tasks.celery_app worker -Q default --concurrency=4

celery -A tasks worker -l INFO -Q queue1

# run monitor flower
$ celery -A worker.tasks.celery_app flower --port=5555
$ celery --app worker.tasks.celery_app flower --port=5555 -Q default --concurrency=4
$ celery --app worker.tasks.celery_app flower --port=5555 -Q default
$ celery -A tasks flower --basic-auth="user1:foo,user2:bar" --port=5001

```

- https://www.revsys.com/tidbits/celery-and-django-and-docker-oh-my/

https://marshmallow-sqlalchemy.readthedocs.io/en/latest/