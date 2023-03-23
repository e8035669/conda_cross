FROM arm32v7/centos:7

# configure yum and rpm for running on armv8l
RUN echo "armhfp" > /etc/yum/vars/basearch && \
    echo "armv7hl" > /etc/yum/vars/arch && \
    echo "armv7hl-redhat-linux-gpu" > /etc/rpm/platform

# Set an encoding to make things work smoothly.
ENV LANG en_US.UTF-8

# location where conda from scatch is installed
ENV CFS_PREFIX /opt/cfs

# Resolves a nasty NOKEY warning that appears when using yum.
RUN rpm --import /etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-SIG-AltArch-Arm32 && \
    rpm --import /etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-7

# Fix up issues with locales because the default images have these minimized
# to the point of not being properly functional
# See: https://github.com/CentOS/sig-cloud-instance-images/issues/71
RUN yum update -y && \
    yum reinstall -y glibc-common && \
    yum clean all
RUN localedef -i en_US -f UTF-8 en_US.UTF-8

# Install basic requirements.
RUN yum update -y && \
    yum install -y \
        bzip2 \
        tar \
        which \
        git \
    && yum clean all

# Build tools, gcc will be removed at the end
RUN yum install -y \
    curl \
    gcc \
    make \
    perl \
    perl-core \
    pcre-devel \
    wget \
  && yum clean all

# Install Python from source
# system library headers needed by Python, removed after Python install
RUN yum install -y \
    bzip2-devel \
    libffi-devel \
#    openssl-devel \
    readline-devel \
    sqlite-devel \
    zlib-devel \
    uuid-devel \
    lzma-devel \
  && yum clean all

ENV OPENSSL_VERSION 1.1.1k
RUN curl -O https://ftp.openssl.org/source/openssl-${OPENSSL_VERSION}.tar.gz && \
    tar xf openssl-${OPENSSL_VERSION}.tar.gz && \
    pushd openssl-${OPENSSL_VERSION} && \
    ./config --prefix=/usr && \
    make -j && \
    make install && \
    popd && \
    rm -rf openssl-${OPENSSL_VERSION} openssl-${OPENSSL_VERSION}.tar.gz


ENV PYTHON_VERSION 3.10.9
RUN curl -O https://www.python.org/ftp/python/${PYTHON_VERSION}/Python-${PYTHON_VERSION}.tgz && \
    tar xf Python-${PYTHON_VERSION}.tgz && \
    pushd Python-${PYTHON_VERSION} && \
    ./configure --disable-shared --prefix ${CFS_PREFIX} && \
    make -j && \
    make install && \
    ln -s ${CFS_PREFIX}/bin/python3 ${CFS_PREFIX}/bin/python && \
    ln -s ${CFS_PREFIX}/bin/pip3 ${CFS_PREFIX}/bin/pip && \
    popd && \
    rm -rf Python-${PYTHON_VERSION} Python-${PYTHON_VERSION}.tgz

ENV LIBARCHIVE_VERSION 3.6.2
ENV LIBARCHIVE=/opt/cfs/lib/libarchive.so
RUN curl -O https://www.libarchive.org/downloads/libarchive-${LIBARCHIVE_VERSION}.tar.gz && \
    tar xf libarchive-${LIBARCHIVE_VERSION}.tar.gz && \
    pushd libarchive-${LIBARCHIVE_VERSION} && \
    ./configure --prefix ${CFS_PREFIX} && \
    make -j && \
    make install && \
    popd && \
    rm -rf libarchive-${LIBARCHIVE_VERSION} libarchive-${LIBARCHIVE_VERSION}.tar.gz

RUN ${CFS_PREFIX}/bin/python3 -m pip install six tqdm libarchive-c

ENV CPH_VERSION 2.0.2
RUN curl -L -O https://github.com/conda/conda-package-handling/archive/refs/tags/${CPH_VERSION}.tar.gz && \
    tar xf ${CPH_VERSION}.tar.gz && \
    pushd conda-package-handling-${CPH_VERSION} && \
    ${CFS_PREFIX}/bin/python3 setup.py install --single-version-externally-managed --record record.txt && \
    popd && \
    rm -rf conda-package-handling-${CPH_VERSION} ${CPH_VERSION}.tar.gz

RUN curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs -o rustup.sh && \
    sh rustup.sh -y && \
    rm -rf rustup.sh

RUN export PATH=$PATH:/root/.cargo/bin && \
    ${CFS_PREFIX}/bin/python3 -m pip install requests pycosat pyopenssl ruamel.yaml pluggy

ENV CONDA_VERSION 23.1.0
RUN curl -L -O https://github.com/conda/conda/archive/${CONDA_VERSION}.tar.gz && \
    tar xf ${CONDA_VERSION}.tar.gz && \
    pushd conda-${CONDA_VERSION} && \
    echo ${CONDA_VERSION} > conda/.version && \
    ${CFS_PREFIX}/bin/python3 setup.py install --single-version-externally-managed --record record.txt && \
    ${CFS_PREFIX}/bin/python3 -m conda init --install && \
    ln -s ${CFS_PREFIX}/etc/profile.d/conda.sh /etc/profile.d/conda.sh && \
    mkdir -p ${CFS_PREFIX}/conda-meta && \
    popd && \
    rm -rf conda-${CONDA_VERSION} ${CONDA_VERSION}.tar.gz

ENV CONDA_SUBDIR linux-armv7l


