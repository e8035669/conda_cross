#!/bin/bash

mkdir -p ${PREFIX}/${target_machine}-${ctng_vendor}-linux-gnueabihf/sysroot
pushd ${PREFIX}/${target_machine}-${ctng_vendor}-linux-gnueabihf/sysroot > /dev/null 2>&1
mkdir -p usr/include
cp -Rf "${SRC_DIR}"/binary-kernel-headers/include/* usr/include/
popd
