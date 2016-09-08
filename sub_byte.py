import sbox
from state import *


def sub_bytes(state):
    for x in range(0, 4):
        for y in range(0, 4):
            state.set(x, y, sub_bytes_cell(state.get(x, y)))


def sub_bytes_cell(block):
    block_hex = str(hex(block))

    # remove the '0x' from the hex block string
    block_hex = block_hex[2:]

    # if the first element of the block is a 0 then block_hex will reduce to only one element
    if len(block_hex) == 1:
        x_el = 0
        y_el = block_hex[0]
    else:
        x_el = block_hex[0]
        y_el = block_hex[1]

    new_block = sbox.get(int(str(x_el), 16), int(str(y_el), 16))
    return new_block


def main():
    state = State('193de3bea0f4e22b9ac68d2ae9f84808')
    state.pretty_print()
    print()

    sub_bytes(state)
    state.pretty_print()


main()
