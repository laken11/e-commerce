FROM python:3.9.1-buster
WORKDIR  /app
RUN apt-get update && apt-get -y install libssl-dev
RUN apt-get install -y python3-dev libmariadb-dev-compat libmariadb-dev
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN pip install dependency-injector
RUN pip install Pillow
COPY . .
EXPOSE 8087
CMD [ "python3", "manage.py", "runserver" ]
