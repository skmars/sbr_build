# Sbr Build Lite 🎮

This is a part of a Build System for GameDev for allowing machines to create builds automatically.

#### *Table of contents*:
<!-- toc -->

- [Sbr Build Lite 🎮](#sbr-build-lite-)
      - [*Table of contents*:](#table-of-contents)
  - [Features](#features)
  - [Tools](#tools)
  - [Commands for local development with docker compose](#commands-for-local-development-with-docker-compose)
  - [Few-words](#few-words)
<!-- tocstop -->

---
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
sudo docker compose -f docker-composel.yaml up -d
``` 
   
2. Open <http://localhost:8000/docs>  to test API.
As an example:
```json
{
     "build": "reach_wind"
}

```   
   
## Few-words

*Here we have a simple example of my sort of "hometask"*.
*Of course one could spent much more time to make this micro-microservice much more stable, extensible and covered by more tests.*
*But I was really excited to make it and at least few words from you guyes will be appriciated.*
*And no matter what, wish you all the best, stay safe and sound!* 💫