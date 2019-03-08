
## Create docker network

```
$ docker network create gluons-network
```


## Run Docker container

```
$ docker run --name gluons-postgres --network gluons-network -p 5433:5432 -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=password -d postgres:11.2
```
