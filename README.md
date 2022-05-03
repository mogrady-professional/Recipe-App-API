<h1 align="center">Python Django RestAPI Development with Docker and TDD (Test Driven Development) Reference</h1>

# Introduction

> Building an API in Python using Test Driven Development.

- [Introduction](#introduction)
- [Project: Recipe API](#project-recipe-api)
  - [What You'll learn](#what-youll-learn)
  - [End goal](#end-goal)
- [Introduction](#introduction-1)
  - [Technologies](#technologies)
    - [Python](#python)
    - [PEP-8](#pep-8)
    - [Django](#django)
    - [Django REST framwork](#django-rest-framwork)
    - [Docker](#docker)
    - [Travis CI](#travis-ci)
    - [PostgreSQL](#postgresql)
- [Unit Tests](#unit-tests)
  - [Test Stages](#test-stages)
    - [Why write Unit Tests?](#why-write-unit-tests)
    - [Test Driven Development (TDD)](#test-driven-development-tdd)
      - [Why use TDD?](#why-use-tdd)
- [Installation and Setup](#installation-and-setup)
- [Project Name: Recipe App API](#project-name-recipe-app-api)
- [Docker](#docker-1)
  - [Specifying Major an Minor Versions of Dependencies](#specifying-major-an-minor-versions-of-dependencies)
  - [Build docker image](#build-docker-image)
  - [Creating a Docker Compose File - and configuration](#creating-a-docker-compose-file---and-configuration)
- [Creating a Django Project using the Docker Configuration](#creating-a-django-project-using-the-docker-configuration)
- [CI/CD Testing](#cicd-testing)
  - [Option 1: Travis-CI](#option-1-travis-ci)
  - [Setting up Travis-CI](#setting-up-travis-ci)
  - [Create Travis-CI Configuration File](#create-travis-ci-configuration-file)
  - [Option 2: GitHub Actions](#option-2-github-actions)
- [Test Driven Development (TDD)](#test-driven-development-tdd-1)
  - [Unit Test](#unit-test)

TDD (Test Driven Development) is what seperates the good developers from the great ones.

Test Driven Development greatly improves:

1. Code Quality
2. Comprehension
3. Confidence

> Rarely implemented properly, as it's challenging to get right.

This project will demonstrate the best practice principles of TDD.

Going to create the following using Test Driven Development

- A fully functional RestAPI that will handle
  - Authentication
  - Creating Objects
  - Filtering
  - Uploading Images
  - More

# Project: Recipe API

Virtual Recipe Box that you can use to organise your favourite recipes by:

- Title
- Ingredients
- Cooking Time
- Tags
- Images

## What You'll learn

- Python
- Django
- Django Rest Framework
- Docker
- Travis CI
- PostgreSQL

## End goal

You will have a fully functional RestAPI that you can use as a foundation for future projects e.g. mobile or web based apps.

```py
# Manage users
/api/user/create
/api/user/token
/api/user/me

# Manage Recipies
/api/recipe/tags
/api/recipe/ingredients
/api/recipe/recipe
/api/recipe/recipe<id>/
/api/recipe/recipe<id>/upload-image

```

# Introduction

Main Features of an API which you'll learn:

- User Authentication
- Creating Objects
- Listing/Filtering
- Uploading Images

After completion, you can build your on frontend. This is set at advanced level.

## Technologies

### Python

- Python 3.7
  - Application logic and tests
  - PEP-8 best practice guidelines
    - Keeping all lines to a miximum of 79 characters
    - Adding docstrings to functions
    - Code linting tool to automatically check code and notify if any guidelines are broken

### PEP-8

PEP 8 – Style Guide for Python Code. The primary focus of PEP 8 is to improve the readability and consistency of Python code. PEP stands for Python Enhancement Proposal, and there are several of them. A PEP is a document that describes new features proposed for Python and documents aspects of Python, like design and style, for the community.

Practicing the [PEP-8 guidelines](https://peps.python.org/pep-0008/) makes you stand out amoungst other developers and future collegues appreciate it when reviewing and maintaining your code.

Linting tool [Flake8](https://pypi.org/project/flake8/).

### Django

- Django is used as the web framework that underpins the API.

> Django is a popular framework used for building web applications which comes with many great features when building web applications rapidly. The main features we will be using are:

- Object Relational Mapper (ORM)
  - Easy to use way for converting objects in the API to rows in the database
    - e.g. Django model for recipe objects, and Django will automatically create the recipe table and an easy to use interface for matching rows in the table.
- Django Admin
  - Out of the box admin site to help managing models in the database.
  - Great for testing on local machine

### Django REST framwork

- Extension to Django which offers a lot of features for building REST API's.
  - Built-in Authentication System -> to add to API end-points.
  - Django Rest framework **viewsets** to create the structure of the API and provide all the necessary endpoints for managing objects.
  - **Serializers** to provide validation on all requests to the API, and help convert JSON objects to Django database models.
  - **Browsable API** that you can use to test endpoints in the browser as you go.

### Docker

Isolate project dependencies from the machine it's running on. Kind of like a super lightweight virtual machine.

- Used to wrap project and dependencies into a single image that can be run independently on any machine
- Provides a consistent development environment across multiple machines
- Used to deploy project to a cloud platform such as AWS, Azure or Google Cloud.

### Travis CI

A continuous integration tool that integrates well with GitHub. You can configure Travis-CI to run a script anytime everytime you make changes to your code.

- Automatically run linting and unit tests anytime you make changes to your code.
- Write a script that will run unit tests and linting tool, and if either of those two fail, Travis-CI will notify you by email that the build is broken. This is a common practice employed by all serious development teams as it helps identify issues early before they end up in production code or deployed in the end product.

### PostgreSQL

Will be used as the database.

- Open source, production grade database
- Easy to get up and running with docker

# Unit Tests

When writing software, it's important to include unit tests with your code.

- Check that your code works and does what it's supposed to do
- Start by isolating the particular piece of code to be tested.
  - Function
  - Class
    In this project, will be testing the API calls to our endpoints. Knowing which code to target comes with practice.

## Test Stages

Tests are broken down into three stages:

1. Setup
   1. Create sample database objects, which you use to test code
      1. e.g. create sample recipe to test endpoint
2. Execution
   1. Call the code via testing
      1. e.g. call recipe update endpoint with the ID of the recipe and some sample fields to update
3. Assertions
   1. e.g. ensure that the appropriate fields in the sample recipe were updated with the correct values

### Why write Unit Tests?

Professional development teams have a policy that they must be written for all code.

- Expected in most professional dev teams
- Makes it a lot easier to maintain and make changes to your code
  - Making changes to code with great test coverage, you can be confident that if something breaks as a side effect of the change, you'll know about it when the tests run. This way you can identify and fix issues before they end up in the production build.
- Takes more time at first, but in the long run it saves time because adding features and making changes becomes a lot easier with the added confidence that tests bring.
- Encourates developers to write testable code.
  - In order for code to be testible, there must be a clear **input** and **output** in each unit of code.
    - This also happens to make easy to read, reliable code. Testable code = quality code.

### Test Driven Development (TDD)

The classic way to write Unit Tests is to write a piece of code and write a unit test. With **Test Driven Development**, you switch around.

- Start by writing the unit test
- Ensure the test fails
- Implement the code or feature to make sure the test passes

#### Why use TDD?

Benefits of doing it this way:

- Increases test coverage
  - **You can be sure that all code written by TDD has been tested**
  - **Helps to make sure that your tests actually work**
    - Just as there can be bugs in regular code, there can also be bugs in test code.
    - It is possible that if there is a mistake in your test, that it will always pass wherther it works or not. **Test Driven Development** helps avoid this.
      - **You check that your test fails before, and passes after you implement the feature.**
      - TDD encourages quality code since bad code is often difficult to test.
    - **Unit Tests serve as a guideline for when to stop coding.**
      - Helps keep you on track and focused.

# Installation and Setup

# Project Name: Recipe App API

# Docker

- Create `Dockerfile` at the root directory of the project
  - A dockerfile is simply a list of instructions for docker to build a dockerimage.
    - Dependencies that you need for your project are described in the dockerfile

```
...
└── Dockerfile
```

The first line of the Dockerfile is the image that you inherit the Dockerfile from. With docker you can build images on top of other images, the benefit is that you can fild an image that has everything you need for your project and you can add any further requirements for your specific project. Find a list of available docker images on [Dockerhub](https://hub.docker.com/) that you can use to base your project on.

> Create the Python file using the Python 3.7 image

- Search for Python
  - Scroll to `Simple Tags`
    - For this project, will be using `3.7-alpine`

This is a lightweight version of docker (alpine) and runs python 3.7.

- Run python in unbuffered mode which is recommended when running python within docker containers. The reason for this is it does not allow python to buffer the outputs, it just prints them directly, this avoids complications when running the application.
- Next, install the dependencies. The dependencies will be stored in a `requirements.txt` file. Need to copy the `requirements.txt` from the file adjacent to the dockerfile and copy it on the docker image to inside the image.
- Next take the `requirements.txt` file just copied and install it using pip in the dockerimage.
- Next, make a directory within docker image that can be used to store application source code, set as the default working directory, copies from the local machine the `.app` folder to the `.app` folder created on the image. This allows you to take the code that is created in the project on the local computer and copy it into the dockerimage.
- Next, create user that is going to run the application using docker.
- Switch to that user
  - This is for security purposes. _If you don't do this then the image will run the application using the root account which is not recommended as if someone compromises the application they can have root access to the image and do malicious actions_. **Creating a seperate user just for the application limits the scope that an attacker can have within the container**.

Type the following into the `Dockerfile`

```PY
FROM python:3.7-alpine
LABEL maintainer="Michael O'Grady"

ENV PYTHONUNBUFFERED 1 # Set Environment Variable in docker build

# Install dependencies
COPY ./requirements.txt /requirements.txt # Copy in requirements file into image

RUN pip install -r /requirements.txt # Install requirements into image

RUN mkdir /app # Create directory to store source code
WORKDIR /app # Set as default working directory
COPY ./app /app # Copy source code from local machine into the image


RUN adduser -D user # Create user to run the application processes using docker
USER user # Switch to that user just created

```

Find required packages on the [Python Package Index (PyPI)](https://pypi.org/).

## Specifying Major an Minor Versions of Dependencies

When using the Django example below, this means to install Django that is equal to, or higher than 2.1.3 but less than 2.2.0. The reason you do this is to take the minor version, which is the last number and make sure that you install the latest available version, as that typically is the version that has the security features, security fixes and typically does not have breaking changes, so you can be confident that your app, when you rebuild the docker image will have the latest security patches but may not have the latest version which may contain changes that break the project.

Create `requirements.txt` file:

1. Install Django
2. Install djangorestframework
3. Install flake8

```py
Django>=2.1.3,<2.2.0
djangorestframework>=3.9.0,<3.10.0
flake8>=3.6.0,<3.7.0
```

Create directory called `app` which is required for docker file to build.

## Build docker image

Build whichever Dockerfile is in the root of the project you are currently in.

In the terminal type:

- `docker build .`

## Creating a Docker Compose File - and configuration

Docker compose is a tool that allows you to run the docker image easily from project location. This allows the management of different services that make up the project, e.g. one service may be the python application, another may be the database.

- Create a Docker Compose file
  - Create a File in the root directory `docker-compose.yml`

This is a YAML file that contains the configuration for all of the services that make the project.

- First line is the version of docker compose that you're going to be writing the file for.
- Second define the services that make up the application
  - Right now only one service is needed in this project for the python django application.
    - This means there's a service called `app` and the build section of the configuration, set the context to `. ` which is the current directory that you are running docker compose from.
    - Next, type the port configuration. Map the project from port 8000 on host machine to 8000 on the image.
    - Add volume. This allows you to get the updates made to the project into the docker image in real time, so it maps a volume from local machine into docker container ruunning the application. **This means whenever you make changes it will be automatically updated in the container and you do not need to restart docker to get the changes into effect.**
      - Maps the app directory to the app directory in the docker image
    - Write the command that is used to run the application in the docker container.
      - Run the command using shell
    - Runs a django development server available on all ip addresses that run on the docker container and run on port 8000 which is mapped through the port configuration to the local machine. So you can run the application and connect to it on the local machine.

```
version: "3"
services:
  app:
    build:
      context: .
    ports:
      - "8080:8080"
    volumes:
      - ./app:/app
    command: >
      sh -c "python manage.py runserver 0.0.0.0:8000"
```

- Build the image:
  - Type `docker-compose build`

# Creating a Django Project using the Docker Configuration

Docker compose to run a command on the image that contains the Django dependency which will create the project files that you need for the app. **Run commands using docker-compose** and the name of the service you want to run the command on within the linux container that was created using the dockerfile.

- Run the following command which runs a shell script passing the command in speech marks here. By using `sh -c`, is makes it very clear to see the command you are running on versus the docker compose command. You could run the command without using sh -c, but this just makes it very clear: what is the command you are running, and what is the docker compose syntatic sugar that goes around it.
- This will run the Django admin management command and starts a new project called app and `.` in the current location.
  - This process runs on the docker container, and base it from the `WORKDIR` in the `Dockerfile`.
    - `docker-compose run app sh -c *django-admin.py startproject app .*`
    - or alternatively, run `docker-compose run app django-admin.py startproject app .`

# CI/CD Testing

## Option 1: Travis-CI

Enable Travis-CI for a GitHub project. Travis is a really useful continuous integration tool that lets you automate tests and checks on your project everytime you push it to GitHub. For example, everytime you push a change to GitHub you can make it run **Python Unit Tests** and **Python Linting** so if there is any issues with your code you can see straight away via an email notification that the build is broken.

## Setting up Travis-CI

An easy process, [On the Travis-CI website, sign in with GitHub](https://travis-ci.com/), this will pull in all your GitHub projects and selectively enable with Travis.

## Create Travis-CI Configuration File

This is the file that tells Travis what to do every time you push a change to the project.

- To create a Travis-CI Configuration file:
  - Create a File in the root directory of the project called `.travis.yml`
    - On the first line you tell Travis what language to expect our project to be in
      - Version
    - What services needed to use
    - Specify a before script which is a script Travis will run before execute any of the automation commands
    - Evertime you push a change to GitHub, Travis is going to spin up a python server running python 3.6 and make the docker service available, and use pip to install docker compose and then run script (flake8 is used as linting tool).
      - If this exits with a failure, it will fail the build and send notification.

```
language: python
python:
    - "3.6"

services:
    - docker

before_script: pip install docker-compose

script:
    - docker-compose run app sh -c "python manage.py test && flake8"

```

- Adding a flake8 config file
  - Within the project `app` create a File called .flake8

Directory structure

```py
app
├── app
|   ├── __init__.py
|   ├── .flake8
|   ├── settings.py
|   ├── urls.py
│   └── wsgi.py
└── ...
```

Add exclusions: automated scripts and tools created by Django, as Django works to a 100 character limit, where as 79 character limit is recommended by Python guidelines. Doing this, you can exclude the Django limit so it does not fail on the linting.

`.flake8`

```
[flake8]
exclude =
    migrations
    __pycache__,
    manage.py,
    settings.py
```

Now you can push to GitHub and Travis-CI will begin the build.

## Option 2: GitHub Actions

This is the method used within this project as "Travis-CI no longer offers a free tier and we are working on a course update which uses GitHub Actions instead."

1. Register on Docker Hub
   1. If you don't already have one, head over to [hub.docker.com](https://hub.docker.com/) and register for a new free account.
   2. Under Account Settings > Security, create a new Access Token.

Under Account Settings > Security, create a new Access Token.

- Access Token: `00400038-d5b8-47c2-9c88-4ffe219403e0`

---

To use the access token from your Docker CLI client:

- Run docker login -u mogradyprof
- At the password prompt, enter the personal access token.

---

2. Add credentials to your GitHub Repo

- Open repo on GitHub, select Settings:
  - Select Secrets > Actions:
    - Choose New repository secret (top right):
    - Add the following two secrets to the repo:
      - `DOCKERHUB_USER` - Your Docker Hub username.
      - `DOCKERHUB_TOKEN` - Access token created during step 1 above.
      -

3. Add the GitHub Actions configuration file

- Create a new file at .github/workflows/build.yml and add the following contents:

```
---
name: Checks

on: [push]

jobs:
  test-lint:
    name: Test and Lint
    runs-on: ubuntu-20.04
    steps:
      - name: Login to Docker Hub
        uses: docker/login-action@v1
        with:
          username: ${{ secrets.DOCKERHUB_USER }}
          password: ${{ secrets.DOCKERHUB_TOKEN }}
      - name: Checkout
        uses: actions/checkout@v2
      - name: Test
        run: docker-compose up -d && docker-compose run --rm app sh -c "python manage.py test"
      - name: Lint
        run: docker-compose run --rm app sh -c "flake8"
```

4. Push the changes, and you should see the GitHub Actions job running under Actions on the repo page.

# Test Driven Development (TDD)

## Unit Test
