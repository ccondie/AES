def word_to_num(word):
    temp_array = ['0x']
    for el in word:
        temp_array.append(format(el, '02x'))
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
