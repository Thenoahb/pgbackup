#!/usr/bin/env python3


from setuptools import setup, find_packages

with open("README.rst", encoding = "UTF-8") as f:
	readme = f.read()

setup(
	name = "pgbackup",
	version = "0.1.0",
	description = "Creates a backup of my database locally or to AWS S3",
	long_description = readme,
	author = "Noah Bessler",
	author_email = "besslern2@nku.edu",
	packages = find_packages("src"),
	package_dir = {"":"src"},
	install_requires = []
	)