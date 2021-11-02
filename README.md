# 630_django_example

The commands necessary to run this are:

```
pip install django
python3 manage.py makemigrations 
python3 manage.py migrate
python3 manage.py createsuperuser
python3 manage.py runserver
```
However, for practice/learning, it would be best to work through the project creation steps:

```
django-admin startproject edu
cd edu
python3 manage.py startapp registration
# copy or modify the registration/models.py
# add registration to INSTALLED_APPS in edu/settings.py
# register models in registration/admin.py
python3 manage.py makemigrations 
python3 manage.py migrate
python3 manage.py createsuperuser
python3 manage.py runserver
```
