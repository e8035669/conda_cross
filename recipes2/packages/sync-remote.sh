#!/bin/bash

set -e

function sync_remote() {

    need_update=()

    for i in */; do
        echo $i

        gitc="git -C ${i}"

        origin=$(${gitc} remote get-url origin)
        upstream=$(echo "${origin}" | sed 's/e8035669acarmv7/conda-forge/g' | sed 's/git@github.com:/https:\/\/github.com\//g')

        ret=0
        ${gitc} remote | grep upstream > /dev/null || ret=$?
        if [ "${ret}" -eq "0" ]; then
            cur_upstream=$(${gitc} remote get-url upstream)
            if [ "${cur_upstream}" != "${upstream}" ]; then
                ${gitc} remote remove upstream
                ${gitc} remote add -t main upstream "${upstream}"
            fi
        else
            ${gitc} remote add -t main upstream "${upstream}"
        fi


        ${gitc} fetch upstream main

        cur_remote_commit=$(${gitc} rev-parse upstream/main)
        merge_base=$(${gitc} merge-base main upstream/main)

        if [ "${cur_remote_commit}" != "${merge_base}" ]; then
            need_update+=("$i")
        fi

    done

    for i in "${need_update[@]}"; do
        echo "$i" need update
    done

    echo "Dump to need_update.txt"
    rm -rvf need_update.txt
    for i in "${need_update[@]}"; do
        echo "$i" >> need_update.txt
    done

}

function merge_from_upstream() {
    while read i; do
        echo ${i}

        gitc="git -C ${i}"

        ${gitc} checkout main
        ${gitc} merge upstream/main

        # exit 0
        echo ""

    done < ./need_update.txt
}

function git_push() {
    for i in */; do
        echo ${i}

        gitc="git -C ${i}"

        ${gitc} push -u origin main

        # exit 0
        echo ""

    done
}



if [ "$1" == "sync_remote" ]; then
    sync_remote
elif [ "$1" == "merge_from_upstream" ]; then
    merge_from_upstream
elif [ "$1" == "git_push" ]; then
    git_push
fi


