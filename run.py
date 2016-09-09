from sbox import *
from mix_column import *
from sub_byte import *
from shift_row import *
from state import *
from key_handler import *
from add_round_key import *


def main():
    plain_text = '00112233445566778899aabbccddeeff'
    key_text = '000102030405060708090a0b0c0d0e0f'

    state = State(plain_text)
    key = KeyHandler(key_text)

    print('round[ 0].input\t', end='')
    state.raw_print()

    print('round[ 0].k_sch\t', end='')
    key.print_next_round()
    add_round_key(state, key.next_round())

    for r in range(1, 10):
        print('round[ ' + str(r) + '].start\t\t', end='')
        state.raw_print()

        sub_bytes(state)
        print('round[ ' + str(r) + '].s_byt\t\t', end='')
        state.raw_print()

        shift_rows(state)
        print('round[ ' + str(r) + '].s_row\t\t', end='')
        state.raw_print()

        mix_columns(state)
        print('round[ ' + str(r) + '].m_col\t\t', end='')
        state.raw_print()

        print('round[ ' + str(r) + '].k_sch\t\t', end='')
        key.print_next_round()
        add_round_key(state, key.next_round())

    print('round[10].start\t\t', end='')
    state.raw_print()

    sub_bytes(state)
    print('round[10].s_byt\t\t', end='')
    state.raw_print()

    shift_rows(state)
    print('round[10].s_row\t\t', end='')
    state.raw_print()

    print('round[10].k_sch\t\t', end='')
    key.print_next_round()
    add_round_key(state, key.next_round())

    print('round[10].output\t', end='')
    state.raw_print()


main()
