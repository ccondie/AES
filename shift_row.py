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


def main():
    state = State('d42711aee0bf98f1b8b45de51e415230')
    state.pretty_print()
    print()

    shift_rows(state)
    state.pretty_print()


main()
