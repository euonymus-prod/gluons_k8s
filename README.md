
# Steps to build local docker network

* Create gluons-network
* Build postgres container
* Build gluons_graphql container


## Create docker network

```
$ docker network create gluons-network
```

## Build postgres container

See [postgres](https://github.com/euonymus-prod/gluons_k8s/blob/master/containers/postgres/README.md)


## Build gluons_graphql container

See [gluons_graphql](https://github.com/euonymus-prod/gluons_k8s/blob/master/containers/gluons_graphql/README.md)



# Steps to build local Kubernetes Cluster for Docker for Mac

* Create Namespace
* Create Context
* Change Context
* Apply Postgres config
* Apply Application config
* Apply Initial Jobs

## Namespace preparation

```
$ kubectl create namespace gluons
$ kubectl config set-context gluons --namespace=gluons --user=docker-for-desktop --cluster=docker-for-desktop-cluster
$ kubectl config use-context gluons
```

## Apply Kubeconfigs

```
$ kubectl apply -f k8s/postgres_common
$ kubectl apply -f k8s/postgres_local
$ kubectl apply -f k8s/gluons_graphql
$ kubectl apply -f k8s/gluons_graphql_init
```

