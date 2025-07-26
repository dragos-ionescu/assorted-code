from enum import Enum, auto


class State(Enum):
    START = auto()
    REJECT = auto()
    ACCEPT = auto()
    ANY = auto()
