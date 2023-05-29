# start linux with python
FROM python:3.10.11-slim-buster

# setup linux 
ENV PYTHONUNBUFFERED=1

# install needed libraries 
RUN apt-get update && apt-get -y install libpq-dev gcc

# create fodler for project 
WORKDIR /app

# copy requiremts.txt file
COPY requirements.txt /app/requirements.txt

# install libraries
RUN pip install -r /app/requirements.txt

# copy all folder 
COPY . /app/