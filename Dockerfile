FROM python:2-onbuild
ENV PYTHONUNBUFFERED 1

EXPOSE 8080

RUN mkdir -p /usr/src/app 
COPY . /usr/src/app
WORKDIR /usr/src/app


RUN apt-get update

RUN pip install -r requirements.txt

CMD python manage.py runserver 0.0.0.0:8080


