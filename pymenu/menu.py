from __future__ import annotations

import os
from typing import Callable, List, Tuple, Union

from termcolor import colored

from pymenu.option import Option
from pymenu.utils.keyboard import input_key


class Menu:
    text: str

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
        self.text = ''

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
        
        if self.text:
            print(f'\n{self.text}')
        self.wait_for_command()

    def up(self):
        if self.__selected_index > 0:
            self.__selected_index -= 1

    def down(self):
        if self.__selected_index < len(self.options) - 1:
            self.__selected_index += 1

    def text_input(self, number: str):
        self.text += number

    def backspace(self):
        if self.text:
            self.text = self.text[:-1]

    def wait_for_command(self):
        key = input_key()
        if key == 'ENTER':
            return self.run_selected()
        elif key == 'UP':
            self.up()
        elif key == 'DOWN':
            self.down()
        elif key == 'BACKSPACE':
            self.backspace()
        elif key.isnumeric():
            self.text_input(key)
        self.__update()

    @property
    def selected_option(self):
        return self.options[self.__selected_index]

    def run_selected(self):
        self.clear()
        if self.text and self.text.isnumeric():
            number = int(self.text)
            self.__selected_index = number - 1
        self.selected_option()
