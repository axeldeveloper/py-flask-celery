# Using lightweight alpine image
FROM python:3.11-alpine

# Installing packages
RUN apk update
RUN pip install --no-cache-dir pipenv

# Defining working directory and adding source code
WORKDIR /usr/src/app
COPY Pipfile Pipfile.lock bootstrap.sh ./
COPY cashman ./cashman

# Install API dependencies
RUN pipenv install --system --deploy

# Start app
EXPOSE 5000
ENTRYPOINT ["/usr/src/app/bootstrap.sh"]

# build RUN the image
#docker build -t cashman .

# run a new docker container named cashman
#docker run --name cashman -d -p 5000:5000 cashman


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