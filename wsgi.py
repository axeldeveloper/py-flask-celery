#
# Conteudo do arquivo `wsgi.py`
#
import os
import sys
# sys.path.insert(0, "/home/seu-usuario/projetos/flask-test")
# sys.path.insert(0, "E:/Desenvolvimento\python/py_flask_celery/")
sys.path.append(os.path.dirname(__file__))

from app import app
from app import app as application
if __name__ == "__main__":
    if os.environ.get('FLASK_ENV') == "development":
        #print("Desenvolvimento")
        #app.run(host="0.0.0.0", port=5002, debug=False)
        app.run(debug=False)
    else:
        #print("prod")
        #from app import app as application
        application.run(host="0.0.0.0", debug=False)