
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

```
$ docker run -it --name gluons-graphql --network gluons-network -p 8000:8000 euonymus/gluons-graphql:[versioning-tag]
```

## Database migration

docker exec -it gluons-graphql python manage.py makemigrations
docker exec -it gluons-graphql python manage.py migrate


## Push Docker Image to Docker Hub

```
$ docker login
$ docker push euonymus/gluons-graphql:[versioning-tag]
```

