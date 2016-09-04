import sbox


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


def main():
    state = [
        [0x19, 0xa0, 0x9a, 0xe9],
        [0x3d, 0xf4, 0xc6, 0xf8],
        [0xe3, 0xe2, 0x8d, 0x48],
        [0xbe, 0x2b, 0x2a, 0x08]
    ]

    pretty_print_state(state)
    shift_rows(state)

    print()
    pretty_print_state(state)


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

---AddRoundKeye : DIFFICULTY ??? (How to get roundKey?)
XOR each element of each column 0-3 with each element of each column 0-3 of the RoundKey





? KeyExpansion ?


"""
