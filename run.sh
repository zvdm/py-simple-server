#!/bin/bash

run_django_commands() {
  echo "[ Django ] Running Django commands..."
  if [ ! -d "../venv" ]; then
    echo "[ Django ] Creating a python virtual environment..."
    python3 -m venv ../venv
  fi
  echo "[ Django ] Activated the python virtual environment..."
  source ../venv/bin/activate
  echo "[ Django ] Installing requirements..."
  pip3 install --upgrade pip
  pip3 install -r requirements.txt
  echo "[ Django ] Running migrating..."
  ./manage.py migrate --noinput
  echo "[ Django ] End"
}

run_docker() {
  echo "[ Docker ] Running docker compose command..."
  if [ -n "$flag" ] && [ "$flag" == "-d" ]; then
    COMPOSE_IGNORE_ORPHANS=True docker-compose -p acl-backend --profile servers up -d
    docker cp nginx.conf acl-nginx:/etc/nginx/conf.d/default.conf
    docker restart acl-nginx
    echo "[ Docker ] End"
    exit
  else
    setup_env
    COMPOSE_IGNORE_ORPHANS=True docker-compose -p acl-backend up -d
    echo "[ Docker ] End"
  fi
}

setup_env() {
  echo "[ Bash ] Setting environments variables..."
  if [ -f ".env.example" ]; then
    cp .env.example .env
  else
    echo "[ Bash ] Error, file '.env.example' does not exist."
    exit
  fi
  echo "[ Bash ] End"
}

if [ $# -eq 1 ]; then
  flag=$1
fi
run_docker
run_django_commands
if [ -n "$flag" ] && [ "$flag" == "-t" ]; then
  ./manage.py makemigrations --check --dry-run
  ./manage.py test --parallel
else
  ./manage.py runserver
fi
