from typing import List, TypeVar

from pymenu import Menu

T = TypeVar('T')


def create_select_menu(options: List[T], title: str = 'Select an option') -> T:
    selected_option: T

    def select_option(option: T) -> None:
        nonlocal selected_option
        selected_option = option

    menu = Menu(title)
    for option in options:
        def callback(option: T):
            return lambda: select_option(option)

        menu.add_option(str(option), callback(option))
    menu.show()

    return selected_option
