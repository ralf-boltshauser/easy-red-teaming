#!/bin/bash

sudo apt install xdotool -y

echo "Enter the ip you want the reverse shells to connect to!"
read ip

sed -i 's/my_ip = ".*"/my_ip = "'$ip'"/g' easy-red-teaming.py

python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt

chmod +x easyredteaming.sh

ln -s $PWD/easyredteaming.sh /usr/local/bin/easyredteaming