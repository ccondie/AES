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
    byte <<= 1
    byte_set = byte & 0b100000000
    if byte_set == 0b100000000:
        return byte ^ 0b100011011
    else:
        return byte
