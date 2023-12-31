#!/bin/bash

if [ -d "env" ] 
then
    echo "Python virtual environment exists." 
else
    virtualenv env
fi

echo $PWD
source env/bin/activate
pip install -r app/requirements.txt

if [ -d "logs" ] 
then
    echo "Log folder exists." 
else
    mkdir logs
    touch logs/error.log logs/access.log
fi
sudo chmod -R 777 logs