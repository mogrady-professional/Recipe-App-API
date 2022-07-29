<h1 align="center">Recipe-App-API</h1>
<h1 align="center">Backend REST API with Python Django</h1>

> Python Django RestAPI Development with Docker and TDD (Test Driven Development) Reference

# Introduction

> Building an API in Python using Test Driven Development.

# Getting started

To start project

1. disable VPN (during docker build)
2. Start docker
3. Run `docker build .` in the root directory `/` to build docker image
4. Run `docker-compose up` to build container with image and **start the server**
5. Run `docker-compose run app sh -c "python manage.py createsuperuser"` to create superuser in Django
6. Log in to the Django admin panel with the superuser credentials [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)
7. Add in sample data, i.e. ingredients, recipies, tags, users (as required) in the Django Admin Panel
8. Optionally use [Postman](https://www.postman.com/) to send requests via routes below; set up routes in Postman for requests
9. Optionally, use [ModHeader](https://modheader.com/) to send token within header when making requests in chrome browser

# Accessing the Routes / API via Postman

> Import the JSON file into Postman to save yourself the trouble of having to create the routes in Postman yourself.

- **Attached Postman routes colection**
  - `Recipe-App Python Django backend API.postman_collection.json`

## Postman Setup instructions for non Authenticated Routes

### Create User

- Create user - POST - `http://127.0.0.1:8000/api/user/token/`
  - Body - form-data
    - key: `email`
      - value: `your_email_goes_here`
    - key: `password`
      - value: `your_password_goes_here`
    - key: `name`
      - value: `your_name_goes_here`

> Returns new user's email, name

## Postman Setup instructions for Authenticated Routes

> Firstly, get authenticated:

### Get Token

- Get token : **POST** - `http://127.0.0.1:8000/api/user/token/`
  - Body
    - form-data
      - key: `email`
        - value: `your_email_goes_here`
      - key: `password`
        - value: `your_password_goes_here`

> Returns token

1. Retrieve the token
2. In subsequent requests, within `Headers` add:

- Key: `Authorization`
- Value: `token your_authorization_token_goes_here`

4. You can now proceed to use the Authenticated routes below provided you add the following to each request in Postman

- `token`

### Authenticated routes

#### Get User Details

- Get user details : **GET** - `http://127.0.0.1:8000/api/user/me/`
  - `Headers`
    - key: `Authorization`
      -value: `token your_token_goes_here`

> returns user email, name

#### Manage Recipies

##### Tags

- Get tags : **GET** - `http://127.0.0.1:8000/api/recipe/tags/`
  - `Headers`
    - key: `Authorization`
      -value: `token your_token_goes_here`

> returns tags

- Create tag : **POST** - `http://127.0.0.1:8000/api/recipe/tags/`
  - `Headers`
    - key: `Authorization`
      - value: `token your_token_goes_here`
  - `Body`
    - `form-data`
      - `KEY`: `name`
        - `VALUE` : `tagname_goes_here`

> returns tag

##### Ingredients

- Get ingredients : **GET** - `http://127.0.0.1:8000/api/recipe/ingredients/`
  - `Headers`
    - key: `Authorization`
      - value: `token your_token_goes_here`

> returns ingredients

- Create ingredient : **POST** - `http://127.0.0.1:8000/api/recipe/ingredients/`
  - `Headers`
    - key: `Authorization`
      - value: `token your_token_goes_here`
  - `Body`
    - `form-data`
      - `KEY`: `name`
        - `VALUE` : `ingredient_goes_here`

> returns ingredient

##### Recipies

- Get recipies : **GET** - `http://127.0.0.1:8000/api/recipe/recipes/`
  - `Headers`
    - key: `Authorization`
      -value: `token your_token_goes_here`

> returns recipies

- Craete recipie : **POST** - `http://127.0.0.1:8000/api/recipe/recipes/`
  - `Headers`
    - key: `Authorization`
      - value: `token your_token_goes_here`
  - `Body`
    - `form-data`
      - `KEY`: `title`
        - `VALUE` : `recipe_name_goes_here`
      - `KEY`: `ingredients`
        - `VALUE` : `ingredients_go_here`
      - `KEY`: `tags`
        - `VALUE` : `tags_go_here`
      - `KEY`: `time_minutes`
        - `VALUE` : `time_minutes_go_here`
      - `KEY`: `price`
        - `VALUE` : `price_goes_here`
      - `KEY`: `link`
        - `VALUE` : `link_goes_here`

> returns recipies

##### Recipe<id>

- Get recipe : GET - `http://127.0.0.1:8000/api/recipe/recipes/1/`
  - `Headers`
    - key: `Authorization`
      -value: `token your_token_goes_here`

> returns recipe

##### Recipe<id>upload-image

- Post recipie image : **POST** - `http://127.0.0.1:8000/api/recipe/recipes/1/upload-image/`
  - `Headers`
    - key: `Authorization`
      - value: `token your_token_goes_here`
  - `Body`
    - `form-data`
      - `KEY`: `link`
        - `VALUE` : `link_name_goes_here`

> returns id, link

---

```py
# Routes

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

# URL Routes

> You can view the following routes in your browser to view the endpoints in the Django REST Framework:

## Manage users

- Create User
  - [http://127.0.0.1:8000/api/user/create/](http://127.0.0.1:8000/api/user/create/)
- Create Token
  - [http://127.0.0.1:8000/api/user/token/](http://127.0.0.1:8000/api/user/token/)
- Manage User
  - [http://127.0.0.1:8000/api/user/me/](http://127.0.0.1:8000/api/user/me/)

## Manage Recipies

- Tag List
  - [http://127.0.0.1:8000/api/recipe/tags/](http://127.0.0.1:8000/api/recipe/tags/)
- Ingredients List
  - [http://127.0.0.1:8000/api/recipe/ingredients/](http://127.0.0.1:8000/api/recipe/ingredients/)
- Recipies
  - [http://127.0.0.1:8000/api/recipe/recipe](http://127.0.0.1:8000/api/recipe/recipe)
  - Recipe
    - [http://127.0.0.1:8000/api/recipe/recipe\<id>/](http://127.0.0.1:8000/api/recipe/recipe<id>)
  - Upload Recipe Image
    - [http://127.0.0.1:8000/api/recipe/recipe%3Cid%3E/upload-image](http://127.0.0.1:8000/api/recipe/recipe%3Cid%3E/upload-image)

# Finishing up

- Stop the server using ctrl + c in the terminal
- Remove the image and the container using Docker desktop GUI

---

# Testing

Both the following are used:

- Travis-CI to automate testing and linting at each GitHub push
- GitHub Actions to automate testing and linting at each GitHub push

---

# Table of Contents

- [Introduction](#introduction)
- [Getting started](#getting-started)
- [Accessing the Routes / API via Postman](#accessing-the-routes--api-via-postman)
  - [Postman Setup instructions for non Authenticated Routes](#postman-setup-instructions-for-non-authenticated-routes)
    - [Create User](#create-user)
  - [Postman Setup instructions for Authenticated Routes](#postman-setup-instructions-for-authenticated-routes)
    - [Get Token](#get-token)
    - [Authenticated routes](#authenticated-routes)
      - [Get User Details](#get-user-details)
      - [Manage Recipies](#manage-recipies)
        - [Tags](#tags)
        - [Ingredients](#ingredients)
        - [Recipies](#recipies)
        - [Recipe<id>](#recipeid)
        - [Recipe<id>upload-image](#recipeidupload-image)
- [URL Routes](#url-routes)
  - [Manage users](#manage-users)
  - [Manage Recipies](#manage-recipies-1)
- [Finishing up](#finishing-up)
- [Testing](#testing)
- [Table of Contents](#table-of-contents)
- [Project: Recipe API](#project-recipe-api)
  - [Technologies](#technologies)
  - [End goal](#end-goal)
- [Introduction](#introduction-1)
  - [Technologies](#technologies-1)
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
- [CI/CD Test Automation](#cicd-test-automation)
  - [Option 1: Travis-CI](#option-1-travis-ci)
  - [Setting up Travis-CI](#setting-up-travis-ci)
  - [Create Travis-CI Configuration File](#create-travis-ci-configuration-file)
  - [Option 2: GitHub Actions](#option-2-github-actions)
- [Test Driven Development (TDD)](#test-driven-development-tdd-1)
  - [Unit Testing](#unit-testing)
  - [Creating a Test using Test Driven Development](#creating-a-test-using-test-driven-development)
  - [Adding Flake command to test](#adding-flake-command-to-test)
    - [What is the benefit of using TDD?](#what-is-the-benefit-of-using-tdd)
- [Building the Django Application](#building-the-django-application)
  - [Adding Tests for Custom User Model](#adding-tests-for-custom-user-model)
  - [Adding Tests for Normalized Email Feature](#adding-tests-for-normalized-email-feature)
  - [Adding Tests for Validation for email field](#adding-tests-for-validation-for-email-field)
- [Add suppport for creating superusers](#add-suppport-for-creating-superusers)
    - [Add flake8](#add-flake8)
    - [Commit to GitHub for Triggering Tests](#commit-to-github-for-triggering-tests)
- [Setup Django Admin](#setup-django-admin)
  - [As with TDD -> Start by building the tests](#as-with-tdd---start-by-building-the-tests)
  - [Final Change for the Custom Admin user model to work](#final-change-for-the-custom-admin-user-model-to-work)
  - [Django Customization of the Admin complete](#django-customization-of-the-admin-complete)
    - [Commit to GitHub for Triggering Tests](#commit-to-github-for-triggering-tests-1)
- [Setting up Database](#setting-up-database)
  - [Configure Database in Django](#configure-database-in-django)
- [Mocking with unit tests](#mocking-with-unit-tests)
- [Add tests for wait_for_db command](#add-tests-for-wait_for_db-command)
  - [Add wait_for_db command](#add-wait_for_db-command)
- [View in Browser](#view-in-browser)
  - [Create superuser](#create-superuser)
- [Creating user management endpoints](#creating-user-management-endpoints)
- [Serializers & Creating user API](#serializers--creating-user-api)
  - [Run Unit Tests](#run-unit-tests)

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

# Project: Recipe API

Virtual Recipe Box that you can use to organise your favourite recipes by:

- Title
- Ingredients
- Cooking Time
- Tags
- Images

## Technologies

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

Main Features of an API:

- User Authentication
- Creating Objects
- Listing/Filtering
- Uploading Images

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
    - `docker-compose run app sh -c "django-admin.py startproject app ."`
    - or alternatively, run `docker-compose run app django-admin.py startproject app .`

# CI/CD Test Automation

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

- Access Token: `<access_token>`

---

To use the access token from your Docker CLI client:

- Run docker login -u `<username>`
- At the password prompt, enter the `<personal access token>`.

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

- Create the following new directories within the root directory of the project and add a `build.yml` file: `.github/workflows/build.yml` with the following contents:

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

1. Push the changes, and you should see the GitHub Actions job running under Actions on the repo page.

# Test Driven Development (TDD)

## Unit Testing

- Writing a simple unit test.

Create a file `calc.py`

```py
def add(x, y):
    """Add two numbers together"""
    return x + y

```

To create a Unit test for the function

- Create new file called `tests.py`

The Django Unit Test framework looks for any file that begin with tests and uses them as the tests when you run the Django run unit tests command.

- Import the TestCase from django.tests. This is a class that comes with Django which has helper functions that help test Django code.
- Import the function you are going to test and inherit from TestCase
- A test usually comprises of two stages
  - Setup Stage: set function up to be tested
  - Assertion Stage: test the output and confirm that the output is equals to the expected outcome.

`calc.py`

```py
def add(x, y):
    """Add two numbers together"""
    return x + y

```

`tests.py`

```py
from django.test import TestCase

from app.calc import add

class CalcTests(TestCase):
    def test_add_numbers(self):
        """Test that two numbers are added together"""
        self.assertEqual(add(3, 8), 11)

    def test_add_strings(self):
        """Test that two strings cannot be added together"""
        self.assertEqual(add('3', '8'), '38')


```

Run the following command which will run the docker container and run the test.

- `docker-compose run app sh -c "python manage.py test"`

```
----------------------------------------------------------------------
Ran 2 tests in 0.002s

OK
Destroying test database for alias 'default'...
```

## Creating a Test using Test Driven Development

When you write the test before you write the code.

- Add a new feature to the `calc.py` module to subtract two numbers, but this time by using Test Driven Development.

`tests.py`

```py
    def test_subtract_numbers(self):
        """Test that values are subtracted and returned"""
        self.assertEqual(subtract(5, 11), 6)
```

Note that the test will fail:

```
Ran 1 test in 0.000s

FAILED (errors=1)
Destroying test database for alias 'default'...
ERROR: 1
```

Now add the function in `calc.py`

```py
def subtract(x, y):
    """Subtract two numbers"""
    return x - y
```

Now note, that the test will run again and fail as the function was incorrect! 11-5=7

```
Ran 3 tests in 0.008s

FAILED (failures=1)
Destroying test database for alias 'default'...
ERROR: 1
```

Modify the code
`tests.py`

```py
    def test_subtract_numbers(self):
        """Test that values are subtracted and returned"""
        self.assertEqual(subtract(11, 5), 6)
```

`calc.py` Note that the ordering of x - y is important, as if reversed (y - x) it will fail likewise if subtracting negative number

```py
def subtract(x, y):
    """Subtract two numbers"""
    return x - y
```

Pass

```
Ran 3 tests in 0.001s

OK
Destroying test database for alias 'default'...
```

## Adding Flake command to test

- Build the image as flake was not installed since the last build.
  - Type `docker-compose build`

Run the following to also run lint test on code:
`docker-compose run app sh -c "python manage.py tes && flake8"`

### What is the benefit of using TDD?

- The main benefit is that you know your tests work. There's often cases where your write a unit test and you think it's testing something but really it's not testing something. For example maybe you forgot to add the test string to the beginning of the function name and therefore the test is just never getting picked up by the test runner and therefore it seems like everything is working fine but really your test is just not running.
- So it helps eliminate those issues from your code also it helps improve the way you think about your code because before you write the code you're thinking "well I need to write code that I can test" and in order to do that you have to write basically high quality code.
- Usually code that's easy to test is easy to maintain and it's better quality than code that's just kind of being written without thinking about the tests in advance.

# Building the Django Application

> Configuring the Django User Model

First, create the core app which will hold all of the central code that is important to the rest of the sub apps that you create in your system.

- Create anything that is shared between one or more apps such as:
  - Database
  - Migrations

First, delete the `calc.py` and `tests.py` code from the projects.

1. Create the app from the terminal and use tha Django manage command
   1. `docker-compose run app sh -c "python manage.py startapp core"`

This runs the `manage.py` helper script and pass in the commands startapp core.
This creates a new app in the project called `core`.

```
project
├── .github
│   └── workflows
│       └── build.yml
├── app
│   ├── app
|   │   └── ...
│   ├── __pycache__
│   ├── __init__.py
│   ├── .flake8
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── core
│   ├── migrations
|   │   └── ...
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── manage.py
├── .gitignore
├── .flake8
├── manage.py
├── .gitignore
├── docker-compose.yml
├── Dockerfile
└── requirements.txt
```

Next, clean up the files from the `core` app that you're not going to be using:

- `app/core/tests.py` (will be adding the tests to a folder called tests later)
- `app/core/views.py` (not going to need the views in the core app, won't be serving anything will simply holding database models.)

You can't have both tests or there will be an erroe which is why these are deleted, but you could use either.

Now:

- Create a new Directory called `tests` inside `app/core/`
  - Create new File called `__init__.py` (this is where tests will be stored)
  - Doing this means it easily enables you to scale up your tests easily.

## Adding Tests for Custom User Model

Working with Test Driven Development, you write tests first and then implement the model afterwards.

- Write tests
- Firstly, install the app by:
  - adding ` 'core',` to the `INSTALLED_APPS` within `settings.py`
- Create new file: `test_models.py` within `app/code/tests`

Going to test the helper function for the model can create a new user. Use the create user function to create a user, and then verify that the user has been created as expected.

- Import the Get user model helper function that comes from Django. You can import the user model directly from the models, but this is not recommended with Django as at some point in the project you may want to change what your user model is and if everything is using the get user model function, than that's really easy to to as you can change it in the settings instead of having to change all the referencing to the user model.
- Pass in a email address and password and verify if the user has been created and if the email address is correct and the password is correct.
- This is calling the `create user function` of the `user manager` for the `user model` that you will create in a future step.

`test_models.py`

```py
from django.test import TestCase # Import the TestCase class
from django.contrib.org import get_user_model # Import the get_user_model function

class ModelTests(TestCase): # Create a test class that inherits from TestCase
    def test_create_user_with_email_successful(self): # Create a test method
        """Test creating a new user with an email is successful"""
        email = 'test@email.com'
        password = 'Testpass123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        ) # Create a new user with the email and password

        self.assertEqual(user.email, email) # Assert that the email is equal to the email we created
        self.assertTrue(user.check_password(password)) # Assert that the password is equal to the password we created
```

Run unit tests to test that: **the test fails** as we have not created the feature yet.

Now test is failing, you can make it pass by creating the custom user model.

- Create User Model in `models.py` in the core app.
- Update the `settings.py` file to set the custom auth user model.

`app/core/models.py`

```py
from django.db import models
# import the abstract base user, base user manager, permissions mixin -> to extend the django user model
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin
)
# Import the manager class -> provides the helper functions for creating a user or superuser
class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        # extra fields take any extra fields that are passed in and take into extra fields
        """Creates and saves a new user"""
        user = self.model(email, **extra_fields)
        user.set_password(password) # set the password (encrypted) - important
        user.save(using=self._db) # save the user to the database, supporting multiple databases

        return user

# Create a custom user model
class User(AbstractBaseUser, PermissionsMixin):
    """Custom user model that supports using email instead of username"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager() # Create a custom manager for the user model

    USERNAME_FIELD = 'email' # set the username field to the email field
```

`app/app/settings.py`

```py
AUTH_USER_MODEL = 'core.User' # set the custom user model to the core user model
```

- Make migrations
  - `docker-compose run app sh -c "python manage.py makemigrations core"`

This runs database migrations which create a new migrations file which is the instructions for Django to create the real model in the real Database.

- Run test
  - `docker-compose run app sh -c "python manage.py test"`

## Adding Tests for Normalized Email Feature

Add a feature to the function to normalize the email address that the users sign up with, not a required step, but is recommended because the second part of the domain name for email addresses is case-insensitive. That means the case of the last part like @gmail.com is not case sensitive.

- Don't want that to be case sensitive when the users log into the system, so will make that part all lowercase every time a new user registers.

`test_models.py`

```py
    def test_new_user_email_normalized(self):
        """Test the email for a new user is normalized"""
        email = 'test@GMAIL.com',
        user = get_user_model().objects.create_user(email, 'test123')

        self.assertEqual(user.email, email.lower())
        # Make string lowercase
```

- Run test
- `docker-compose run app sh -c "python manage.py test"`
  - Fail -> expected
    - Correct it: `test@gmail.com`
    - Fail -> expected
      - Implement in `Models.py`
        - Wrap the email in the Normilize email function

`models.py`

```py
# from
user = self.model(email=email, **extra_fields)
#to
user = self.model(email=self.normalize_email(email), **extra_fields)
```

`models.py`

```
    def test_new_user_email_normalized(self):
        """Test the email for a new user is normalized"""
        email = 'test@GMAIL.com'
        user = get_user_model().objects.create_user(email, 'test123')

        self.assertEqual(user.email, email.lower())
        # Make string lowercase
```

Run test

- `docker-compose run app sh -c "python manage.py test"`
  - Pass

## Adding Tests for Validation for email field

When the create user function is called to ensure en email field is actually being provided. Want to make sure when the create user function is called, and we don't pass an email address (blank string, none value) raise a value error.

`test_models.py`

```py
    def test_new_user_invalid_email(self):
        """Test creating user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')
```

Run tests

- `docker-compose run app sh -c "python manage.py test"`
  - Fail -> expected - Implement this feature in the models:

`models.py`

```py
        if not email:
            raise ValueError('Users must have an email address')
```

Run tests

- `docker-compose run app sh -c "python manage.py test"`
  - Pass

# Add suppport for creating superusers

Just one more function to add to user manager, create superuser function. This function is used by the Django CLI when creating new users via the command line.

- Want to make sure it is included in the custom user model so that we can take advantage of the Django management command for using a super user.
- The test is going to be to test that a super user is created when we call create super user and that it is assigned the is staff and is super user settings.

Add test `test_models.py`

```py
    def test_create_new_superuser(self):
        """Test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            'test@gmail.com',
            'test123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
        # Assert that the user is a superuser and a staff member
```

- Run test
- `docker-compose run app sh -c "python manage.py test"`
  - Fail -> expected
    - Need to implement this feature

`models.py`

```py
class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        # extra fields take any extra fields that are passed in and take into extra fields
        """Creates and saves a new user"""
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password) # set the password (encrypted) - important
        user.save(using=self._db) # save the user to the database, supporting multiple databases

        return user

    def create_superuser(self, email, password):
        """Creates and saves a new superuser"""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user
```

Run tests

- `docker-compose run app sh -c "python manage.py test"`
  - Pass

### Add flake8

- This will run linting on the project and make sure there is no linting errors.

Run tests

- ` docker-compose run app sh -c "python manage.py test && flake8"`
  - Fail: doesn't like because the `admin.py` file is not populated (unused import)
    - Comment out the code (import in the admin file)
      - Pass

### Commit to GitHub for Triggering Tests

- `git add .`
- `git commit -a
  - "Added custom user model"
    - :wq
    - `git push origin`
    - GitHub Actions will be Triggered and run tests emailing if there is any failures

# Setup Django Admin

To manage the custom user model. Giving a nice interface to login and see which users have been created, create users or make changes to existing users.

## As with TDD -> Start by building the tests

- Create new Unit Test
  - `tests_admin.py` in `app/app/core/tests` directory

A setUp function is a function that is ran before every test that you run. For example if they are setup tasks that need to be run for every test in the test case class.

- Test Client
- New user
- Make sure user is logged into client
- Create a regular user that is not authenticated or that can be used to list on admin page

Test that the users are listed in the Django admin as we need to slightly customize the Django admin to work with our custom user model as the default user model expects a username and as such the default django admin for the user model also expects a username which we don't have username, we just have email address so a few small changes are required to the `admin.py` file to make sure it supports the custom user model.

- Preform HTTP Get on the URL (from django docs)
- Run assertions
  - Checks for HTTP:200 and looks into the object and check for content

`tests_admin.py`

```py
    def test_users_listed(self):
        """Test that users are listed on user page"""
        url = reverse('admin:core_user_changelist') # Generate url for user list page
        res = self.client.get(url) # Get response from url

        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)
```

Run tests

- ` docker-compose run app sh -c "python manage.py test && flake8"`
  - Fail: as we have not created admin yet.

Customize Django admin to list custom user model:
`admin.py`

```py
from unittest.mock import Base
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from core import models

class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display = ['email', 'name']


admin.site.register(models.User, UserAdmin)
```

Run tests

- ` docker-compose run app sh -c "python manage.py test && flake8"`
  - Pass

Test that the change page renders correctly. It's not required to test dependencies of your project so don't need to test features that are specific to the frameworks or externam modules that you're using in you're project, Django is pretty robustly tested, we just need to make sure that the code you write is tested correctly.

`admin.py`

```py
    def test_user_change_page(self):
        """Test that the user edit page works"""
        url = reverse('admin:core_user_change', args=[self.user.id])
        # /admin/core/user/1
        res = self.client.get(url) # HTTP:Get  on url -> response from url

        self.assertEqual(res.status_code, 200) # Check if response is 200
```

Run tests

- ` docker-compose run app sh -c "python manage.py test && flake8"`
  - Fail -> expected
    - Unknown fields
      - Need to customize the user admin field sets to support our custom model as opposed to the default model it is expecting

Add fieldsets class variable
`admin.py`

```py
from unittest.mock import Base
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as _ # Convert strings to human readable

from core import models

class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display = ['email', 'name']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal Info'), {'fields': ('name',)}),
        (
            _('Permissions'),
            {
                'fields': (
                    'is_active',
                    'is_staff',
                    'is_superuser',
                )
            }
        ),
        (_('Important dates'), {'fields': ('last_login',)}),
    )


admin.site.register(models.User, UserAdmin)
```

Run tests

- ` docker-compose run app sh -c "python manage.py test && flake8"`
  - Pass

## Final Change for the Custom Admin user model to work

- Add page

Page for adding new users in the Django admin.

`tests_admin.py`

```py
    def test_create_user_page(self):
        """Test that the create user page works"""
        url = reverse('admin:core_user_add')
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200) # Check if response is 200
```

Run tests

- ` docker-compose run app sh -c "python manage.py test && flake8"`
  - Fail -> expected
    - Username is not specified for user
      - Go to admin.py and correct

`admin.py`
Add the add field sets class variable, from Django admin documentation

```py
from unittest.mock import Base
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as _ # Convert strings to human readable

from core import models

class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display = ['email', 'name']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal Info'), {'fields': ('name',)}),
        (
            _('Permissions'),
            {
                'fields': (
                    'is_active',
                    'is_staff',
                    'is_superuser',
                )
            }
        ),
        (_('Important dates'), {'fields': ('last_login',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')
        }),
    )


admin.site.register(models.User, UserAdmin)
```

Run tests

- ` docker-compose run app sh -c "python manage.py test && flake8"`
  - Pass

## Django Customization of the Admin complete

### Commit to GitHub for Triggering Tests

- `git add .`
- `git commit -a
  - "Added custom user model"
    - :wq
    - `git push origin`
    - GitHub Actions will be Triggered and run tests emailing if there is any failures

# Setting up Database

Setting up PostgreSQL as the Database instead of the default sqllite database.

- Start by making changes to docker compose file
  - Create a new service called `db`
    - Add postgres lightweight image
    - Set up env variables
    - Modify app service to set some environment variablesand depend on the db service
    - Configure dockerfile to support the postgres client

`docker-compose.yml`

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
    environment:
      - DB_HOST=app
      - DB_NAME=app
      - DB_USER=postgres
      - DB_PASS=postgres
  db:
    image: postgres:10-alpine
    environment:
      - POSTGRES_DB=app
      - POSTGRES_USER=postgres
      - POSTGRES_PASSWORD=postgres

```

`requirements.txt`

```
Django>=2.1.3,<2.2.0
djangorestframework>=3.9.0,<3.10.0
psycopg2>=2.7.5,<2.8.0
flake8>=3.6.0,<3.7.0
```

`Dockerfile`

```
FROM python:3.7-alpine
LABEL maintainer="Michael O'Grady"

ENV PYTHONUNBUFFERED 1

# Install dependencies
COPY ./requirements.txt /requirements.txt
RUN apk add --update --no-cache postgresql-client
RUN apk add --update --no-cache --virtual .tmp-build-deps \
    gcc libc-dev linux-headers postgresql-dev

RUN pip install -r /requirements.txt
RUN apk del . tmp-build-deps

RUN mkdir /app
WORKDIR /app
COPY ./app /app


RUN adduser -D user
USER user

```

- Make sure image will build successfully
  - `docker-compose build`

## Configure Database in Django

- Configure the Django project to use postgresql
- `settings.py`

```py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': os.environ.get('DB_HOST'),
        'NAME': os.environ.get('DB_NAME'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASS'),
    }
}
```

# Mocking with unit tests

- Mocking is when you override or change the behavior of the dependencies of the code that you're testing. We use mocking to avoid any unintended side effects and also to isolate the specific piece of code that we want to test.

For example imagine you're testing a function that sends an email. There are two good reasons that you wouldn't want to actually send an email every time you run your tests.

- The first reason is that you should never write tests that depend on external services. This is because you can't guarantee that these services will be uvailable at the point that you run the test and this would make the test unpredictable and unreliable.
- The second reason is you don't want to be sending spam emails each time you run your test suite even if you're using a fake address those emails would still be backing up on a server somewhere. When you write your test you can use mocking to avoid sending an actual email. You can override the function in the dependency that sends the email and replace it with a mock object. Using this mock object we can avoid sending an actual email and instead just check that the function was called with the correct parameters.

# Add tests for wait_for_db command

The management command is going to be a helper command that allows us to wait for the database to be available before continuing and running other commands.
We're going to use this command in our docker compose file when starting our django app. The reason that we need this command is because I find that sometimes when using Postgres with docker compose in a django app sometimes the django app fails to start because of a database error. It turns out that this is because once the Postgres service has started there are a few extra setup tasks that need to be done on the Postgres before it is ready to accept connections. So what this means is our django app will try and connect to our database before the database is ready and therefore it will fail with an exception and you will need to restart the app. To improve the reliability of our project we're going to add this helper command that we can put in front of all of the commands we've run in docker compose and that will ensure that the database is up and ready to accept connections before we try and access the database. This will make our application a lot more reliable when running it locally as a development server and also if we ever deploy it as a production system.

`test_commands.py`

```py
from unittest.mock import patch

from django.core.management import call_command
from django.db.utils import OperationalError
from django.test import TestCase


class CommandTests(TestCase):

    def test_wait_for_db_ready(self):
        """Test waiting for db when db is available"""
        with patch('django.db.utils.ConnectionHandler.__getitem__') as gi:
            gi.return_value = True
            call_command('wait_for_db')
            self.assertEqual(gi.call_count, 1)

    @patch('time.sleep', return_value=True)
    def test_wait_for_db(self, ts):
        """Test waiting for db"""
        with patch('django.db.utils.ConnectionHandler.__getitem__') as gi:
            gi.side_effect = [OperationalError] * 5 + [True]
            call_command('wait_for_db')
            self.assertEqual(gi.call_count, 6)

```

- All we're going to check is that this get item was called once. So the way that you check that using this mock object is you type self.assertEqual gi.call_count, 1
  So this return value in this call count these are all options that you can set on a mock object.

- Okay so now we've added the first test we can add the second test and in this test we're going to check that the wait for db command will try the database five times and then on the sixth time it'll be successful and it will continue.

## Add wait_for_db command

So this is the django convention and it's recommended on the django website to put all of your commands in a directory called management and then forward slash commands so we're going to start by creating a folder called management and make sure that this is in the actual core app folder.

`wait_for_db.py`

```py
import time

from django.db import connections
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Django command to pause execution until database is available"""

    def handle(self, *args, **options):
        self.stdout.write('Waiting for database...')
        db_conn = None
        while not db_conn:
            try:
                db_conn = connections['default']
            except OperationalError:
                self.stdout.write('Database unavailable, waiting 1 second...')
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('Database available!')) #
```

Add wait_for_db to command in docker-compose

# View in Browser

- docker-compose build
- docker-compose up -> starts server

## Create superuser

`docker-compose run app sh -c "python manage.py createsuperuser"`

- http://127.0.0.1:8000/admin/
- email: `<email>`
- password: `<password>`

# Creating user management endpoints

In this section we're going to create our manage user endpoints.
These endpoints are going to allow us to create users, to update users, to change a user's password and to create user authentication tokens which can be used to authenticate requests to the other APIs in our project.

- Create new app `users`

`docker-compose run --rm app sh -c "python manage.py startapp user"`
removes the container after it's run the command

- Cleanup, remove:

  - Migrations
  - admin.py
  - models.py
  - tests.py

- Create new file tests
- Add to settings, installed apps

```py
    'rest_framework',
    'rest_framework.authtoken',
    'core',
    'user',
```

Okay so the first API that we're going to create in our users project is the create users API so we're going to start by adding some unit tests to test creating users and different scenarios when we give different post requests. Let's head over to our source code and open up our tests here and create a new file called test_user_api.py
`test_user_api.py`

```py
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status


CREATE_USER_URL = reverse('user:create')
TOKEN_URL = reverse('user:token')
ME_URL = reverse('user:me')


def create_user(**params):
    return get_user_model().objects.create_user(**params)


class PublicUserApiTests(TestCase):
    """Test the users API (public)"""

    def setUp(self):
        self.client = APIClient()

    def test_create_valid_user_success(self):
        """Test creating user with valid payload is successful"""
        payload = {
            'email': 'test@londonappdev.com',
            'password': 'testpass',
            'name': 'Test name'
        }
        res = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        user = get_user_model().objects.get(**res.data)
        self.assertTrue(user.check_password(payload['password']))
        self.assertNotIn('password', res.data)

    def test_user_exists(self):
        """Test creatinga  user that already exists fails"""
        payload = {
            'email': 'test@londonappdev.com',
            'password': 'testpass',
            'name': 'Test',
        }
        create_user(**payload)

        res = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_password_too_short(self):
        """Test that the password must be more than 5 characters"""
        payload = {
            'email': 'test@londonappdev.com',
            'password': 'pw',
            'name': 'Test',
        }
        res = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        user_exists = get_user_model().objects.filter(
            email=payload['email']
        ).exists()
        self.assertFalse(user_exists)

    def test_create_token_for_user(self):
        """Test that a token is created for the user"""
        payload = {'email': 'test@londonappdev.com', 'password': 'testpass'}
        create_user(**payload)
        res = self.client.post(TOKEN_URL, payload)

        self.assertIn('token', res.data)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_create_token_invalid_credentials(self):
        """Test that token is not created if invalid credentials are given"""
        create_user(email='test@londonappdev.com', password="testpass")
        payload = {'email': 'test@londonappdev.com', 'password': 'wrong'}
        res = self.client.post(TOKEN_URL, payload)

        self.assertNotIn('token', res.data)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_token_no_user(self):
        """Test that token is not created if user doesn't exist"""
        payload = {'email': 'test@londonappdev.com', 'password': 'testpass'}
        res = self.client.post(TOKEN_URL, payload)

        self.assertNotIn('token', res.data)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_token_missing_field(self):
        """Test that email and password are required"""
        res = self.client.post(TOKEN_URL, {'email': 'one', 'password': ''})
        self.assertNotIn('token', res.data)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_retrieve_user_unauthorized(self):
        """Test that authentication is required for users"""
        res = self.client.get(ME_URL)

        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


class PrivateUserApiTests(TestCase):
    """Test API requests that require authentication"""

    def setUp(self):
        self.user = create_user(
            email='test@londonappdev.com',
            password='testpass',
            name='name'
        )
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_retrieve_profile_success(self):
        """Test retrieving profile for logged in used"""
        res = self.client.get(ME_URL)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, {
            'name': self.user.name,
            'email': self.user.email
        })

    def test_post_me_not_allowed(self):
        """Test that POST is not allowed on the me url"""
        res = self.client.post(ME_URL, {})

        self.assertEqual(res.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_update_user_profile(self):
        """Test updating the user profile for authenticated user"""
        payload = {'name': 'new name', 'password': 'newpassword123'}

        res = self.client.patch(ME_URL, payload)

        self.user.refresh_from_db()
        self.assertEqual(self.user.name, payload['name'])
        self.assertTrue(self.user.check_password(payload['password']))
        self.assertEqual(res.status_code, status.HTTP_200_OK)

```

# Serializers & Creating user API

- Create urls and Settings
- Authentication and tests for Create Token API

Django rest framework has a built-in serializer that we can do this with that we just need to specify the fields that we want from our module and it does the database conversion for us. And even helps with the creating and retrieving from the database.

```py
from django.contrib.auth import get_user_model, authenticate
from django.utils.translation import ugettext_lazy as _

from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    """Serializer for the users object"""

    class Meta:
        model = get_user_model()
        fields = ('email', 'password', 'name')
        extra_kwargs = {'password': {'write_only': True, 'min_length': 5}}

    def create(self, validated_data):
        """Create a new user with encrypted password and return it"""
        return get_user_model().objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        """Update a user, setting the password correctly and return it"""
        password = validated_data.pop('password', None)
        user = super().update(instance, validated_data)

        if password:
            user.set_password(password)
            user.save()

        return user


class AuthTokenSerializer(serializers.Serializer):
    """Serializer for the user authentication object"""
    email = serializers.CharField()
    password = serializers.CharField(
        style={'input_type': 'password'},
        trim_whitespace=False
    )

    def validate(self, attrs):
        """Validate and authenticate the user"""
        email = attrs.get('email')
        password = attrs.get('password')

        user = authenticate(
            request=self.context.get('request'),
            username=email,
            password=password
        )
        if not user:
            msg = _('Unable to authenticate with provided credentials')
            raise serializers.ValidationError(msg, code='authentication')

        attrs['user'] = user
        return attrs

```

## Run Unit Tests

- `docker-compose run --rm app sh -c "python manage.py test && flake8"`
- Create Token
- `http://127.0.0.1:8000/api/user/token/`

---
