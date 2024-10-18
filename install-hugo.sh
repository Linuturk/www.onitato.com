#!/bin/bash

set -x
set -e

HUGO_BIN=/usr/local/bin/hugo
# Fetch the latest Hugo version using GitHub API
HUGO_VERSION=$(curl -s https://api.github.com/repos/gohugoio/hugo/releases/latest | grep '"tag_name":' | sed -E 's/.*"v([^"]+)".*/\1/')
echo "Discovered Hugo version: $HUGO_VERSION"
HUGO_DOWNLOAD=hugo_extended_${HUGO_VERSION}_Linux-64bit.tar.gz

# Install Hugo if not already cached or upgrade an old version.
if [ ! -f $HUGO_BIN ] || ! [[ $(hugo version) =~ v${HUGO_VERSION} ]]; then
	if [ ! -f /tmp/${HUGO_DOWNLOAD} ]; then
		wget https://github.com/gohugoio/hugo/releases/download/v${HUGO_VERSION}/${HUGO_DOWNLOAD} -O /tmp/${HUGO_DOWNLOAD}
	fi
	tar xvzf /tmp/${HUGO_DOWNLOAD} hugo
	mv hugo $HUGO_BIN
fi
