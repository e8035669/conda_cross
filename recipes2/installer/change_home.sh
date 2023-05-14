#!/bin/sh

if [ ! -d "${HOME}" ]; then

  if [ -z "${OLD_HOME}" ]; then
    export OLD_HOME="${HOME}"
  fi

  conda_dir="$(dirname $(dirname ${CONDA_EXE}))"
  new_home="${conda_dir}/home/${USER}"
  mkdir -p "${new_home}"
  export HOME="${new_home}"

  echo "HOME directory not writable. change to ${HOME}"

fi

