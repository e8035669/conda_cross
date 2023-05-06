#!/bin/bash

for i in */; do
    # echo $i

    # ret=$(git -C "$i" status | grep "tree clean")
    # ret=$(git -C "$i" status | grep "乾淨")

    # if [ -z "$ret" ]; then
    #     echo $i not clean
    # fi

    remote=$(git -C "$i" remote get-url origin)
    branch=$(git -C "$i" branch --show-current)

    git submodule add -f -b "$branch" "$remote" "$i"

done

