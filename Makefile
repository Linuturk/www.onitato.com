.PHONY: ci dev deps spell build submodule-init submodule-update server sync

defaults: dev

ci: submodule-init deps spell build
dev: spell server

deps:
	sudo apt update && sudo apt install aspell
	sudo pip3 install awscli
	bash ./install-hugo.sh

spell:
	bash spell content/post/*
	
build:
	hugo env
	hugo -v --cleanDestinationDir

submodule-init:
	git submodule update --init --recursive

submodule-update:
	git submodule update --remote --merge

server:
	hugo server --buildFuture --buildDrafts --buildExpired -D
