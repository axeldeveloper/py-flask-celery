# Project
    - python 3.11.4
    - celery
    - alwaysdata `host free`
    - flask
    - migration
    - postgres

# Install dependencies
    - python3 pip install -r .\requirements.txt

# Celery

<b>Celery workers: </b> são processos de trabalho que executam tarefas
    independentemente umas das outras e fora do contexto do seu serviço
    principal.

<b>Celery beat: </b> é um agendador que orquestra quando executar tarefas.
    Você também pode usá-lo para agendar tarefas periódicas.





# Create virtual env
```sh
$ cd my-project

$ python -m venv venv311
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
or
$ python -m pip install -r requirements.txt

# bootstrap
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
$ flask run --debug
$ uvicorn main:app --port 8100 --host '::' --proxy-headers --forwarded-allow-ips "::1"
$ gunicorn --bind 0.0.0.0:5002 wsgi:app

```

# Running the Celery worker server

```sh

# Worker
# Start worker instance.

$ celery --app app.celery_ap worker -l INFO
$ celery --app app.celery_ap worker --concurrency=4
$ celery --app app.celery_ap worker --concurrency=1000 -P eventlet
$ celery --app worker.tasks.celery_app worker -l INFO -E
$ celery --app worker.tasks.celery_app worker --without-heartbeat --without-gossip --without-mingle

# Queue
$ celery --app worker.tasks.celery_app worker -Q default --concurrency=4
$ celery --app app.celery_app worker --loglevel=INFO -Q cache
$ celery --app app.celery_ap worker -l INFO -Q hipri,lopri

# run monitor flower
$ celery --app app.celery_ap flower --port=5555  -l INFO -E
$ celery --app worker.tasks.celery_app flower --port=5555
$ celery --app worker.tasks.celery_app flower --port=5555 -Q default --concurrency=4
$ celery --app worker.tasks.celery_app flower --port=5555 -Q default
$ celery -A tasks flower --basic-auth="user1:foo,user2:bar" --port=5001




$ celery -A app.celery_app beat --loglevel=INFO
# run celery beat for periodic tasks
$ celery -A src.worker:celery beat --loglevel=INFO

$ celery -A worker.tasks.celery_app beat --loglevel=INFO

```
- https://www.youtube.com/watch?v=ig9hbt-yKkM

- https://demo.bootstrapdash.com/hiro-agency-landing-page/index.html#services

- https://www.revsys.com/tidbits/celery-and-django-and-docker-oh-my/

- https://marshmallow-sqlalchemy.readthedocs.io/en/latest/