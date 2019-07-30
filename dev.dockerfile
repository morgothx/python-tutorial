# Image based on the official Python 3 image from dockerhub
FROM python:3.7.3

# Change directory so that commands run inside this new directory
WORKDIR /usr/src/app

# Python install
COPY requirements.txt ./
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN python -m spacy download es_core_news_sm

RUN python manage.py makemigrations
RUN python manage.py migrate


# Expose port to server
EXPOSE 8000
