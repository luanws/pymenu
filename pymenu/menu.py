from __future__ import annotations

import os
from typing import Callable, List, Tuple, Union

import keyboard
from termcolor import colored

from pymenu.option import Option
from pymenu.utils import inputs


class Menu:
    def __init__(
        self,
        title: str,
        options: List[Option] = None,
        title_color: str = 'blue',
        selected_color: str = 'cyan',
        back_name: str = '<-',
        prefix: str = '%s) ',
        enable_keyboard_selection: bool = True,
    ) -> None:
        self.title = title
        self.title_color = title_color
        self.selected_color = selected_color
        self.options = options or []
        self.__selected_index: int = 0
        self.back_name = back_name
        self.prefix = prefix
        self.enable_keyboard_selection = enable_keyboard_selection

    def open_submenu(self, submenu: Menu):
        self.clear()
        if submenu.options[-1].name != self.back_name:
            submenu.add_option(self.back_name, lambda: self.return_to_this_menu(submenu))
        submenu.show()

    def return_to_this_menu(self, submenu: Menu):
        submenu.clear()
        self.show()

    def add_option(self, name: str, call: Union[Callable, Menu]):
        if isinstance(call, Menu):
            submenu: Menu = call
            if len(submenu.options) > 0:
                self.options.append(Option(name, lambda: self.open_submenu(submenu)))
        else:
            self.options.append(Option(name, call))

    def add_options(self, options: List[Tuple[str, Union[Callable, Menu]]]):
        for option in options:
            self.add_option(*option)

    def show(self):
        self.__update()
        if self.enable_keyboard_selection:
            keyboard.add_hotkey('up', self.up)
            keyboard.add_hotkey('down', self.down)
        self.wait_for_command()
        self.run_selected()

    def remove_keyboard_listener(self):
        if self.enable_keyboard_selection:
            keyboard.remove_hotkey('up')
            keyboard.remove_hotkey('down')

    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def __update(self):
        self.clear()
        print(colored(self.title, self.title_color), '\n')
        for i, script in enumerate(self.options):
            prefix = self.prefix % (i + 1)
            if self.enable_keyboard_selection and i == self.__selected_index:
                print(colored(f'{prefix}{script}', self.selected_color))
            else:
                print(f'{prefix}{script}')

    def up(self):
        if self.__selected_index > 0:
            self.__selected_index -= 1
            self.__update()

    def down(self):
        if self.__selected_index < len(self.options) - 1:
            self.__selected_index += 1
            self.__update()

    def wait_for_command(self):
        command = inputs.get_numeric_input()
        self.remove_keyboard_listener()
        if command.isnumeric():
            option_number = int(command)
            self.__selected_index = option_number - 1

    @property
    def selected_option(self):
        return self.options[self.__selected_index]

    def run_selected(self):
        self.clear()
        self.selected_option()
