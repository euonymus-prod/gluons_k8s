# https://github.com/iquiw/docker-pgroonga-on-postgres/blob/master/Dockerfile
FROM postgres:11

RUN localedef -i ja_JP -c -f UTF-8 -A /usr/share/locale/locale.alias ja_JP.UTF-8
ENV LANG ja_JP.UTF-8
ENV DEBIAN_FRONTEND=noninteractive
ENV PGROONGA_VERSION=2.1.8

COPY sqls/*.sql /docker-entrypoint-initdb.d/
COPY groonga.list /tmp/

RUN apt-get update && \
    apt-get install -y apt-transport-https gcc make postgresql-server-dev-${PG_MAJOR} wget && \
    \
    mv /tmp/groonga.list /etc/apt/sources.list.d/ && \
    \
    apt-get update && \
    apt-get install -y --allow-unauthenticated groonga-keyring && \
    apt-get update && \
    apt-get install -y --no-install-recommends libgroonga-dev groonga-tokenizer-mecab && \
    \
    cd /usr/src && \
    wget https://packages.groonga.org/source/pgroonga/pgroonga-${PGROONGA_VERSION}.tar.gz && \
    tar xzf pgroonga-${PGROONGA_VERSION}.tar.gz && \
    \
    cd pgroonga-${PGROONGA_VERSION} && \
    make install && \
    apt-get purge -y --auto-remove gcc make postgresql-server-dev-${PG_MAJOR} wget && \
    rm -rf /usr/src/* /var/lib/apt/lists/*
