# Define patterns for each letter (5 rows each)
I = [
    "XXXXX",
    "  X  ",
    "  X  ",
    "  X  ",
    "XXXXX"
]

M = [
    "X   X",
    "XX XX",
    "X X X",
    "X   X",
    "X   X"
]

R = [
    "XXXX ",
    "X   X",
    "XXXX ",
    "X  X ",
    "X   X"
]

A = [
    " XXX ",
    "X   X",
    "XXXXX",
    "X   X",
    "X   X"
]

N = [
    "X   X",
    "XX  X",
    "X X X",
    "X  XX",
    "X   X"
]

# Combine all letters in order
letters = [I, M, R, A, N]

# Print row by row
for row in range(5):
    for letter in letters:
        print(letter[row], end="   ")  # space between letters
    print()  # move to next line
