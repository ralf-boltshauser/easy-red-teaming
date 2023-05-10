#!/bin/bash

sudo apt install xdotool -y

python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt

chmod +x easyredteaming.sh

ln -s $PWD/easyredteaming.sh /usr/local/bin/easyredteaming