
## Prepare Local Env

```
$ cd [path-to-project]/containers/gluons_graphql
$ python -m venv venv
$ source venv/bin/activate
$ pip install --upgrade pip
$ pip install -r requirements.txt

```

## Run locally with builtin server

```
$ cd [path-to-project]/containers/gluons_graphql
$ python manage.py runserver
```

## Run locally with gunicorn

```
$ cd [path-to-project]/containers/gluons_graphql
$ gunicorn -b :8000 gluons.wsgi
```


## Docker build

```
$ cd [path-to-project]/containers/gluons_graphql
$ docker build -t euonymus/gluons-graphql:[versioning-tag] .
```

## Run Docker container on local

You neet to create gluons-network before you create gluons-graphql
See: /containers/postgres/README.md


```
$ docker run -it --name gluons-graphql --network gluons-network -p 8000:8000 euonymus/gluons-graphql:[versioning-tag]
```

## Push Docker Image to Docker Hub

```
$ docker login
$ docker push euonymus/gluons-graphql:[versioning-tag]
```
