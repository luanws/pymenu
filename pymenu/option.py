from typing import Callable


class Option:
    def __init__(self, name: str, call: Callable) -> None:
        self.name = name
        self.call = call

    def __str__(self) -> str:
        return self.name

    def __call__(self):
        self.call()
