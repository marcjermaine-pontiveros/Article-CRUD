FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONBUFFERED=1
WORKDIR /usr/src/bulletin/
COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY . ./
