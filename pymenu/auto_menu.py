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


def run_python_file(path: str):
    os.system(f'python {path}')


def create_menu_from_directory(path: str, prefix: str = None) -> Menu:
    title = get_directory_name(path)
    title = prefix + title if prefix else title
    menu = Menu(title)
    for file in get_all_files_from_directory(path):
        menu.add_option(file, lambda: run_python_file(os.path.join(path, file)))
    for folder in get_all_folders_from_directory(path):
        menu.add_option(folder, create_menu_from_directory(os.path.join(path, folder), f'{title} > '))
    return menu
