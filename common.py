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