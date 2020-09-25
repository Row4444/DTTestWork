FROM python:3.6-alpine
# set work directory
WORKDIR /usr/src/DevelopsToday/
# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# install dependencies
RUN apk add bind-tools
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev
RUN pip install --upgrade pip
RUN pip install psycopg2-binary
COPY ./requirements.txt .
RUN pip install -r requirements.txt
# copy project
COPY . .