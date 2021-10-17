# start from an official image
FROM python:3.8-slim

ARG APP

RUN mkdir -p $APP
WORKDIR $APP

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY . $APP
RUN pip3 install -r requirements.txt && \
    python3 manage.py collectstatic --noinput && \
    python3 manage.py makemigrations && \
    python3 manage.py makemigrations config bank attendance && \
    python3 manage.py migrate

EXPOSE 80
CMD ["gunicorn", "--bind", ":80", "yg_system.wsgi:application"]