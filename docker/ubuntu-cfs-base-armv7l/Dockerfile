FROM arm32v7/ubuntu:22.04

# Set an encoding to make things work smoothly.
ENV LANG en_US.UTF-8

RUN apt-get update && \
    apt-get install -y tzdata && \
    ln -fs /usr/share/zoneinfo/Asia/Taipei /etc/localtime && \
    dpkg-reconfigure -f noninteractive tzdata && \
    rm -rf /var/lib/apt/lists/*

# location where conda from scatch is installed
ENV CFS_PREFIX /opt/cfs

RUN apt-get update && apt-get install -y tar curl \
    build-essential gdb lcov pkg-config \
    libbz2-dev libffi-dev libgdbm-dev libgdbm-compat-dev liblzma-dev \
    libncurses5-dev libreadline6-dev libsqlite3-dev libssl-dev \
    lzma lzma-dev tk-dev uuid-dev zlib1g-dev cmake git && \
    rm -rf /var/lib/apt/lists/*

ENV PYTHON_VERSION 3.10.9
RUN curl -O https://www.python.org/ftp/python/${PYTHON_VERSION}/Python-${PYTHON_VERSION}.tgz && \
    tar xf Python-${PYTHON_VERSION}.tgz && \
    cd Python-${PYTHON_VERSION} && \
    ./configure --disable-shared --prefix ${CFS_PREFIX} && \
    make -j && \
    make install && \
    ln -s ${CFS_PREFIX}/bin/python3 ${CFS_PREFIX}/bin/python && \
    ln -s ${CFS_PREFIX}/bin/pip3 ${CFS_PREFIX}/bin/pip && \
    cd .. && \
    rm -rf Python-${PYTHON_VERSION} Python-${PYTHON_VERSION}.tgz

ENV LIBARCHIVE_VERSION 3.6.2
ENV LIBARCHIVE=/opt/cfs/lib/libarchive.so
RUN curl -O https://www.libarchive.org/downloads/libarchive-${LIBARCHIVE_VERSION}.tar.gz && \
    tar xf libarchive-${LIBARCHIVE_VERSION}.tar.gz && \
    cd libarchive-${LIBARCHIVE_VERSION} && \
    ./configure --prefix ${CFS_PREFIX} && \
    make -j && \
    make install && \
    cd .. && \
    rm -rf libarchive-${LIBARCHIVE_VERSION} libarchive-${LIBARCHIVE_VERSION}.tar.gz

RUN ${CFS_PREFIX}/bin/python3 -m pip install six tqdm libarchive-c

ENV CPH_VERSION 2.0.2
RUN curl -L -O https://github.com/conda/conda-package-handling/archive/refs/tags/${CPH_VERSION}.tar.gz && \
    tar xf ${CPH_VERSION}.tar.gz && \
    cd conda-package-handling-${CPH_VERSION} && \
    ${CFS_PREFIX}/bin/python3 setup.py install --single-version-externally-managed --record record.txt && \
    cd .. && \
    rm -rf conda-package-handling-${CPH_VERSION} ${CPH_VERSION}.tar.gz

RUN curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs -o rustup.sh && \
    sh rustup.sh -y && \
    rm -rf rustup.sh

RUN export PATH=$PATH:/root/.cargo/bin && \
    ${CFS_PREFIX}/bin/python3 -m pip install requests pycosat pyopenssl ruamel.yaml pluggy

ENV CONDA_VERSION 23.1.0
RUN curl -L -O https://github.com/conda/conda/archive/${CONDA_VERSION}.tar.gz && \
    tar xf ${CONDA_VERSION}.tar.gz && \
    cd conda-${CONDA_VERSION} && \
    echo ${CONDA_VERSION} > conda/.version && \
    ${CFS_PREFIX}/bin/python3 setup.py install --single-version-externally-managed --record record.txt && \
    ${CFS_PREFIX}/bin/python3 -m conda init --install && \
    ln -s ${CFS_PREFIX}/etc/profile.d/conda.sh /etc/profile.d/conda.sh && \
    mkdir -p ${CFS_PREFIX}/conda-meta && \
    cd .. && \
    rm -rf conda-${CONDA_VERSION} ${CONDA_VERSION}.tar.gz

ENV CONDA_SUBDIR linux-armv7l


