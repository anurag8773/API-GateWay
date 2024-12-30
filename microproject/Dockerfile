FROM python:3.13.1
ENV PYTHONUNBUFFERED 1
WORKDIR /microapp
COPY requirements.txt /microapp/requirements.txt
RUN pip install -r requirements.txt
COPY . /microapp
