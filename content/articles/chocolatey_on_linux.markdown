Title: Running Chocolatey on Linux
Tags: chocolatey choco linux mono
Category: tutorial
Slug: running-chocolatey-on-linux
Author: Justin Phelps
Date: 2017-01-26 0:00
Summary: Do you want to create Chocolatey packages but don't want to run a Windows server? Use this Dockerfile to build Chocolatey and do your package development without a Windows system.

Do you want to create Chocolatey packages but don't want to run a Windows server? Use this Dockerfile to build Chocolatey and do your package development without a Windows system.

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

Simply cd into the */usr/local/src/choco/choco-stable/build_output/chocolatey* directory and run **mono choco.exe -h** to test the install. Should work the way you are expecting.
