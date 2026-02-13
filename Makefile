.PHONY: ci dev deps spell build submodule-init submodule-update server sync

defaults: dev

ci: submodule-init deps spell build
dev: spell server

deps:
	apt update && apt install aspell curl unzip -y
	curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" && unzip -q awscliv2.zip && ./aws/install && rm -rf aws awscliv2.zip
	bash ./bin/install-hugo.sh
	bash ./bin/install-dart-sass.sh

spell:
	bash bin/spell content/post/*
	
build:
	hugo env
	hugo --logLevel info --cleanDestinationDir

submodule-init:
	git submodule update --init --recursive

submodule-update:
	git submodule update --remote --merge

server:
	hugo server --buildFuture --buildDrafts --buildExpired -D
