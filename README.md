# dtm
A simple implementation of a One-Tape Deterministic Turing Machine.

## Usage
```python
# Import the machine and the base states
from DTM import DTM, State

# Optionally extend the states
from enum import Enum, auto
class Extended(Enum):
    MOVE = auto()
    # ...

# Define the rules and the input
rules = {
    (State.START, "*"): (Extended.MOVE, "*", -1),
    (Extended.MOVE, "H"): (State.ACCEPT, "h", +1),
    (State.ANY, "*"): (State.REJECT, "*", +1),
}
input = "Hello, everyone!"

# Create the DTM and pass the input
dtm = DTM.from_input(input)

# Run the DTM with the rules
dtm.run(rules)

# Print the DTM tape contents as list
print(dtm) # ['H', 'e', 'l', 'l', 'o', ',', ' ', 'e', 'v', 'e', 'r', 'y', 'o', 'n', 'e', '!']

# Print the halting configuration
print(dtm.config) # (<State.ACCEPT: 3>, "['h', 'e', 'l', 'l', 'o', ',', ' ', 'e', 'v', 'e', 'r', 'y', 'o', 'n', 'e', '!']", 1)
```
