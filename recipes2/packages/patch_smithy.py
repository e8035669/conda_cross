#!/usr/bin/env python3

import sys
import argparse
from pathlib import Path
import shutil
from ruamel.yaml import YAML, CommentedMap, CommentedSeq

def parsearg():
    parser = argparse.ArgumentParser()
    parser.add_argument('feedstock')
    return parser.parse_args()

def main(args):
    print(args)
    feedstock = Path(args.feedstock)
    yaml = YAML()

    conda_forge_path = feedstock / 'conda-forge.yml'
    conda_forge = yaml.load(conda_forge_path)

    build_platform = {
        'linux_armv7l': 'linux_armv7l'
    }
    provider = {
        'linux_armv7l': 'azure',
        'linux_64': 'None',
        'osx_64': 'None',
        'win_64': 'None',
        'linux_ppc64le': 'None',
        'linux_aarch64': 'None',
    }

    conda_forge['build_platform'] = build_platform
    conda_forge['provider'] = provider

    channels = CommentedMap({
        'sources': CommentedSeq(['e8035669acarmv7', 'conda-forge']),
        'targets': CommentedSeq([
            CommentedSeq(['e8035669acarmv7', 'main']),
        ]),
    })
    conda_forge['channels'] = channels
    conda_forge['channels']['targets'][0].fa.set_flow_style()

    remote_ci_setup = "e8035669acarmv7::conda-forge-ci-setup=3"
    conda_forge['remote_ci_setup'] = remote_ci_setup

    print('Patched', conda_forge_path)
    bak_file = conda_forge_path.with_name(conda_forge_path.name + '.bak')
    if not bak_file.exists():
        conda_forge_path.rename(bak_file)

    yaml.dump(conda_forge, conda_forge_path)

    conda_build_config_path = feedstock / 'recipe' / 'conda_build_config.yaml'

    if conda_build_config_path.exists():
        conda_build_config = yaml.load(conda_build_config_path)
    else:
        conda_build_config = CommentedMap()

    channel_sources = [
        'e8035669acarmv7,conda-forge',
    ]
    channel_targets = [
        'e8035669acarmv7 main',
    ]

    docker_image = CommentedSeq(['e8035669/linux-anvil-armv7l'])
    docker_image.yaml_add_eol_comment('[os.environ.get("BUILD_PLATFORM") == "linux-armv7l"]', 0)
    conda_build_config['channel_sources'] = channel_sources
    conda_build_config['channel_targets'] = channel_targets
    conda_build_config.insert(len(conda_build_config), 'docker_image', docker_image)


    print()
    print('Patched', conda_build_config_path)
    bak_file = conda_build_config_path.with_name(conda_build_config_path.name + '.bak')
    if not bak_file.exists():
        conda_build_config_path.rename(bak_file)

    yaml.dump(conda_build_config, conda_build_config_path)


if __name__ == '__main__':
    main(parsearg())

