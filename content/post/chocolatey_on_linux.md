+++
title = "Running Chocolatey on Linux"
tags = [ "chocolatey", "choco", "linux", "mono" ]
topics = [ "tech" ]
slug = "running-chocolatey-on-linux"
date = "2017-01-26"
description = "Create Chocolatey packages on Linux."
+++

**Update:** This docker image is now available on the Docker Hub as [linuturk/mono-choco](https://hub.docker.com/r/linuturk/mono-choco/).

Do you want to create Chocolatey packages but don't want to run a Windows server? Use this Dockerfile to build Chocolatey and do your package development without a Windows system.

```Dockerfile
FROM mono:3.12.1

MAINTAINER Justin Phelps

RUN apt-get update && apt-get install -y wget unzip

WORKDIR /usr/local/src/choco
RUN wget https://github.com/chocolatey/choco/archive/stable.zip
RUN unzip stable.zip
RUN rm stable.zip

WORKDIR /usr/local/src/choco/choco-stable
RUN chmod +x build.sh
RUN chmod +x zip.sh
RUN ./build.sh

WORKDIR /usr/local/bin
RUN ln -s /usr/local/src/choco/choco-stable/build_output/chocolatey

COPY choco /usr/local/bin/choco

WORKDIR /root
```

In the same directory as the Dockerfile, place a file called **choco** with executable permissions. The content of this file should be:

```bash
#!/bin/bash

cd /usr/local/bin/chocolatey
mono choco.exe "$@" --allow-unofficial
```

Build the image like you would any docker image. In the directory with the Dockerfile run:

```bash
docker build -t choco .
```

Then, run a new container based on this new image:

```bash
docker run --rm -ti choco /bin/bash
```

Simply cd into the */usr/local/src/choco/choco-stable/build_output/chocolatey* directory and run **mono choco.exe -h** to test the install. Should work the way you are expecting.
