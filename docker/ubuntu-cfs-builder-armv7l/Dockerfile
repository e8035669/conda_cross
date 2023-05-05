FROM ubuntu-cfs-base-armv7l

RUN apt-get update && \
    apt-get install -y cmake && \
    rm -rf /var/lib/apt/lists/*


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

# ENV CMAKE_VERSION 3.8.2
# RUN curl -L -O https://github.com/Kitware/CMake/releases/download/v${CMAKE_VERSION}/cmake-${CMAKE_VERSION}.tar.gz && \
#     tar xf cmake-${CMAKE_VERSION}.tar.gz && \
#     pushd cmake-${CMAKE_VERSION} && \
#     ./bootstrap --parallel=8 && \
#     make -j8 && \
#     make install && \
#     popd && \
#     rm -rf cmake-${CMAKE_VERSION}.tar.gz cmake-${CMAKE_VERSION}

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
    lief \
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


