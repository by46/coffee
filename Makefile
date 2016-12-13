#!/usr/bin/env bash

LINK=pyinstaller
COVER=coverage
CWD=$(shell pwd)
VERSION=$(shell python ./tools/version.py)
NAME=Falcon.0.1

.PHONY: test clean release debug

release:
	@$(LINK)  --distpath=$(NAME) run.py --name=falcon