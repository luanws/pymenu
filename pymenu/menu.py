import os
from typing import Callable, List, Tuple

import keyboard
from termcolor import colored

from pymenu.option import Option


class Menu:
    def __init__(
        self, title: str, options: List[Option] = [],
        title_color: str = 'blue', selected_color: str = 'cyan'
    ) -> None:
        self.title = title
        self.title_color = title_color
        self.selected_color = selected_color
        self.options = options
        self.__selected_index: int = 0

    def add_option(self, option: Tuple[str, Callable]):
        name, call = option
        self.options.append(Option(name, call))

    def add_options(self, options: List[Tuple[str, Callable]]):
        for option in options:
            self.add_option(option)

    def show(self):
        self.__update()
        keyboard.add_hotkey('up', self.up)
        keyboard.add_hotkey('down', self.down)
        self.wait_for_command()
        self.run_selected()

    def remove_keyboard_listener(self):
        keyboard.remove_hotkey('up')
        keyboard.remove_hotkey('down')

    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def __update(self):
        self.clear()
        print(colored(self.title, self.title_color), '\n')
        for i, script in enumerate(self.options):
            if i == self.__selected_index:
                print(colored(f'{i+1} - {script}', self.selected_color))
            else:
                print(i + 1, '-', script)

    def up(self):
        if self.__selected_index > 0:
            self.__selected_index -= 1
            self.__update()

    def down(self):
        if self.__selected_index < len(self.options) - 1:
            self.__selected_index += 1
            self.__update()

    def wait_for_command(self):
        command = input()
        self.remove_keyboard_listener()
        if command.isnumeric():
            option_number = int(command)
            self.__selected_index = option_number - 1

    def run_selected(self):
        self.clear()
        option = self.options[self.__selected_index]
        option()
