#!/bin/bash

pkg_name=$1
feed_stock=${pkg_name}-feedstock
dir_name=$2

if [[ -z "${dir_name}" ]] && [[ -d "${dir_name}" ]]; then
    echo "directory exist"
    exit 1
fi

git clone git@github.com:e8035669acarmv7/${feed_stock}.git "${dir_name}"

if [ $? != 0 ]; then
    git clone https://github.com/conda-forge/${feed_stock}.git "${dir_name}"
    pushd "${dir_name}"
    gh repo fork --org e8035669acarmv7
    popd
else
    pushd "${dir_name}"
    git remote add upstream https://github.com/conda-forge/${feed_stock}.git
    popd
    echo "good"
fi

git submodule add -f -b main git@github.com:e8035669acarmv7/${feed_stock}.git "${dir_name}"

