# Project
    - python 3.11.4
    - celery
    - alwaysdata
    - flask

# Install dependencies
    - python3 pip install -r .\requirements.txt


# Create virtual env
```sh
$ python3 -m venv .venv311
# window 
$ ./venv311/Scripts/activate/Activate.ps1
$ ./venv311/Scripts/activate

# linux 
source ./venv311/bin/activate
source venv311/bin/activate

$ pip install -r requirements.txt

$ cd my-project

$ virtualenv --python C:\Path\To\Python\python.exe venv
$ virtualenv -p  C:\Python311\ venv311
$ virtualenv --python C:\Python311\python.exe venv311
$ .\venv311\Scripts\activate

$ .\venv311\Scripts\activate
$ & e:/Desenvolvimento/python/Em_py3/rq-test/venv39/Scripts/Activate.ps1


```
# run 
- uvicorn main:app --port 8100 --host '::' --proxy-headers --forwarded-allow-ips "::1"
- gunicorn --bind 0.0.0.0:5002 wsgi:app

# Start worker instance.

$ celery --app=proj worker -l INFO

$ celery -A proj worker -l INFO -Q hipri,lopri

$ celery -A proj worker --concurrency=4

$ celery -A proj worker --concurrency=1000 -P eventlet

$ celery worker --autoscale=10,0


# Running the Celery worker server

```powershell
# run worker
$ celery -A tasks worker --loglevel=INFO
$ celery -A tasks worker -l INFO -E
$ celery -A tasks worker -l debug

celery -A tasks worker --without-heartbeat --without-gossip --without-mingle

celery worker -A tasks -Q default --concurrency=4

celery -A tasks worker -l INFO -Q queue1

# run monitor flower
$ celery -A tasks flower --port=5001

$ celery -A tasks flower --basic-auth="user1:foo,user2:bar" --port=5001

```

- https://www.revsys.com/tidbits/celery-and-django-and-docker-oh-my/