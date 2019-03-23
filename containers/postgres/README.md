

## Docker build

```
$ cd [path-to-project]/containers/postgres
$ docker build --rm -t euonymus/gluons-postgres:[versioning-tag] .
```

## Run Docker container

```
$ docker run --name gluons-postgres --network gluons-network -p 5433:5432 -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=password -d euonymus/gluons-postgres:[versioning-tag]
```


## Show Database List

```
$ docker exec -it gluons-postgres psql -U postgres -l
```

## Access Permission check

```
$ docker exec -it gluons-postgres cat /var/lib/postgresql/data/pg_hba.conf
```

## Push Docker Image to Docker Hub

```
$ docker login
$ docker push euonymus/gluons-postgres:[versioning-tag]
```

---

You don't neet to do below explicitly, because these Database settings are already in sqls directory, and Dockerfile will copy them into container's docker-entrypoint-initdb.d directoly. then docker automatically executes these sql's


## Create user and database

```
$ docker exec -it gluons-postgres psql -U postgres -d template1
```

```
CREATE USER gluons WITH PASSWORD 'gluons';
CREATE DATABASE gluons;
GRANT ALL PRIVILEGES ON DATABASE gluons to gluons;
```


## Create PGroonga Index

```
docker exec -it gluons-postgres psql -U postgres -d gluons --command 'CREATE EXTENSION pgroonga'
```

