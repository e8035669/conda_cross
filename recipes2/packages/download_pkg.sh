#!/bin/bash

pkg_name=$1
feed_stock=${pkg_name}-feedstock

if [ -d "${feed_stock}" ]; then
    echo "directory exist"
    exit 1
fi

git clone git@github.com:e8035669acarmv7/${feed_stock}.git

if [ $? != 0 ]; then
    git clone https://github.com/conda-forge/${feed_stock}.git
    pushd ${feed_stock}
    gh repo fork --org e8035669acarmv7
    popd
else
    pushd ${feed_stock}
    git remote add upstream https://github.com/conda-forge/${feed_stock}.git
    popd
    echo "good"
fi

git submodule add -f -b main git@github.com:e8035669acarmv7/${feed_stock}.git

