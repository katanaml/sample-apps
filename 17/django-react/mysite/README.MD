## Based on this tutorial

[Integrating a Modern JavaScript Pipeline into a Django Application](https://www.saaspegasus.com/guides/modern-javascript-for-django-developers/integrating-javascript-pipeline/)

## Django setup

```
pip install django
```

```
django-admin startproject mysite
```

```
python manage.py startapp myapp
```

```
python manage.py migrate
```

```
python manage.py runserver
```

## Webpack setup

```
npm init -y
npm install webpack webpack-cli --save-dev
```

```
npm run dev
```

## Connecting webpack bundles to Django

Run Django server

```
http://localhost:8000/hello-webpack/
```

## Setting up React with Babel

```
npm install --save-dev babel-loader @babel/core @babel/preset-env @babel/preset-react
```

```
npm install --save react react-dom
```

```
npm run dev
```