#!/bin/bash

set -x
set -e

# Fetch the latest Dart Sass version using GitHub API
DART_SASS_VERSION=$(curl -s https://api.github.com/repos/sass/dart-sass/releases/latest | grep '"tag_name":' | sed -E 's/.*"([^"]+)".*/\1/')
echo "Discovered Dart Sass version: $DART_SASS_VERSION"

curl -LJO "https://github.com/sass/dart-sass/releases/download/${DART_SASS_VERSION}/dart-sass-${DART_SASS_VERSION}-linux-x64.tar.gz"
tar -xf "dart-sass-${DART_SASS_VERSION}-linux-x64.tar.gz"
cp -r dart-sass/* /usr/local/bin
rm -rf dart-sass*
