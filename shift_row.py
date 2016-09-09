from state import *


def shift_rows(state):
    for x in range(0, 4):
        for y in range(0, x):
            # shift_row(state[x])
            state.set_row(x, shift_row(state.get_row(x)))


def shift_row(row):
    to_shift = row[0]
    del row[0]
    row.append(to_shift)
    return row
