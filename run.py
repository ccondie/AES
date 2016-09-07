import sbox


def build_state(plaintext_32hex):
    plaintext_str = str(plaintext_32hex)
    plaintext_8bit_split = [plaintext_str[i:i + 2] for i in range(0, len(plaintext_str), 2)]
    return plaintext_8bit_split


def pretty_print_state(state):
    for x in range(0, len(state)):
        for y in range(0, len(state[x])):
            print(str(hex(state[x][y]))[2:], end=' ')
        print()


def sub_bytes(state):
    for x in range(0, len(state)):
        for y in range(0, len(state[x])):
            state[x][y] = sub_bytes_cell(state[x][y])


def shift_rows(state):
    for x in range(0, len(state)):
        for y in range(0, x):
            shift_row(state[x])
        print()


def shift_row(row):
    to_shift = row[0]
    del row[0]
    row.append(to_shift)


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
    pass


def mix_column(column):
    pass


def ff_multi(byte_one, byte_two):
    pass


def x_time(byte):
    byte <<= 1                      # left shift the incoming byte
    byte_set = byte & 0b100000000   # check if the overflow bit is set
    if byte_set == 0b100000000:     # after the AND, the byte_set will be 0b100000000 if the overflow bit was set
        return byte ^ 0b100010111
    else:                           # or 0b000000000 if the overflow bit was not set
        return byte


def main():
    plaintxt = '02468ace13579bdf02468ace13579bdf'
    build_state(plaintxt)

    x_time(0b01111111)


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
