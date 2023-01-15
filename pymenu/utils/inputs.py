import msvcrt


def get_numeric_input() -> str:
    input_str: str = ''
    while True:
        char = msvcrt.getch()
        if char.isdigit():
            input_str += char.decode()
            print(char.decode(), end='', flush=True)
        elif char in b'\r\n':  # Enter key pressed
            break
        elif char in b'\x08':  # Backspace key pressed
            input_str = input_str[:-1]
            print('\b \b', end='', flush=True)
        elif char in b'\x03':  # Ctrl + C pressed
            raise KeyboardInterrupt
    return input_str
