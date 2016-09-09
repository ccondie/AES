from state import *
from common import *


def add_round_key(state, round_key):
    for round_word_index in range(0, len(round_key)):
        column = state.get_column(round_word_index)
        column_num = word_to_num(column)
        round_word_num = word_to_num(round_key[round_word_index])

        new_column_num = column_num ^ round_word_num
        new_column = num_to_word(new_column_num)
        state.set_column(round_word_index, new_column)