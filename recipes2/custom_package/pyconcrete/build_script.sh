#!/bin/bash

pyversion=("3.8" "3.9" "3.10" "3.11")

export CONDA_BUILD=1
export PYCONCRETE_PASSPHRASE=tlq32

source ${CONDA_PREFIX}/etc/profile.d/conda.sh

pushd workspace

# curl -L -o pyconcrete.tgz 'https://github.com/Falldog/pyconcrete/archive/refs/heads/master.tar.gz'
# tar zxvf pyconcrete.tgz

for py in "${pyversion[@]}"; do
    echo ${py}
    conda create -y -n build_pyconcrete python=${py} c-compiler patchelf

    conda activate build_pyconcrete

    # pushd pyconcrete-master
    pushd pyconcrete

    python setup.py bdist_wheel

    mv -v dist/*.whl ../

    popd

    conda deactivate

    conda env remove -y -n build_pyconcrete

done

# rm -rf pyconcrete-master pyconcrete.tgz

popd

