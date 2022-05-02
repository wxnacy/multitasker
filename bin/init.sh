#!/usr/bin/env bash

# python = "^3.6.1"
# SQLAlchemy = "^1.4.35"
# rich = "^10.6.0"
# wpy = "^0.6.1"
# typer = "^0.4.1"
# pydantic = "^1.9.0"
# gevent = "^21.12.0"

# [tool.poetry.dev-dependencies]
# pytest = "^6.2.4"

for name in SQLAlchemy rich wpy typer pydantic gevent
do
    echo $name
    pt add $name
done

for name in pytest sphinx
do
    echo $name
    pt add -D $name
done

