import sbox
from state import State


def shift_rows(state):
    for x in range(0, len(state)):
        for y in range(0, x):
            shift_row(state[x])
        print()


def shift_row(row):
    to_shift = row[0]
    del row[0]
    row.append(to_shift)


def sub_bytes(state):
    for x in range(0, len(state)):
        for y in range(0, len(state[x])):
            state[x][y] = sub_bytes_cell(state[x][y])


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


def ff_multi(byte_one, byte_two):
    x_time_values = []
    final_xor_values = []

    # calculate and store the 8 xTime values for byte_one
    x_time_values.append(byte_one)
    for x in range(1, 8):
        x_time_values.append(x_time(x_time_values[x - 1]))

    byte_two_str = str(bin(byte_two))[2:]
    for x in range(0, len(byte_two_str)):
        bit = byte_two_str[len(byte_two_str) - 1 - x]
        if bit == '1':
            final_xor_values.append(x_time_values[x])

    result = 0b00000000
    for el in final_xor_values:
        result = result ^ el

    return result


def x_time(byte):
    byte <<= 1  # left shift the incoming byte
    byte_set = byte & 0b100000000  # check if the overflow bit is set
    if byte_set == 0b100000000:  # after the AND, the byte_set will be 0b100000000 if the overflow bit was set
        return byte ^ 0b100011011
    else:  # or 0b000000000 if the overflow bit was not set
        return byte


def main():
    # plaintxt = '02468ace13579bdf02468ace13579bdf'
    plaintxt = 'd4bf5d30e0b452aeb84111f11e2798e5'
    state = State(plaintxt)

    state.pretty_print()
    print()

    mix_columns(state)
    state.pretty_print()


main()

"""
---Initial Round
AddRoundKey

---Middle Rounds
1-SubBytes
2-ShiftRows
3-MixColumns
4-AddRoundKey

---Final Round
SubBytes
ShiftRows
AddRoundKey




---SubBytes : DIFFICULTY EASY
For each 8bit piece of the 128bit block
lookup x for first 4bits, and y for second 4 bits and replace with value from s-box

---ShiftRows : DIFFICULTY EASY
For each row 0-3
rotate first n bytes from front of row to back of row

---MixColumns : DIFFICULTY HARD
Something with Matrix Multiplication ...

---AddRoundKey : DIFFICULTY ??? (How to get roundKey?)
XOR each element of each column 0-3 with each element of each column 0-3 of the RoundKey





? KeyExpansion ?


"""
