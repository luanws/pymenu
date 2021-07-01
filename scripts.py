import os
import shutil
from contextlib import suppress

import setuptools

from pymenu import Menu


def clear_build():
    folders = ['build', 'dist', 'pymenu_console.egg-info']
    for folder in folders:
        with suppress(FileNotFoundError):
            shutil.rmtree(folder)


def show_packages():
    print(setuptools.find_packages())


def deploy():
    clear_build()
    os.system('python setup.py sdist bdist_wheel')
    os.system('twine upload dist/*')
    clear_build()


menu = Menu('Scripts')
menu.add_options([
    ('build', lambda: os.system('python setup.py sdist bdist_wheel')),
    ('publish', lambda: os.system('twine upload dist/*')),
    ('clear build', lambda: clear_build),
    ('show packages', show_packages),
    ('deploy', deploy),
])
menu.show()
