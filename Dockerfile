FROM python:3.11-slim

WORKDIR /usr/src/app 

ENV PYTHONUNBUFFERED 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

ENTRYPOINT [ "sh", "entrypoint.sh" ]