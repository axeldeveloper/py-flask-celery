# Using lightweight alpine image
FROM python:3.11-alpine

# Installing packages
RUN apk update
#RUN pip install --no-cache-dir pipenv

# Defining working directory and adding source code
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

#COPY start.sh bootstrap.sh ./
#COPY start.sh ./


# Install API dependencies
# RUN pipenv install --system --deploy
COPY requirements.txt .
COPY start.sh .
RUN pip install -r requirements.txt


# Start app
#EXPOSE 5000
#ENTRYPOINT ["/usr/src/app/bootstrap.sh"]


# Copiar o código da aplicação
COPY . .

# Comando padrão para iniciar o Gunicorn
# CMD ["gunicorn", "-b", "0.0.0.0:8000", "app.main:app"]
# CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]
# CMD ["flask", "run", "--host", "0.0.0.0"]
ENTRYPOINT ["/usr/src/app/start.sh"]




#
#FROM python:3.6-slim-buster
#
#WORKDIR /app
#
#COPY requirements.txt ./
#
#RUN pip install -r requirements.txt
#
#COPY . .
#
#EXPOSE 4000
#
#CMD [ "flask", "run", "--host=0.0.0.0", "--port=4000"]