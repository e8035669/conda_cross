#!/bin/bash

SOURCE=$(dirname ${BASH_SOURCE[0]})
# echo "${SOURCE}"
export $(cat ${SOURCE}/../../.env | xargs)
export UPLOAD_PACKAGES="True"
export IS_PR_BUILD="False"

