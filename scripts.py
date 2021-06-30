import sys
import os
import shutil
import setuptools
from contextlib import suppress

args = sys.argv[1:]


def clear_build():
    folders = ['build', 'dist', 'pymenu.egg-info']
    for folder in folders:
        with suppress(FileNotFoundError):
            shutil.rmtree(folder)


def show_packages():
    print(setuptools.find_packages())


scripts = {
    'build': 'python setup.py sdist bdist_wheel',
    'publish': 'twine upload dist/*',
    'clear_build': clear_build,
    'deploy': [
        clear_build,
        'python setup.py sdist bdist_wheel',
        'twine upload dist/*',
        clear_build,
    ],
    'show_packages': show_packages,
}

commands = []
for arg in args:
    if scripts.keys().__contains__(arg):
        commands.append(scripts[arg])


def run_command(command):
    if isinstance(command, str):
        os.system(command)
    elif callable(command):
        command()


for command in commands:
    if isinstance(command, list):
        [run_command(c) for c in command]
    else:
        run_command(command)


if (len(args) == 0):
    print(list(scripts.keys()))
