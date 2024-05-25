#
# Conteudo do arquivo `wsgi.py`
#
import os
import sys

sys.path.append(os.path.dirname(__file__))

from app import app as application
if __name__ == "__main__":
    if os.environ.get('FLASK_ENV') == "development":
        from app import app
        #print("Desenvolvimento")
        #app.run(host="0.0.0.0", port=5002, debug=False)
        app.run(debug=False)
    else:
        #print("prod")
        #from app import app as application
        application.run(host="0.0.0.0", debug=False)