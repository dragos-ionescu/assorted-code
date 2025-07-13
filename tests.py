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


if __name__ == "__main__":
    unittest.main()
