#!/usr/bin/env python

from setuptools import find_packages, setup

setup(
    name="{{ cookiecutter.project_slug }}",
    version="0.0.1",
    description="{{ cookiecutter.project_description }}",
    author="{{ cookiecutter.author_name }}",
    author_email="{{ cookiecutter.author_email }}",
    url="https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}",
    install_requires=[
        "lightning",
        "hydra-core",
    ],
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "{{ cookiecutter.project_slug }}-train = src.train:main",
            "{{ cookiecutter.project_slug }}-eval = src.eval:main",
        ]
    },
)

