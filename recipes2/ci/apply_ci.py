#!/usr/bin/env python3

import os
from pathlib import Path
import argparse
import shutil
import subprocess

from ruamel.yaml import YAML

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

def parsearg():
    parser = argparse.ArgumentParser()
    parser.add_argument('paths', nargs='*', help='add custom configs')
    return parser.parse_args()

def main(args):
    print(args)
    print('SCRIPT_DIR', SCRIPT_DIR)

    target_config = './.github/workflows/conda-build-package.yml'
    target_script = './.scripts/run_armv7l_build.sh'
    if args.paths and len(args.paths) > 0:
        print('Apply script with config')
        paths = args.paths
        yaml = YAML(typ='rt')
        conf_obj = yaml.load((Path(SCRIPT_DIR) / 'conda-build-package.yml').read_text())
        matrix_include = conf_obj['jobs']['build-linux']['strategy']['matrix']['include']
        matrix_include.clear()
        for i in paths:
            matrix_include.append({'name': os.path.basename(i), 'config_file': str(i)})

        print('Write', target_config)
        with open(target_config, 'w') as f:
            yaml.dump(conf_obj, f)
        subprocess.run(['git', 'add', '-f', *paths], check=True)

    else:
        print('Apply default scripts')
        src_config = os.path.join(SCRIPT_DIR, 'conda-build-package.yml')
        print('Write', target_config)
        shutil.copyfile(src_config, target_config)

    src_script = os.path.join(SCRIPT_DIR, 'run_armv7l_build.sh')
    print('Write', target_script)
    shutil.copyfile(src_script, target_script)

    subprocess.run(['git', 'add', '-f', target_config, target_script], check=True)

    wrong_file = './.github/workflows/conda-build-packege.yml'
    if os.path.exists(wrong_file):
        print('Remove wrong file', wrong_file)
        Path(wrong_file).unlink()

    pass


if __name__ == '__main__':
    main(parsearg())

