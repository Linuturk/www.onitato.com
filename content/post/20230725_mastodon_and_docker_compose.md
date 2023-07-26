+++
title = "Mastodon and Docker Compose"
tags = [ "fediverse", "mastodon", "docker", "compose" ]
topics = [ "tech" ]
slug = "mastodon-and-docker-compose"
date = "2023-07-25 21:00:00"
description = "This is how I run Mastodon using Docker Compose"
draft = true
+++

## Docker Compose

I use Traefik as my reverse proxy. Here is a snippet of my Docker Compose file for Mastodon:

```yaml
######################
# Mastodon           #
######################
  mastodon-db:
    image: postgres:14-alpine
    container_name: mastodon-db
    shm_size: 256mb
    environment:
      - UID=${PUID}
      - GID=${PGID}
      - TZ=${TZ}
      - POSTGRES_HOST_AUTH_METHOD=trust
    volumes:
      - /root/docker/appdata/mastodon/dbdata:/var/lib/postgresql/data
    labels:
      - "com.centurylinklabs.watchtower.enable=true"
    restart: unless-stopped
  mastodon-redis:
    image: redis:7-alpine
    container_name: mastodon-redis
    environment:
      - UID=${PUID}
      - GID=${PGID}
      - TZ=${TZ}
    volumes:
      - /root/docker/appdata/mastodon/redis:/data
    labels:
      - "com.centurylinklabs.watchtower.enable=true"
    restart: unless-stopped
  mastodon-web:
    image: tootsuite/mastodon
    container_name: mastodon-web
    command: bash -c "rm -f /mastodon/tmp/pids/server.pid; bundle exec rails s -p 3000"
    env_file:
      - .mastodon.env
    environment:
      - UID=${PUID}
      - GID=${PGID}
      - TZ=${TZ}
    volumes:
      - /root/docker/appdata/mastodon/public/system:/mastodon/public/system
    labels:
      - "traefik.enable=true"
      - "traefik.http.routers.mastodon-web.rule=Host(`toot.onitato.com`)"
      - "traefik.http.routers.mastodon-web.entrypoints=https"
      - "traefik.http.routers.mastodon-web.tls=true"
      - "traefik.http.routers.mastodon-web.tls.certresolver=letsencrypt"
      - "traefik.http.routers.mastodon-web.middlewares=authelia@docker"
      - "com.centurylinklabs.watchtower.enable=true"
    ports:
      - "3000:3000"
    restart: unless-stopped
    depends_on:
      - traefik
      - mastodon-redis
      - mastodon-db
  mastodon-streaming:
    image: tootsuite/mastodon
    container_name: mastodon-streaming
    command: node ./streaming
    env_file:
      - .mastodon.env
    environment:
      - UID=${PUID}
      - GID=${PGID}
      - TZ=${TZ}
    labels:
      - "traefik.enable=true"
      - "traefik.http.services.mastodon-web.loadbalancer.server.port=4000"
      - "traefik.http.routers.mastodon-streaming.rule=(Host(`toot.onitato.com`) && PathPrefix(`/api/v1/streaming`))"
      - "traefik.http.routers.mastodon-streaming.entrypoints=https"
      - "traefik.http.routers.mastodon-streaming.tls=true"
      - "traefik.http.routers.mastodon-streaming.tls.certresolver=letsencrypt"
      - "traefik.http.routers.mastodon-streaming.middlewares=authelia@docker"
      - "com.centurylinklabs.watchtower.enable=true"
    ports:
      - "4000:4000"
    restart: unless-stopped
    depends_on:
      - traefik
      - mastodon-redis
      - mastodon-db
  mastodon-sidekiq:
    image: tootsuite/mastodon
    container_name: mastodon-sidekiq
    command: bundle exec sidekiq
    env_file:
      - .mastodon.env
    environment:
      - UID=${PUID}
      - GID=${PGID}
      - TZ=${TZ}
    volumes:
      - /root/docker/appdata/mastodon/public/system:/mastodon/public/system
    labels:
      - "com.centurylinklabs.watchtower.enable=true"
    restart: unless-stopped
    depends_on:
      - mastodon-redis
      - mastodon-db
```

## mastodon.env

mastodon.env was generated using these instructions:

```env
# This is a sample configuration file. You can generate your configuration
# with the `rake mastodon:setup` interactive setup wizard, but to customize
# your setup even further, you'll need to edit it manually. This sample does
# not demonstrate all available configuration options. Please look at
# https://docs.joinmastodon.org/admin/config/ for the full documentation.

# Note that this file accepts slightly different syntax depending on whether
# you are using `docker-compose` or not. In particular, if you use
# `docker-compose`, the value of each declared variable will be taken verbatim,
# including surrounding quotes.
# See: https://github.com/mastodon/mastodon/issues/16895

# continues with a bunch of secrets
```

Hope this was helpful in getting your own Mastodon instance up and running.
