import rcon
import copy
from state import *
from sub_byte import *
from common import *


def pre_process_key(key):
    """

    :param key: a string '0123456789abcdef'
    :return: two hex split of the string [0x01, 0x23, 0x45, 0x67, 0x89, 0xab, 0xcd, 0xef]
    """
    final_state = []

    for i in range(0, len(key), 2):
        add_this = key[i:i + 2]
        final_state.append(int(add_this, 16))

    return final_state


def build_schedule(key, nk, nr):
    """
    Nb: Number of columns (32-bit words) comprising the State, Nb = 4
    Nr: Number of rounds, Nr = 10, 12, 14

    :param nk: number of 32-bit [8bit x 4] words comprising the cipher key, Nk = 4, 6, 8
    :param key: [0xd4, 0xe1, 0x23, 0x9f, ...]
    :return: round_keys[
            [0a,fe,2d,e6,b2 ...],       each element is a round key
            [d4,eb,2c,d1,a3 ...]
        ]
    """
    nb = 4

    w = []
    temp = []
    i = 0

    while i < nk:
        w.append([key[4 * i], key[4 * i + 1], key[4 * i + 2], key[4 * i + 3]])
        i += 1

    i = nk

    while i < (nb * (nr + 1)):
        temp = copy.deepcopy(w[i - 1])
        if i % nk == 0:
            temp = rot_word(temp)
            temp = sub_word(temp)
            temp_num = word_to_num(temp)
            temp_num ^= rcon.get(int(i / nk))
            temp = num_to_word(temp_num)

        elif (nk > 6) and (i % nk == 4):
            temp = sub_word(temp)

        w.append(num_to_word(word_to_num(w[i - nk]) ^ word_to_num(temp)))

        i += 1
    return w


def sub_word(word):
    """
    :param word: [0xa0, 0x02, 0xc1, 0xf3]
    :return: [0xe0, 0x77, 0x78, 0x0d]
    """
    for x in range(0, len(word)):
        word[x] = sub_bytes_cell(word[x])
    return word


def rot_word(word):
    """
    :param word: [0xa0, 0x02, 0xc1, 0xf3]
    :return: [0x02, 0xc1, 0xf3, 0xa0]
    """
    temp = word[0]
    del word[0]
    word.append(temp)
    return word


class KeyHandler(object):
    def __init__(self, key):
        key = pre_process_key(key)
        nr_lookup = {4: 10, 6: 12, 8: 14}
        self.nk = int(len(key) / 4)
        self.nr = nr_lookup[self.nk]

        self.key = key
        self.key_schedule = build_schedule(key, self.nk, self.nr)

    def next_round(self):
        return_me = []
        for i in range(0, 4):
            return_me.append(self.key_schedule[0])
            del self.key_schedule[0]
        return return_me

    def inv_next_round(self):
        return_me = []
        for i in range(len(self.key_schedule) - 4, len(self.key_schedule)):
            return_me.append(self.key_schedule[i])
        for j in range(0, 4):
            del self.key_schedule[len(self.key_schedule) - 4]
        return return_me

    def print_inv_next_round(self):
        for i in range(len(self.key_schedule) - 4, len(self.key_schedule)):
            for j in range(0, 4):
                print(format(self.key_schedule[i][j], '02x'), end='')
        print()

    def print_next_round(self):
        for i in range(0, 4):
            for j in range(0, 4):
                print(format(self.key_schedule[i][j], '02x'), end='')
        print()
