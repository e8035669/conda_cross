#!/bin/bash

for i in */; do
    # echo $i

    # ret=$(git -C "$i" status | grep "tree clean")

    # if [ -z "$ret" ]; then
    #     echo $i not clean
    # fi

    remote=$(git -C "$i" remote get-url origin)

    git submodule add "$remote" "$i"

done

