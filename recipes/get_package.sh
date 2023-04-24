#!/bin/bash

pkg_name=$1

rm -rf main.zip
wget "https://github.com/conda-forge/${pkg_name}-feedstock/archive/refs/heads/main.zip"
unzip main.zip
rm -rf main.zip

