import re
import os
from typing import List

from pymenu import Menu

exclude_folders = ['__pycache__']
exclude_files = ['__init__.py']


def is_python_file(path: str) -> bool:
    return path.endswith('.py')


def get_all_files_from_directory(path: str) -> List[str]:
    files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    files = [f for f in files if f not in exclude_files]
    files = [f for f in files if is_python_file(f)]
    return files


def get_all_folders_from_directory(path: str) -> List[str]:
    folders = [f for f in os.listdir(path) if os.path.isdir(os.path.join(path, f))]
    folders = [f for f in folders if f not in exclude_folders]
    return folders


def get_directory_name(path: str) -> str:
    return os.path.basename(os.path.normpath(path))


def python_filename_to_module_name(filename: str) -> str:
    module_name = filename.replace(os.getcwd(), '').replace('/', '.').replace('\\', '.').replace('.py', '')
    module_name = re.sub(r'^\.', '', module_name)
    return module_name


def run_python_module(module_name: str):
    os.system(f'python -m {module_name}')


def create_menu_from_directory(path: str, prefix: str = None, *args, **kwargs) -> Menu:
    title = get_directory_name(path)
    title = prefix + title if prefix else title
    menu = Menu(title, *args, **kwargs)

    def file_callback(path: str, file: str):
        python_module = python_filename_to_module_name(os.path.join(path, file))
        return lambda: run_python_module(python_module)

    for file in get_all_files_from_directory(path):
        menu.add_option(file, file_callback(path, file))

    for folder in get_all_folders_from_directory(path):
        menu.add_option(folder, create_menu_from_directory(os.path.join(path, folder), f'{title} > ', *args, **kwargs))

    return menu
