# pymenu

pymenu is a python library for creating interactive, console-based menus. It allows for the creation of menus that can be controlled with keyboard arrows, and can also automatically generate menus from files in a folder. 

## Installation

To install pymenu, simply run the following command:

```
pip install pymenu-console
```

## Usage

pymenu makes it easy to create menus for your console applications. You can create a menu from files in a folder, or create a selector menu, in which the user chooses an option and the option is returned in the function.

## Examples

### Simple menu

Here is an example of how to create a menu with pymenu:

```python
from pymenu import Menu

menu = Menu('Menu title')
menu.add_option("Option 1", lambda: print("Option 1"))
menu.add_option("Option 2", lambda: print("Option 2"))
menu.add_option("Option 3", lambda: print("Option 3"))
menu.show()
```

### Menu with submenus

Here is an example of how to create a menu with submenus using pymenu:

```python
from pymenu import Menu

menu = Menu('Menu title')
menu.add_option("Option 1", lambda: print("Option 1"))
menu.add_option("Option 2", lambda: print("Option 2"))
menu.add_option("Option 3", lambda: print("Option 3"))

submenu = Menu('Submenu title')
submenu.add_option("Suboption 1", lambda: print("Suboption 1"))
submenu.add_option("Suboption 2", lambda: print("Suboption 2"))
submenu.add_option("Suboption 3", lambda: print("Suboption 3"))

menu.add_option("Submenu", submenu)
menu.show()
```

### Automatic menu of a folder

Here's an example of how to automatically create a menu from a folder with pymenu:

```python
from pymenu import auto_menu

menu = auto_menu.create_menu_from_directory('directory')
menu.add_option('Exit', exit)
menu.show()
```

### Selector menu

Here is an example of how to create a selector menu with pymenu:

```python
from pymenu import select_menu

options = ['Option 1', 'Option 2', 'Option 3']
selected_option = select_menu.create_select_menu(options, 'Select an option')
```