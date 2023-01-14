import msvcrt


def get_numeric_input():
    input_str = ""
    while True:
        char = msvcrt.getch()
        if char.isdigit():
            input_str += char.decode()
            print(char.decode(), end='', flush=True)
        elif char in b'\r\n':  # Enter key pressed
            break
    return input_str
