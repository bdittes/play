#!/bin/bash

# For PyMesh
# sudo apt-get install libeigen3-dev libgmp-dev libgmpxx4ldbl libmpfr-dev libboost-dev libboost-thread-dev libtbb-dev
# export CMAKE_BUILD_TYPE=Release
# 

. ~/miniconda3/etc/profile.d/conda.sh

CMD=$1
shift

if [ $CMD = "install" ]; then
    #python${P3} -m venv venv
    #. ./venv/bin/activate
    conda create --prefix conda
    conda install python=3.10 numpy=1.24 python-dotenv absl-py elasticsearch-dsl pip setuptools yapf ipython pytest libffi=3.3 conda-forge::libcblas
    conda activate ./conda
    #pip install --upgrade pip || echo "Please first sudo apt install python${P3}-pip"
    #pip install --upgrade setuptools
    pip install --upgrade -r requirements.txt
    # To install PyMesh: https://pymesh.readthedocs.io/en/latest/installation.html
    # . py && cd ../PyMesh && ./setup.py install && cd -
    # For pymeshlab:
    # sudo install --yes libgl1-mesa-dev
    exit 0
fi

if [ ! -f "conda/bin/python" ]; then
    ./py install
fi

conda activate ./conda || exit -1

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
elif [ $CMD = "alti" ]; then
    python python/alti.py $@
else
    "$CMD" "$@"
fi
