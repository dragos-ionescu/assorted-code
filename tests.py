from enum import Enum, auto
from DTM import DTM, State
import unittest


class DTMTests(unittest.TestCase):
    def test_simple_copy(self):
        test_cases = [
            ("Hello, World!", list("Hello, World!")),
            ("", list("")),
            (" ", list(" ")),
        ]
        rules = {
            (State.START, "*"): (State.ACCEPT, "*", +1),
            (State.ANY, "*"): (State.REJECT, "*", +1),
        }
        for input, expected in test_cases:
            with self.subTest(input=input, expected=expected):
                dtm = DTM.from_input(input)
                dtm.run(rules)
                self.assertEqual(dtm.tape, expected)

    # L = { w#w | w in {0, 1}* }
    def test_two_strings_equal(self):
        class Extended(Enum):
            MOVE0 = auto()
            MOVE1 = auto()
            COMP0 = auto()
            COMP1 = auto()
            BACK_FIRST = auto()
            BACK = auto()
            AGAIN = auto()
            CHECK_END = auto()

        test_cases = [
            ("00#00", State.ACCEPT),
            ("010#010", State.ACCEPT),
            ("11#", State.REJECT),
            ("#", State.ACCEPT),
            ("", State.REJECT),
        ]
        rules = {
            (State.START, ""): (State.REJECT, "", +1),
            (State.START, "#"): (Extended.CHECK_END, "#", +1),
            (State.START, "0"): (Extended.MOVE0, "X", +1),
            (State.START, "1"): (Extended.MOVE1, "X", +1),
            (Extended.MOVE0, "0"): (Extended.MOVE0, "0", +1),
            (Extended.MOVE0, "1"): (Extended.MOVE0, "1", +1),
            (Extended.MOVE0, "#"): (Extended.COMP0, "#", +1),
            (Extended.MOVE1, "0"): (Extended.MOVE1, "0", +1),
            (Extended.MOVE1, "1"): (Extended.MOVE1, "1", +1),
            (Extended.MOVE1, "#"): (Extended.COMP1, "#", +1),
            (Extended.COMP0, "X"): (Extended.COMP0, "X", +1),
            (Extended.COMP0, "0"): (Extended.BACK_FIRST, "X", -1),
            (Extended.COMP0, "1"): (State.REJECT, "1", +1),
            (Extended.COMP0, ""): (State.REJECT, "", +1),
            (Extended.COMP1, "X"): (Extended.COMP1, "X", +1),
            (Extended.COMP1, "1"): (Extended.BACK_FIRST, "X", -1),
            (Extended.COMP1, "0"): (State.REJECT, "0", +1),
            (Extended.COMP1, ""): (State.REJECT, "", +1),
            (Extended.BACK_FIRST, "0"): (Extended.BACK_FIRST, "0", -1),
            (Extended.BACK_FIRST, "1"): (Extended.BACK_FIRST, "1", -1),
            (Extended.BACK_FIRST, "X"): (Extended.BACK_FIRST, "X", -1),
            (Extended.BACK_FIRST, "#"): (Extended.BACK, "#", -1),
            (Extended.BACK, "0"): (Extended.BACK, "0", -1),
            (Extended.BACK, "1"): (Extended.BACK, "1", -1),
            (Extended.BACK, "X"): (Extended.AGAIN, "X", +1),
            (Extended.AGAIN, "0"): (Extended.MOVE0, "X", +1),
            (Extended.AGAIN, "1"): (Extended.MOVE1, "X", +1),
            (Extended.AGAIN, "#"): (Extended.CHECK_END, "#", +1),
            (Extended.CHECK_END, "X"): (Extended.CHECK_END, "X", +1),
            (Extended.CHECK_END, ""): (State.ACCEPT, "", +1),
            (Extended.CHECK_END, "0"): (State.REJECT, "0", +1),
            (Extended.CHECK_END, "1"): (State.REJECT, "1", +1),
        }
        for input, expected in test_cases:
            with self.subTest(input=input, expected=expected):
                dtm = DTM.from_input(input)
                dtm.run(rules)
                state, _, _ = dtm.config
                self.assertEqual(state, expected)


if __name__ == "__main__":
    unittest.main()
