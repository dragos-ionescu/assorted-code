from State import State


class KTM:
    """
    Implementation of a k-tape deterministic Turing machine (DTM)
    with the 'stay' command and wildcard support.
    """

    def __init__(self, input: str = "", tapes: int = 1) -> None:
        if tapes < 1:
            raise ValueError("A Turing machine must have at least one tape.")
        self.tapes = [list(input)] + [[] for _ in range(tapes - 1)]
        self.heads = [0 for _ in range(tapes)]
        self.state = State.START

    def _ensure_tape_length(self, tape: int) -> None:
        while self.heads[tape] >= len(self.tapes[tape]):
            self.tapes[tape].append("")

    def get_cell(self, tape: int) -> str:
        if tape >= len(self.tapes):
            raise ValueError(f"Tape with index {tape} doesn't exist")
        self._ensure_tape_length(tape)
        return self.tapes[tape][self.heads[tape]]

    def set_cell(self, tape: int, value: str) -> None:
        if tape >= len(self.tapes):
            raise ValueError(f"Tape with index {tape} doesn't exist")
        self._ensure_tape_length(tape)
        self.tapes[tape][self.heads[tape]] = value

    def transition(
        self, rules: dict[tuple[State, list[str]], tuple[State, list[str], list[int]]]
    ) -> bool:
        if self.state in {State.ACCEPT, State.REJECT}:
            return False

        for (desired_state, desired_contents), (
            new_state,
            new_contents,
            directions,
        ) in rules.items():
            if (
                len(desired_contents) != len(self.tapes)
                or len(new_contents) != len(self.tapes)
                or len(directions) != len(self.tapes)
            ):
                raise ValueError("Rule lengths must match number of tapes")

            for direction in directions:
                if direction not in {-1, 0, 1}:
                    raise ValueError("Head directions must be -1, 0, or +1")

            if desired_state == State.ANY or self.state == desired_state:
                if all(
                    desired_contents[i] == "*" or desired_contents[i] == self.get_cell(i)
                    for i in range(len(self.tapes))
                ):
                    for i in range(len(self.tapes)):
                        if new_contents[i] != "*":
                            self.set_cell(i, new_contents[i])

                    for i in range(len(self.tapes)):
                        self.heads[i] = max(0, self.heads[i] + directions[i])

                    self.state = new_state
                    return True

        return False

    def run(self, rules: dict[tuple, tuple]) -> None:
        try:
            while self.transition(rules):
                pass
        except ValueError as ex:
            print(f"Turing machine error: {ex}")

    @property
    def config(self) -> tuple[State, list[list[str]], list[int]]:
        return (self.state, self.tapes, self.heads)

    def __repr__(self) -> str:
        reprs = []
        for i, (tape, head) in enumerate(zip(self.tapes, self.heads)):
            tape_str = "".join(c if c else "_" for c in tape)
            pointer_line = " " * head + "^"
            reprs.append(f"Tape {i}: {tape_str}\n        {pointer_line}")
        return f"State: {self.state.name}\n" + "\n".join(reprs)
