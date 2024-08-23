#!/bin/bash

# For PyMesh
# conda create -n py310 python=3.10
conda activate py310

P3=
if [[ -f $(which python3) ]]; then
    P3=3
else
    echo "WARNING: Could not find python 3 in path. You probable want to 'sudo apt install python3.7-venv'."
fi

CMD=$1
shift

if [ $CMD = "install" ]; then
    python${P3} -m venv venv
    . ./venv/bin/activate
    pip install --upgrade pip || echo "Please first sudo apt install python${P3}-pip"
    pip install --upgrade setuptools
    pip install --upgrade -r requirements.txt
    # To install PyMesh: https://pymesh.readthedocs.io/en/latest/installation.html
    # ./py install
    # ./py pip install -r ../PyMesh/python/requirements.txt
    # cd ../PyMesh
    # python ./setup.py install
    exit 0
fi

if [ ! -f "venv/bin/activate" ]; then
    ./py install
fi

. ./venv/bin/activate || exit -1

if [ $CMD = "server" ]; then
    flask run --host=0.0.0.0 --port=5000 "$@"
elif [ $CMD = "local" ]; then
    python python/local.py "$@"
elif [ $CMD = "lint" ]; then
    mypy python/*.py python/tests/*.py &&
        flake8 &&
        (yapf -d python/*.py python/tests/*.py >/dev/null || (echo 'Format not happy, do ./py format!' && exit -1))
elif [ $CMD = "format" ]; then
    yapf -i python/*.py python/tests/*.py "$@"
elif [ $CMD = "test" ]; then
    ./py lint && python -m pytest -v -q python/ "$@"
else
    "$CMD" "$@"
fi
