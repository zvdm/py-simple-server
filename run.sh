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
  echo "[ Django ] Running collect static..."
  ./manage.py collectstatic --no-input
  echo "[ Django ] End"
}

run_docker() {
  echo "[ Docker ] Running docker compose command..."
  if [ -n "$flag" ] && [ "$flag" == "-d" ]; then
    COMPOSE_IGNORE_ORPHANS=True docker-compose -p acl-backend --profile servers up -d
    echo "[ Docker ] End"
    exit
  else
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
setup_env
run_docker
run_django_commands
if [ -n "$flag" ] && [ "$flag" == "-t" ]; then
  ./manage.py makemigrations --check --dry-run
  ./manage.py test --parallel
else
  ./manage.py runserver
fi
