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


ENV GCC_VERSION 12.2.0
RUN curl -L -O https://ftp.gnu.org/gnu/gcc/gcc-${GCC_VERSION}/gcc-${GCC_VERSION}.tar.gz && \
    tar xf gcc-${GCC_VERSION}.tar.gz && \
    cd gcc-${GCC_VERSION} && \
    ./contrib/download_prerequisites && \
    mkdir build && \
    cd build && \
    ../configure --prefix=/usr/local \
        --with-abi=aapcs-linux \
        # --with-cpu=cortex-a53 \
        # --with-fpu=neon-fp-armv8 \
        --with-float=hard \
        --with-mode=arm \
        --enable-default-pie \
        --enable-languages=c,c++,fortran,objc,obj-c++ \
        --enable-__cxa_atexit \
        --disable-libmudflap \
        --enable-libgomp \
        --disable-libssp \
        --enable-libquadmath \
        --enable-libquadmath-support \
        --enable-libsanitizer \
        --enable-lto \
        --enable-threads=posix \
        --enable-target-optspace \
        --enable-plugin \
        --enable-gold \
        --disable-nls \
        --disable-bootstrap \
        --disable-multilib \
        --enable-long-long && \
    make -j8 && \
    make install && \
    cd ../../ && \
    rm -rf gcc-${GCC_VERSION} gcc-${GCC_VERSION}.tar.gz

RUN CC=/usr/local/bin/gcc CXX=/usr/local/bin/g++ ${CFS_PREFIX}/bin/python3 -m pip install lief

