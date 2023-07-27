FROM python:3.9.0

WORKDIR /home/

RUN git clone https://github.com/k2h2j3/django_pinterest.git

WORKDIR /home/django_pinterest/

RUN pip install -r requirements.txt

RUN echo "SECRET_KEY=django-insecure-0afu)rkii1_sog_4p2p2-)df$&a5f571^h1ux1bt2kbe5v^+!0" > .env

RUN python manage.py migrate

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]