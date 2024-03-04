import os
import shutil
from contextlib import suppress

import dotenv
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
    token = dotenv.get_key('.env', 'PYPI_TOKEN')
    os.system('python setup.py sdist bdist_wheel')
    os.system(f'twine upload -u __token__ -p {token} dist/*')
    clear_build()


menu = Menu('Scripts')
menu.add_options([
    ('build', lambda: os.system('python setup.py sdist bdist_wheel')),
    ('package', lambda: os.system('twine upload dist/*')),
    ('clear build', clear_build),
    ('show packages', show_packages),
    ('deploy', deploy),
])
menu.show()
