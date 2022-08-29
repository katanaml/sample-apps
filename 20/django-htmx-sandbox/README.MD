## 1. Install Django

```
pip install django
```

Install dependencies:

```
pip install django-widget-tweaks
```

```
pip install django-browser-reload
```

#### Steps 2 - 5 are not required. These steps are needed if you would create app from scratch. Run application in Step 6

## 2. Create project

```
django-admin startproject base .
```

## 3. Create application

```
python manage.py startapp uiapp 
```

## 4. Run Django migrations (build Django ORM)

```
python manage.py makemigrations
```

```
python manage.py migrate
```

## 5. Create Django superuser (not required, DB file is provided)

```
python manage.py createsuperuser
```

Add new employee entries through Django Admin console

## 6. Run application

```
python manage.py runserver
```

## 7. Dump/load data (not required)

```
python manage.py dumpdata uiapp  > db.json --indent 4
```

```
python manage.py loaddata db.json
```
