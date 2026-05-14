# Use bash in case you’re driving from xonsh
SHELL := /usr/bin/env bash
PY := .venv/bin/python
PIP := .venv/bin/pip

.PHONY: venv install bootstrap update recent views sanity

venv:
	python3 -m venv .venv

install: venv
	$(PIP) install -U pip
	$(PIP) install -r requirements.txt

bootstrap:
	$(PY) ingest.py bootstrap

update: recent
recent:
	$(PY) ingest.py update_recent

views:
	$(PY) ingest.py build-duck-views

sanity:
	$(PY) ingest.py sanity
