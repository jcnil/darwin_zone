# API Darwin Zone

## About The Project
Microservice allow compute and send email with account balance specific customer 

### Built With
* Language: Python 3.11.0
* Framework: FastApi

## Getting Started

This is an example of how you may follow instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Installation 

1. Install the virtual environment
```sh
$ python3 -p python3 venv
```
Activate the virtual environment with:
```sh
$ source venv/bin/activate
```
2. Install project requirements
```sh
$ pip3 install -r requirements.txt


Configuration
=============

## Set URL config

Env vars of external API:

ENV VAR    |   VALUES                                      |
---        |   ---                                         |
URL        | 'https://api.chucknorris.io/jokes/random'     | 

### Execution

### uvicorn Server
```sh
$ uvicorn main:app --host=0.0.0.0 --port=5000 --reload --log-level=info


Develop
=======

## Run Flake8

```sh
flake8 --exclude venv/ --max-line-length 120
```

or 

```sh
python -m flake8 --exclude venv/ --max-line-length 120
```

Contact
=======
* **José Nicolielly** - - [jcnil](https://github.com/jcnil/darwin_zone)