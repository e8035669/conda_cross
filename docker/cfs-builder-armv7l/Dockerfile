FROM cfs-base-armv7l

RUN yum install -y gcc-c++ && yum clean all

ENV PATCHELF_VERSION  0.17.2
RUN curl -L -O https://github.com/NixOS/patchelf/releases/download/${PATCHELF_VERSION}/patchelf-${PATCHELF_VERSION}-armv7l.tar.gz && \
    tar xvf patchelf-${PATCHELF_VERSION}-armv7l.tar.gz -C /usr && \
    rm -rf patchelf-${PATCHELF_VERSION}-armv7l.tar.gz

# ENV PATCHELF_VERSION  0.17.2
# RUN curl -L -O https://github.com/NixOS/patchelf/releases/download/${PATCHELF_VERSION}/patchelf-${PATCHELF_VERSION}.tar.gz && \
#     tar xf patchelf-${PATCHELF_VERSION}.tar.gz && \
#     cd patchelf-${PATCHELF_VERSION} && \
#     ./configure --prefix ${CFS_PREFIX} && \
#     make -j && \
#     make install && \
#     cd .. && \
#     rm -rf patchelf-${PATCHELF_VERSION} patchelf-${PATCHELF_VERSION}.tar.gz

ENV CMAKE_VERSION 3.26.3
RUN curl -L -O https://github.com/Kitware/CMake/releases/download/v${CMAKE_VERSION}/cmake-${CMAKE_VERSION}.tar.gz && \
    tar xf cmake-${CMAKE_VERSION}.tar.gz && \
    pushd cmake-${CMAKE_VERSION} && \
    ./bootstrap --parallel=8 && \
    make -j8 && \
    make install && \
    popd && \
    rm -rf cmake-${CMAKE_VERSION}.tar.gz cmake-${CMAKE_VERSION}

ENV GCC_VERSION 12.2.0
RUN curl -L -O https://ftp.gnu.org/gnu/gcc/gcc-${GCC_VERSION}/gcc-${GCC_VERSION}.tar.gz && \
    tar xf gcc-${GCC_VERSION}.tar.gz && \
    cd gcc-${GCC_VERSION} && \
    ./contrib/download_prerequisites && \
    mkdir build && \
    cd build && \
    ../configure --prefix=/usr/local \
        --with-abi=aapcs-linux \
        # --with-arch=armv7 \
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

RUN echo "/usr/local/lib" >> /etc/ld.so.conf.d/sys-libs.conf && \
    echo "/usr/lib" >> /etc/ld.so.conf.d/sys-libs.conf && \
    echo "/lib" >> /etc/ld.so.conf.d/sys-libs.conf && \
    ldconfig

RUN ${CFS_PREFIX}/bin/python3 -m pip install \
    beautifulsoup4 \
    chardet \
    filelock \
    glob2 \
    jinja2 \
    pkginfo \
    psutil \
    pytz \
    pyyaml \
    six \
    tqdm \
    toml \
    #lief \
    git+https://github.com/Anaconda-Server/anaconda-client

ENV CONDA_BUILD_VERSION 3.23.3
RUN curl -L -O https://github.com/conda/conda-build/archive/${CONDA_BUILD_VERSION}.tar.gz && \
    tar xf ${CONDA_BUILD_VERSION}.tar.gz && \
    cd conda-build-${CONDA_BUILD_VERSION} && \
    ${CFS_PREFIX}/bin/python3 setup.py install --single-version-externally-managed --record record.txt && \
    cd .. && \
    rm -rf conda-build-${CONDA_BUILD_VERSION} ${CONDA_BUILD_VERSION}.tar.gz

ENV CONDA_PACKAGE_STREAMING_VERSION 0.7.0
RUN curl -L -O https://github.com/conda/conda-package-streaming/archive/refs/tags/v${CONDA_PACKAGE_STREAMING_VERSION}.tar.gz && \
    tar xf v${CONDA_PACKAGE_STREAMING_VERSION}.tar.gz && \
    cd conda-package-streaming-${CONDA_PACKAGE_STREAMING_VERSION} && \
    ${CFS_PREFIX}/bin/python3 -m pip install . && \
    cd .. && \
    rm -rf conda-package-streaming-${CONDA_PACKAGE_STREAMING_VERSION} v${CONDA_PACKAGE_STREAMING_VERSION}.tar.gz

# ENV MAMBA_VERSION=1.4.2 MAMBA_FNAME=2023.04.06
# RUN curl -L -O https://github.com/mamba-org/mamba/archive/refs/tags/${MAMBA_FNAME}.tar.gz && \
#     tar xvf ${MAMBA_FNAME}.tar.gz && \
#     cd ${MAMBA_FNAME} && \
#     mkdir build && \
#     cd build && \
#     cmake -DCMAKE_INSTALL_PREFIX=${CFS_PREFIX} .. && \
#     make install && \
#     cd ../../ && \
#     rm -rf ${MAMBA_FNAME} ${MAMBA_FNAME}.tar.gz


