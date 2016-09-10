from sbox import *
from mix_column import *
from inv_mix_column import *
from sub_byte import *
from inv_sub_byte import *
from shift_row import *
from inv_shift_row import *
from state import *
from key_handler import *
from add_round_key import *


def encrypt(plain_text, key_text):
    state = State(plain_text)
    key = KeyHandler(key_text)

    print('round[ 0].input\t\t', end='')
    state.raw_print()

    print('round[ 0].k_sch\t\t', end='')
    key.print_next_round()
    add_round_key(state, key.next_round())

    r = 1
    for x in range(1, key.nr):
        print('round[' + '{:>2}'.format(r) + '].start\t\t', end='')
        state.raw_print()

        sub_bytes(state)
        print('round[' + '{:>2}'.format(r) + '].s_byt\t\t', end='')
        state.raw_print()

        shift_rows(state)
        print('round[' + '{:>2}'.format(r) + '].s_row\t\t', end='')
        state.raw_print()

        mix_columns(state)
        print('round[' + '{:>2}'.format(r) + '].m_col\t\t', end='')
        state.raw_print()

        print('round[' + '{:>2}'.format(r) + '].k_sch\t\t', end='')
        key.print_next_round()
        add_round_key(state, key.next_round())

        r += 1

    print('round[' + '{:>2}'.format(r) + '].start\t\t', end='')
    state.raw_print()

    sub_bytes(state)
    print('round[' + '{:>2}'.format(r) + '].s_byt\t\t', end='')
    state.raw_print()

    shift_rows(state)
    print('round[' + '{:>2}'.format(r) + '].s_row\t\t', end='')
    state.raw_print()

    print('round[' + '{:>2}'.format(r) + '].k_sch\t\t', end='')
    key.print_next_round()
    add_round_key(state, key.next_round())

    print('round[' + '{:>2}'.format(r) + '].output\t', end='')
    state.raw_print()

    return state.tostring_raw()


def decrypt(cipher_text, key_text):
    state = State(cipher_text)
    key = KeyHandler(key_text)

    print('round[ 0].input\t\t', end='')
    state.raw_print()

    print('round[ 0].k_sch\t\t', end='')
    key.print_inv_next_round()
    add_round_key(state, key.inv_next_round())

    r = 1
    for x in range(1, key.nr):
        print('round[' + '{:>2}'.format(r) + '].istart\t', end='')
        state.raw_print()

        inv_shift_rows(state)
        print('round[' + '{:>2}'.format(r) + '].is_row\t', end='')
        state.raw_print()

        inv_sub_bytes(state)
        print('round[' + '{:>2}'.format(r) + '].is_byt\t', end='')
        state.raw_print()

        print('round[' + '{:>2}'.format(r) + '].ik_sch\t', end='')
        key.print_inv_next_round()

        add_round_key(state, key.inv_next_round())
        print('round[' + '{:>2}'.format(r) + '].ik_add\t', end='')
        state.raw_print()

        inv_mix_columns(state)

        r += 1

    print('round[' + '{:>2}'.format(r) + '].istart\t', end='')
    state.raw_print()

    inv_shift_rows(state)
    print('round[' + '{:>2}'.format(r) + '].is_row\t', end='')
    state.raw_print()

    inv_sub_bytes(state)
    print('round[' + '{:>2}'.format(r) + '].is_byt\t', end='')
    state.raw_print()

    print('round[' + '{:>2}'.format(r) + '].ik_sch\t', end='')
    key.print_inv_next_round()
    add_round_key(state, key.inv_next_round())

    print('round[' + '{:>2}'.format(r) + '].output\t', end='')
    state.raw_print()

    return state.tostring_raw()


def main():
    plain_text = '00112233445566778899aabbccddeeff'
    key_text = '000102030405060708090a0b0c0d0e0f101112131415161718191a1b1c1d1e1f'

    cipher_text = encrypt(plain_text, key_text)
    print()
    decrypt(cipher_text, key_text)


main()
