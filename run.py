from sbox import *
from mix_column import *
from sub_byte import *
from state import *


def main():
    plain_text = 'd4bf5d30e0b452aeb84111f11e2798e5'
    state = State(plain_text)

    state.pretty_print()
    print()

    mix_columns(state)
    state.pretty_print()


main()
