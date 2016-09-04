import sbox


# block as hex number
def sub_bytes_2(block):
    pass


def sub_bytes(block):
    # s_box[x][y]
    block_hex = str(hex(block))

    # remove the '0x' from the hex block string
    block_hex = block_hex[2:]
    block_hex_len = len(block_hex)

    # if the first element of the block is a 0
    if block_hex_len == 1:
        x_el = 0
        y_el = block_hex[0]
    else:
        x_el = block_hex[0]
        y_el = block_hex[1]

    new_block = sbox.get(int(str(x_el), 16), int(str(y_el), 16))
    return new_block


def main():
    sub_test_hex = 0x08
    print(hex(sub_bytes(sub_test_hex)))


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

---AddRoundKeye : DIFFICULTY
XOR each element of each column 0-3 with each element of each column 0-3 of the RoundKey





? KeyExpansion ?


"""
