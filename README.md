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
    - [Commit to GitProject](#commit-to-gitproject)

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

### Commit to GitProject

- `git add .`
- `git commit -a
  - "Added custom user model"
    - :wq
