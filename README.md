# A simple server
An example of a simple backend written in Django. All static are managed by the server. 

#### Stack:
- [Python](https://www.python.org/downloads/)
- [Docker](https://docs.docker.com/engine/install/)
- [Docker Compose](https://docs.docker.com/compose/install/)
- [PostgreSQL](https://www.postgresql.org/)

## Requirements
To run this project, install the following tools: 
- [Python 3.9](https://www.python.org/downloads/)
- [Docker](https://docs.docker.com/engine/install/) (to install docker use the official instruction on the [official site](https://docs.docker.com/docker-for-mac/install/))
- [Docker Compose](https://docs.docker.com/compose/install/) (can be installed via the command `pip3 install docker-compose`)

## Local Developing
All actions should be executed from the source directory of the project and only after installing all requirements.
The recommended way run the project in IDE. 
However, to run it in the terminal execute (to download requirements, up required services and run the server):
   ```bash
   ./run.sh
   ```
To run tests (should be run before pushing changes to the projects):
   ```bash
   ./run.sh -t
   ```

## Local Container
All actions should be executed from the source directory of the project and only after installing all requirements.
Just, up the service with the support services in the docker containers:
   ```bash
   ./run.sh -d
   ```

## The access to the service
After successfully running, the service and the support services will be available:
- the service on the address http://127.0.0.1:8000,
- the database (PostgreSQL) on the address http://127.0.0.1:5432.
