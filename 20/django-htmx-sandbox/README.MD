## Install Django

```
pip install django
```

## Create project

```
django-admin startproject base .
```

## Create application

```
python manage.py startapp uiapp 
```

## Run Django migrations (build Django ORM)

```
python manage.py makemigrations
```

```
python manage.py migrate
```

## Create Django superuser

```
python manage.py createsuperuser
```

Add new employee entries through Django Admin console

## Run application

```
python manage.py runserver
```