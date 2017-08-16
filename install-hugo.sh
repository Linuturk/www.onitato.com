#!/bin/bash

set -x
set -e

HUGO_VERSION=0.26
HUGO_DOWNLOAD=hugo_${HUGO_VERSION}_Linux-64bit.tar.gz

# Install Hugo if not already cached or upgrade an old version.
if [ ! -f $HOME/bin/hugo ] || ! [[ `hugo version` =~ v${HUGO_VERSION} ]]; then
	if [ ! -f /tmp/${HUGO_DOWNLOAD} ]; then
		wget https://github.com/gohugoio/hugo/releases/download/v${HUGO_VERSION}/${HUGO_DOWNLOAD} -O /tmp/${HUGO_DOWNLOAD}
	fi
  	tar xvzf /tmp/${HUGO_DOWNLOAD} hugo
  	mv hugo $HOME/bin/hugo
fi
