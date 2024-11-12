FROM python:3
ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY . /app
RUN pip install django
RUN python -m pip install Pillow