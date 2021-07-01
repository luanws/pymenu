import os
from typing import Callable, List, Tuple

import keyboard

from pymenu.option import Option


class Menu:
    def __init__(self, title: str, options: List[Option] = []) -> None:
        self.title = title
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
        keyboard.add_hotkey('enter', self.enter)
        keyboard.wait()

    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def __update(self):
        self.clear()
        for i, script in enumerate(self.options):
            if i == self.__selected_index:
                try:
                    print('\033[96m', end='')
                    print(i + 1, '-', script)
                finally:
                    print('\033[0;0m', end='')
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

    def enter(self):
        self.clear()
        option = self.options[self.__selected_index]
        option()
