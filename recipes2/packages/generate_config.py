#!/usr/bin/env python3

import glob
import sys
from pathlib import Path
import argparse

from ruamel.yaml import YAML

def parsearg():
    parser = argparse.ArgumentParser()
    parser.add_argument('--yaml')
    parser.add_argument('--python', action='store_true', help='python mode, split python version as parallel ci')
    return parser.parse_args()

def main(arg):
    print(arg)

    if not arg.yaml:
        all_files = glob.glob('.ci_support/linux_*.yaml')
        if len(all_files) == 1:
            raise RuntimeError('Maybe this project is noarch')

        files = glob.glob('.ci_support/linux_64*cpython*.yaml')

        if len(files) == 0:
            files = glob.glob('.ci_support/linux_64*.yaml')
        template_file = files[0]
    else:
        template_file = arg.yaml

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
        pyvers = ['3.12', '3.11', '3.10', '3.9', '3.8']
        if 'cpython' in orig:
            data['python'] = [f"{i}.* *_cpython" for i in pyvers]
        else:
            data['python'] = pyvers

    if 'python_impl' in data:
        data['python_impl'] = ['cpython'] * 5

    if 'c_stdlib_version' in data:
        data['c_stdlib_version'][0] = '2.17'

    data.update(override)


    output = Path('linux_armv7l_config.yaml')
    yaml.dump(data, sys.stdout)

    print('Write to', output)
    yaml.dump(data, output)

    if arg.python:
        pynames = ['312', '311', '310', '39', '38']
        if 'python' not in data and 'python_impl' not in data:
            raise RuntimeError('maybe this is not python package?')

        for i, pyname in enumerate(pynames):
            new_data = data.copy()
            if 'python' in data:
                new_data['python'] = [data['python'][i]]

            if 'python_impl' in data:
                new_data['python_impl'] = [data['python_impl'][i]]

            output_path = Path('.ci_support') / f'linux_armv7l_config_py{pyname}.yaml'
            print('Write to', output_path)
            yaml.dump(new_data, output_path)





if __name__ == '__main__':
    main(parsearg())

