!#/bin/bash

python3 -m venv --without-pip myvenv
source myvenv/bin/activate
curl https://bootstrap.pypa.io/get-pip.py | python
deactivate
source myvenv/bin/activate