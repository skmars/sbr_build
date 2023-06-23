# Sbr Build Lite 🎮

This is a part of a Build System for GameDev for allowing machines to create builds automatically.


#### *Table of contents*:
<!-- toc -->

- [Sbr Build Lite 🎮](#sbr-build-lite-)
      - [*Table of contents*:](#table-of-contents)
  - [About](#about)
  - [Features](#features)
  - [Tools](#tools)
  - [Commands for local development with docker compose](#commands-for-local-development-with-docker-compose)
  - [*PS](#ps)
<!-- tocstop -->

---

## About

There are two files in 'builds' directory
 - In first we have objects *builds* consist of tasks to builds. 
 - In second we have objects *tasks* consit of depependant tasks.
We need to get all build tasks. And we have one condition: tasks can't be completed before all it's dependencies.


## Features

Sort build related tasks regarding the condition the task cannot be completed before all its dependencies.

**API endpoint:**

`POST` to `/get-tasks` requires JSON body with build name.

## Tools

- FastAPI - modern asynchronuous web framework based on Starlette
- MongoDB - NOSQL, document-oriented DB
- Docker - container image executable package of software to run an application
- Linters - (flake8, black, isort, pre-commit) 

## Commands for local development with docker compose

1. To bild all Docker containers:
```
docker compose build
```
- To run everything
  - if you use Linux OS:
```
make up
```
  - if you use Windows OS:
```
docker compose -f docker-composel.yaml up -d
``` 
   
2. Open <http://localhost:8000/docs>  to test API.
As an example:
```json
{
     "build": "reach_wind"
}

```   
## *PS
 It's a small test-microservice to build up.