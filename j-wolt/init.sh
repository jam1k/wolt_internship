#!/bin/bash

# Initialising the environment
pip3 install virtualenv
virtualenv env
source env/bin/activate
pip3 install flask
pip3 install python-dateutil
pip3 install pytest
pip3 install cerberus
