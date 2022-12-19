
[![Build Status](http://64.227.128.144:8080/buildStatus/icon?job=Flask-Poetry%2Fmaster)](http://64.227.128.144:8080/job/Flask-Poetry/job/master/)

<h1 align="center"> About </h1>

This project aims to implement a standard CI/CD pipeline for a Flask project whose dependencies are managed using Poetry. This repository is a major improvement on my <a href="https://github.com/NarayanAdithya/pythone2e" >last attempt</a> to create a CI/CD pipeline for a basic python application build using the Flask microframework. 

<h1 align="center"> Poetry </h1>

Poetry is a python dependecy manager which is very much analogous to npm for JS projects. With Poetry one can isolate all the dependencies in a `Poetry.lock` file which can then ensure that the versions are maintained while shifting via environments. Poetry also helps group dependencies into dev dependecies and main dependencies. It also provides you the advantage of defining scripts just like one would define in package.json. Poetry generates a `pyproject.toml` file which has become the standard for defining the package details and configuration of tools like flake8, bandit and PyTest.

<h1 align="center"> Stages in CI Pipeline and Associated Commands </h1>

1. Install Environment - `poetry install`
2. Run Linting - `poetry run flake8 .`
3. Vulnerability Check - `poetry run bandit -r . -c "pyproject.toml"`
4. Run Unit Test - `poetry run pytest .`
5. Bump Version - `poetry version patch`
6. Commit Version Update and Push Changes
7. Build Docker Image from Dockerfile
8. Docker Login
9. Push Image to DockerHub Repository


<h1 align="center"> Jenkins </h1>

A multibranch project has been setup with a Multibranch webhook trigger setup to build the latest release on a commit. The Jenkins has also been configured with Build Trigger Extension to prevent build on certain file changes like README.md etc. The Embeddable Status Plugin was used to create the badge shown on the top of the README.md file. Jenkins is making use of two custom defined libraries one for poetry and one for normal python build commands. These repo's can be found <a href="https://github.com/NarayanAdithya/python-jenkins-shared-library"> here </a> and <a href="https://github.com/NarayanAdithya/poetry-jenkins-library"> here </a>
