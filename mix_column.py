from common import *


def mix_columns(state):
    for y in range(0, 4):
        state.set_column(y, mix_column(state.get_column(y)))


def mix_column(column):
    new_column = []

    el_one = ff_multi(0x02, column[0]) ^ ff_multi(0x03, column[1]) ^ column[2] ^ column[3]
    new_column.append(el_one)

    el_two = column[0] ^ ff_multi(0x02, column[1]) ^ ff_multi(0x03, column[2]) ^ column[3]
    new_column.append(el_two)

    el_three = column[0] ^ column[1] ^ ff_multi(0x02, column[2]) ^ ff_multi(0x03, column[3])
    new_column.append(el_three)

    el_four = ff_multi(0x03, column[0]) ^ column[1] ^ column[2] ^ ff_multi(0x02, column[3])
    new_column.append(el_four)

    return new_column
