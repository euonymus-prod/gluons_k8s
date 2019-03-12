
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
* Apply gluons_graphql service

```
$ kubectl create namespace gluons
$ kubectl config set-context gluons --namespace=gluons --user=docker-for-desktop --cluster=docker-for-desktop-cluster
$ kubectl config use-context gluons
$ kubectl apply -f k8s/gluons_graphql
```

