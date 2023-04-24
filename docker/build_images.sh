#!/bin/bash

docker buildx build --progress plain -t cfs-base-armv7l cfs-base-armv7l
docker buildx build --progress plain -t cfs-builder-armv7l cfs-builder-armv7l
docker buildx build --progress plain -t compiler-builder-armv7l compiler-builder-armv7l
docker buildx build --progress plain -t pkg-builder-armv7l pkg-builder-armv7l

