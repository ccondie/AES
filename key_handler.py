import rcon
import copy
from state import *
from sub_byte import *


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


def word_to_num(word):
    temp_array = ['0x']
    for el in word:
        temp_array.append(format(el,'02x'))
    send_this = ''.join(temp_array)
    return int(send_this, 16)


def num_to_word(num):
    as_hex = format(num, '08x')
    return_me = []
    for i in range(0, len(as_hex), 2):
        add_this = '0x' + as_hex[i:i + 2]
        return_me.append(int(add_this, 16))

    return return_me


def print_word_hex(word):
    print('[', end='')
    for el in word:
        print(hex(el), end=' ')
    print(']')


def build_schedule(key):
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
    nr_lookup = {4: 10, 6: 12, 8: 14}

    nk = int(len(key) / 4)
    nr = nr_lookup[nk]
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
        self.key = key
        self.key_schedule = build_schedule(key)


def main():
    key128bit = '2b7e151628aed2a6abf7158809cf4f3c'
    key192bit = '8e73b0f7da0e6452c810f32b809079e562f8ead2522c6b7b'
    key256bit = '603deb1015ca71be2b73aef0857d77811f352c073b6108d72d9810a30914dff4'

    index = 0
    for el in build_schedule(pre_process_key(key192bit)):
        for in_el in el:
            print(format(in_el, '02x'), end=' ')
        print()
        index += 1
        if (index % 4 == 0):
            print()


main()
