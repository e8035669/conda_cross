
conda config --prepend channels e8035669acarmv7
conda config --prepend channels conda-forge
conda config --remove channels defaults
conda config --set anaconda_upload true
mkdir -p /root/.continuum/anaconda-client/
touch /root/.continuum/anaconda-client/config.yaml
anaconda config --set upload_user e8035669acarmv7
