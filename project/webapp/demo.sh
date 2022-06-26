#!/bin/bash

sudo apt update
sudo apt install python3.6
python -m pip install --upgrade pip
sudo apt-get install python3-numpy
sudo apt-get install python3-opencv
sudo apt-get install python3-django

cd /main
. getModel.sh
cd ..

echo "Запуск сервера"

python3 manage.py runserver 0.0.0.0:1337

