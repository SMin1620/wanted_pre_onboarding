FROM python:3.9.0

COPY ./ /app

WORKDIR /app

RUN apt-get update
RUN pip install -r requirements.txt

CMD ["bash", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]