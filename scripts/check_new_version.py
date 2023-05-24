import json
import requests
import operator
import itertools
from conda.models.version import VersionOrder


def get_repodata(subdir):
    url = f'https://conda.anaconda.org/{subdir}/repodata.json'
    print('get url', url)
    ret = requests.get(url, timeout=60)
    if ret.ok:
        return ret.json()

    raise RuntimeError(ret.text)


def chain_pkgs(js_data):
    return itertools.chain(js_data['packages.conda'].values(), js_data['packages'].values())


def chain_pkgs2(data1, data2):
    return itertools.chain(
        data1['packages.conda'].values(),
        data1['packages'].values(),
        data2['packages.conda'].values(),
        data2['packages'].values(),
    )


def get_all_pkgname(pkgs):
    pkgnames = map(operator.itemgetter('name'), pkgs)
    return set(pkgnames)


def get_newest_version(pkgs, pkgname):
    filter_pkgs = filter(lambda p: p['name'] == pkgname, pkgs)
    all_versions = map(operator.itemgetter('version'), filter_pkgs)
    all_versions = set(all_versions)
    all_versions = [VersionOrder(v) for v in all_versions]
    if len(all_versions) > 0:
        return max(all_versions)
    return None

def main():
    myrepodata_noarch = get_repodata('e8035669acarmv7/noarch')
    myrepodata_armv7l = get_repodata('e8035669acarmv7/linux-armv7l')

    conda_noarch = get_repodata('conda-forge/noarch')
    conda_x64 = get_repodata('conda-forge/linux-64')

    all_pkgs = lambda: chain_pkgs2(myrepodata_armv7l, myrepodata_noarch)
    conda_forge_pkg = lambda: chain_pkgs2(conda_noarch, conda_x64)

    pkgnames = get_all_pkgname(all_pkgs())


    not_found = []
    greater = []
    lower = []

    for name in pkgnames:
        version = get_newest_version(all_pkgs(), name)
        print(name, version)

        conda_version = get_newest_version(conda_forge_pkg(), name)
        if conda_version is None:
            not_found.append(name)
        elif conda_version > version:
            greater.append((name, version, conda_version))
        elif conda_version < version:
            lower.append((name, version, conda_version))

    print('-' * 10, 'package not found ', '-' * 10)
    for p in not_found:
        print(p)

    print('-' * 10, 'package newer', '-' * 10)
    for p, v, vc in lower:
        print(p, f'{v} -> {vc}')

    print('-' * 10, 'need update', '-' * 10)
    for p, v, vc in greater:
        print(p, f'{v} -> {vc}')




if __name__ == '__main__':
    main()
