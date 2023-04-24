#!/bin/bash

source /opt/cfs/bin/activate

pip install git+https://github.com/Anaconda-Server/anaconda-client

anaconda login

conda config --set anaconda_upload true
conda config --append channels e8035669


