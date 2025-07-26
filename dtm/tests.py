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
                dtm = DTM(input)
                dtm.run(rules)
                self.assertEqual(dtm.tape, expected)

    # L = { a^n^2 | n natural number }
    # ...for simplicity only L = {1, 4, 9}
    def test_perfect_square(self):
        class Extended(Enum):
            SUB10 = auto()
            SUB30 = auto()
            SUB31 = auto()
            SUB32 = auto()
            SUB50 = auto()
            SUB51 = auto()
            SUB52 = auto()
            SUB53 = auto()
            SUB54 = auto()
            REST = auto()

        test_cases = [
            ("", State.REJECT),
            ("b", State.REJECT),
            ("a", State.ACCEPT),
            ("aa", State.REJECT),
            ("aaa", State.REJECT),
            ("aaaa", State.ACCEPT),
            ("aaaaa", State.REJECT),
            ("aaaaaa", State.REJECT),
            ("aaaaaaa", State.REJECT),
            ("aaaaaaaa", State.REJECT),
            ("aaaaaaaaa", State.ACCEPT),
            ("aaaaaaaaaa", State.REJECT),
            ("aaaaaaaaaaa", State.REJECT),
        ]
        rules = {
            (State.START, "a"): (Extended.SUB10, "a", -1),
            (State.START, "*"): (State.REJECT, "*", +1),  # for empty of non 'a'
            (Extended.SUB10, "a"): (Extended.SUB30, "x", +1),
            (Extended.SUB10, "*"): (State.REJECT, "*", +1),
            (Extended.SUB30, "a"): (Extended.SUB31, "x", +1),
            (Extended.SUB30, ""): (State.ACCEPT, "", +1),
            (Extended.SUB30, "*"): (State.REJECT, "*", +1),
            (Extended.SUB31, "a"): (Extended.SUB32, "x", +1),
            (Extended.SUB31, "*"): (State.REJECT, "*", +1),
            (Extended.SUB32, "a"): (Extended.SUB50, "x", +1),
            (Extended.SUB32, "*"): (State.REJECT, "*", +1),
            (Extended.SUB50, "a"): (Extended.SUB51, "x", +1),
            (Extended.SUB50, ""): (State.ACCEPT, "", +1),
            (Extended.SUB50, "*"): (State.REJECT, "*", +1),
            (Extended.SUB51, "a"): (Extended.SUB52, "x", +1),
            (Extended.SUB51, "*"): (State.REJECT, "*", +1),
            (Extended.SUB52, "a"): (Extended.SUB53, "x", +1),
            (Extended.SUB52, "*"): (State.REJECT, "*", +1),
            (Extended.SUB53, "a"): (Extended.SUB54, "x", +1),
            (Extended.SUB53, "*"): (State.REJECT, "*", +1),
            (Extended.SUB54, "a"): (Extended.REST, "x", +1),
            (Extended.SUB54, "*"): (State.REJECT, "x", +1),
            (Extended.REST, ""): (State.ACCEPT, "", +1),
            (Extended.REST, "*"): (State.REJECT, "*", +1),
        }
        for input, expected in test_cases:
            with self.subTest(input=input, expected=expected):
                dtm = DTM(input)
                dtm.run(rules)
                state, cell, direction = dtm.config
                self.assertEqual(state, expected)

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
                dtm = DTM(input)
                dtm.run(rules)
                state, _, _ = dtm.config
                self.assertEqual(state, expected)


if __name__ == "__main__":
    unittest.main()
