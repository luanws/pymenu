from typing import Dict

from readchar import key, readkey

key_dict: Dict[str, str] = {
    key.UP: "UP",
    key.DOWN: "DOWN",
    key.RIGHT: "RIGHT",
    key.LEFT: "LEFT",
    key.ENTER: "ENTER",
    key.BACKSPACE: "BACKSPACE"
}

def mapper(key: str) -> str:
    if key in key_dict:
        return key_dict[key]
    return key


def input_key() -> str:
    key = readkey()
    return mapper(key)
