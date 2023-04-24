FROM cfs-builder-armv7l

RUN ${CFS_PREFIX}/bin/conda config --append channels e8035669 && \
    ${CFS_PREFIX}/bin/conda config --set anaconda_upload true

RUN yum install -y patch gettext gettext-devel gettext-common-devel && \
    yum clean all

