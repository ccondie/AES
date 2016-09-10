import invsbox
from state import *


def inv_sub_bytes(state):
    for x in range(0, 4):
        for y in range(0, 4):
            state.set(x, y, inv_sub_bytes_cell(state.get(x, y)))


def inv_sub_bytes_cell(block):
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

    new_block = invsbox.get(int(str(x_el), 16), int(str(y_el), 16))
    return new_block
