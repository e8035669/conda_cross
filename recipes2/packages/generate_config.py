#!/usr/bin/env python3

import glob
import sys
from pathlib import Path
from ruamel.yaml import YAML

def main():

    all_files = glob.glob('.ci_support/linux_*.yaml')
    if len(all_files) == 1:
        raise RuntimeError('Maybe this project is noarch')

    files = glob.glob('.ci_support/linux_64*cpython*.yaml')

    if len(files) == 0:
        files = glob.glob('.ci_support/linux_64*.yaml')

    template_file = files[0]
    print('Read template file', template_file)


    yaml = YAML()

    override = {}
    override_path = Path('override.yaml')
    if override_path.exists():
        override = yaml.load(override_path)

    data = yaml.load(Path(template_file))

    compiler_keys = ['c_compiler_version', 'cxx_compiler_version']
    for key in compiler_keys:
        if key in data:
            ver = int(data[key][0])
            ver = max(ver, 12)
            data[key][0] = str(ver)

    if 'cdt_name' in data:
        data['cdt_name'][0] = 'cos7'
        keys = list(data.keys())
        index = keys.index('cdt_name')
        data.insert(index + 1, 'cdt_arch', ['armv7l'])


    if 'target_platform' in data:
        data['target_platform'][0] = 'linux-armv7l'

    if 'python' in data:
        orig = data['python'][0]
        pyvers = ['3.11', '3.10', '3.9', '3.8']
        if 'cpython' in orig:
            data['python'] = [f"{i}.* *_cpython" for i in pyvers]
        else:
            data['python'] = pyvers

    if 'python_impl' in data:
        data['python_impl'] = ['cpython'] * 4

    data.update(override)


    output = Path('linux_armv7l_config.yaml')
    yaml.dump(data, sys.stdout)

    print('Write to', output)
    yaml.dump(data, output)


if __name__ == '__main__':
    main()

