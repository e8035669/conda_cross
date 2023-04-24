#!/bin/bash

pkg_dir=$(basename $1)

pushd ${pkg_dir}/recipe/
conda-build .
popd

