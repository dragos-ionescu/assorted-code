from State import State


class DTM:
    """
    Implementation of a one-tape deterministic Turing machine (DTM)
    with wildcard support.
    """

    def __init__(self, input: str = "") -> None:
        self.tape = list(input) if input else []
        self.head = 0
        self.state = State.START

    @property
    def cell(self) -> str:
        if self.head >= len(self.tape):
            self._extend_tape()
        return self.tape[self.head]

    @cell.setter
    def cell(self, value: str) -> None:
        if self.head >= len(self.tape):
            self._extend_tape()
        self.tape[self.head] = value

    def _extend_tape(self):
        while self.head >= len(self.tape):
            self.tape.append("")

    def transition(self, rules: dict[tuple[State, str], tuple[State, str, int]]) -> bool:
        if self.state in {State.ACCEPT, State.REJECT}:
            return False

        for (current_state, current_symbol), (new_state, new_symbol, direction) in rules.items():
            if direction not in {-1, 1}:
                raise ValueError("Direction must be -1 or 1")

            if current_state == State.ANY or self.state == current_state:
                if current_symbol == "*" or self.cell == current_symbol:
                    if new_symbol != "*":
                        self.cell = new_symbol
                    self.state = new_state
                    self.head = max(0, self.head + direction)
                    return True
        return False

    def run(self, rules: dict[tuple[State, str], tuple[State, str, int]]) -> None:
        try:
            while self.transition(rules):
                pass
        except ValueError as ex:
            print(f"Turing Machine Error: {ex}")

    @property
    def config(self) -> tuple[State, list[str], int]:
        return self.state, self.tape, self.head

    def __repr__(self) -> str:
        tape_str = "".join(c if c else "_" for c in self.tape)
        pointer_line = " " * self.head + "^"
        return f"State: {self.state.name}\nTape:  {tape_str}\n        {pointer_line}"
