FROM cfs-builder-armv7l

# base packages
RUN yum install -y \
    file \
    libX11 \
    libXau \
    libxcb \
    libXdmcp \
    libXext \
    libXrender \
    libXt \
    mesa-libGL \
    mesa-libGLU \
    openssh-clients \
    patch \
    rsync \
    util-linux \
    wget \
    which \
    bzip2 \
    xorg-x11-server-Xvfb \
    && yum clean all

# ctng packages
RUN yum install -y \
    autoconf \
    gperf  \
    bison  \
    flex  \
    texinfo  \
    help2man  \
    gcc-c++  \
    gcc-gfortran \
    patch \
    ncurses-devel  \
    python-devel  \
    perl-Thread-Queue  \
    bzip2  \
    git \
    m4 \
    sed \
    findutils \
   && yum clean all

#crosstool-ng packages
RUN yum install -y \
    automake \
    libtool \
    make \
    unzip \
    && yum clean all

ENV SHELLCHECK_VERSION 0.9.0
RUN curl -L -O https://github.com/koalaman/shellcheck/releases/download/v${SHELLCHECK_VERSION}/shellcheck-v${SHELLCHECK_VERSION}.linux.armv6hf.tar.xz && \
    tar xvf shellcheck-v${SHELLCHECK_VERSION}.linux.armv6hf.tar.xz && \
    cp shellcheck-v${SHELLCHECK_VERSION}/shellcheck /usr/local/bin/shellcheck && \
    rm -rf shellcheck-v${SHELLCHECK_VERSION}.linux.armv6hf.tar.xz shellcheck-v${SHELLCHECK_VERSION}



