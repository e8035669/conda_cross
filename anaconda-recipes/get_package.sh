#!/bin/bash

pkg_name=$1
feed_stock=${pkg_name}-feedstock

git clone --depth 1 https://github.com/AnacondaRecipes/${feed_stock}.git

