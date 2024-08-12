
conda config --prepend channels e8035669acarmv7
conda config --prepend channels conda-forge
conda config --remove channels defaults
conda config --set anaconda_upload true
mkdir -p ${HOME}/.continuum/anaconda-client/
touch ${HOME}/.continuum/anaconda-client/config.yaml
anaconda config --set upload_user e8035669acarmv7
conda config --set conda_build.pkg_format 2
