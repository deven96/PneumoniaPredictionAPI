# Pnuemonia Prediction API

Flask API for binary classification of xray images for pneumonia [PneumAI](https://github.com/deven96/PneumAI)

[![Build Status](https://travis-ci.org/deven96/PneumoniaPredictionAPI.svg?branch=master)](https://travis-ci.com/deven96/PneumoniaPredictionAPI)

![Docker Automated Build](https://img.shields.io/docker/automated/deven96/pneumonia-api.svg?style=flat)
![Docker Pulls](https://img.shields.io/docker/pulls/deven96/pneumonia-api.svg?style=flat)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

- [ImageQ API](#imageq-api)
  - [Getting Started](#getting-started)
    - [Installation](#installation)
  - [Running Locally](#running-locally)
  - [Deploy](#deploy)
  - [Documentation](#documentation)
  - [Todo](#todo)

## Getting Started

Clone the repo

```bash
    # SSH
    git clone git@github.com:deven96/PneumoniaPredictionAPI.git
    # HTTPS
    git clone https://github.com/deven96/PneumoniaPredictionAPI.git
```

Activate virtual environment. All project work should be done in virtualenvs and virtualenv names must be added to gitignore

### Installation

- Install the requirements

```bash
    # install pipenv
    sudo pip3 install pipenv

    # install requirements
    pipenv install
```

## Running Locally

- With flask dev server

```bash
    python flask_api/run_keras_server.py
```

- With Gunicorn (port 5000)

```bash
    gunicorn -b :5000 flask_api:app
```

## Deploy

The `/predict` endpoint on `master` branch of the repo is linked to automatically deploy to be hosted on [Google Cloud](https://imageqapi.appspot.com/predict)


## Documentation

Documentation including example use are available on [hosted version](https://pneumonia-api.appspot.com)

## Todo

- Move keras prediction to API (separate django or flask app)
- Setup GCP serving pipeline for API
- Integrate weight updates from colaboratory
