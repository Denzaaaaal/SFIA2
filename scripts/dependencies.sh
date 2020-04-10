#!/bin/bash

# installing ansible
sudo apt update -y -qq > /dev/null
sudo apt install software-properties-common -y -qq > /dev/null
sudo apt-add-repository --yes --update ppa:ansible/ansible -y -qq > /dev/null
sudo apt install ansible -y -qq > /dev/null

