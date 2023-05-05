FROM ubuntu-cfs-builder-armv7l

RUN apt-get update && \
    apt-get install -y automake texinfo \
    wget make unzip git autoconf bison flex \
    help2man gettext file gawk libtool-bin && \
    rm -rf /var/lib/apt/lists/*

