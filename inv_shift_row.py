from state import *


def inv_shift_rows(state):
    for x in range(0, 4):
        for y in range(0, x):
            state.set_row(x, inv_shift_row(state.get_row(x)))


def inv_shift_row(row):
    to_shift = row[3]
    del row[3]
    row.insert(0, to_shift)
    return row
