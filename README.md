# Docker build

```
$ docker build -t euonymus/gluons-graphql:[versioning-tag] .
```

# Run Docker container on local

```
$ docker run -it --name [name the container freely] -p 8000:8000 euonymus/gluons-graphql:[versioning-tag]
```

# Push Docker Image to Docker Hub

```
$ docker login
$ docker push euonymus/gluons-graphql:[versioning-tag]
```
