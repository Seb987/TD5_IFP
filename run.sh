#!/bin/bash

if [ ! -d "env" ]
then
	echo "Virtual environnement doesn't exist"
	python3 -m venv env
fi
echo "Virtual environnement created"
source env/bin/activate
pip install -r requirements.txt #pytest pyyaml

pip freeze > requirements.txt
python3 main.py
