from common import *


def inv_mix_columns(state):
    for y in range(0, 4):
        state.set_column(y, inv_mix_column(state.get_column(y)))


def inv_mix_column(column):
    new_column = []

    el_one = ff_multi(0x0e, column[0]) ^ ff_multi(0x0b, column[1]) ^ ff_multi(0x0d,column[2]) ^ ff_multi(0x09, column[3])
    new_column.append(el_one)

    el_two = ff_multi(0x09, column[0]) ^ ff_multi(0x0e, column[1]) ^ ff_multi(0x0b, column[2]) ^ ff_multi(0x0d,column[3])
    new_column.append(el_two)

    el_three = ff_multi(0x0d,column[0]) ^ ff_multi(0x09, column[1]) ^ ff_multi(0x0e, column[2]) ^ ff_multi(0x0b, column[3])
    new_column.append(el_three)

    el_four = ff_multi(0x0b, column[0]) ^ ff_multi(0x0d,column[1]) ^ ff_multi(0x09, column[2]) ^ ff_multi(0x0e, column[3])
    new_column.append(el_four)

    return new_column
