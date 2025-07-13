from enum import Enum, auto


class State(Enum):
    START = auto()
    REJECT = auto()
    ACCEPT = auto()
    ANY = auto()


class DTM:
    def __init__(self, initial: list[str] = []) -> None:
        self.tape = initial
        self.tape_index = 0
        self.state = State.START

    @classmethod
    def from_input(cls, input: str) -> "DTM":
        return DTM(list(input))

    @property
    def cell(self) -> str:
        if self.tape_index >= len(self.tape):
            return ""
        return self.tape[self.tape_index]

    @cell.setter
    def cell(self, value: str) -> None:
        if self.tape_index >= len(self.tape):
            self.tape.append("")
        self.tape[self.tape_index] = value

    def transition(self, rules: dict[tuple, tuple]) -> bool:
        for (desired_state, desired_content), (new_state, new_cell, direction) in rules.items():
            if desired_state == State.ANY or self.state == desired_state:
                if desired_content == "*" or desired_content == self.cell:
                    if self.state in {State.ACCEPT, State.REJECT}:
                        return False
                    if direction not in {-1, +1}:
                        raise ValueError("direction can only be -1, +1")
                    if new_cell != "*":
                        self.cell = new_cell
                    self.state = new_state
                    self.tape_index = max(0, self.tape_index + direction)
                    return True
        return False

    def run(self, rules: dict[tuple, tuple]):
        try:
            while self.transition(rules):
                pass
        except ValueError as ex:
            print(f"Error: {ex}")

    @property
    def config(self) -> tuple:
        return (self.state, str(self), self.tape_index)

    def __repr__(self) -> str:
        return repr(self.tape)
