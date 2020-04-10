#!/bin/bash

cd ansible
ansible-playbook -i ./inventory.ini ./installation.yml
ansible-playbook -i ./inventory.ini ./node_assignment.yml
ansible-playbook -i ./inventory.ini ./deployment.yml