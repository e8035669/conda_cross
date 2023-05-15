FROM arm32v7/ubuntu:22.04

ENV LANG=C.UTF-8 LC_ALL=C.UTF-8

RUN apt-get update -q && \
    apt-get install -q -y --no-install-recommends \
        bzip2 \
        ca-certificates \
        git \
        libglib2.0-0 \
        libsm6 \
        libxext6 \
        libxrender1 \
        mercurial \
        openssh-client \
        procps \
        subversion \
        wget \
        sudo \
        tmux \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN useradd -m -s /bin/bash conda && \
    echo "conda ALL=(ALL:ALL) NOPASSWD:ALL" | tee /etc/sudoers.d/conda 

USER conda
WORKDIR /home/conda

ARG CONDA_VERSION=1.0.0

RUN set -x && \
    pwd && \
    MINICONDA_URL="https://github.com/e8035669/conda_cross/releases/download/v${CONDA_VERSION}/conda4arm-${CONDA_VERSION}-Linux-armv7l.sh" && \
    wget "${MINICONDA_URL}" -O miniconda.sh -q && \
    bash miniconda.sh -b -p ${HOME}/conda && \
    rm miniconda.sh && \
    echo ". ${HOME}/conda/etc/profile.d/conda.sh" >> ${HOME}/.bashrc && \
    echo "conda activate base" >> ${HOME}/.bashrc && \
    ${HOME}/conda/bin/conda clean -afy




