def build_state(plaintext_32hex):
    plaintext_str = str(plaintext_32hex)
    final_state = []

    for i in range(0, len(plaintext_str), 2):
        add_this = plaintext_str[i:i + 2]
        final_state.append(int(add_this,16))

    return final_state


class State(object):
    def __init__(self, plaintext_32hex):
        self.state = build_state(plaintext_32hex)


    def get(self, x, y):
        return self.state[y * 4 + x]

    def set(self, x, y, val):
        self.state[y * 4 + x] = val

    def get_row(self, index):
        return_me = []
        for y in range(0, 4):
            return_me.append(self.get(index, y))
        return return_me

    def set_row(self, index, new_row):
        for y in range(0, 4):
            self.set(index, y, new_row[y])

    def get_column(self, index):
        return_me = []
        for x in range(0, 4):
            return_me.append(self.get(x, index))
        return return_me

    def set_column(self, index, new_column):
        for x in range(0, 4):
            self.set(x, index, new_column[x])

    def pretty_print(self):
        for x in range(0, 4):
            for y in range(0, 4):
                print(hex(self.get(x, y)), end=' ')
            print()

    def raw_print(self):
        for el in self.state:
            print(format(el,'02x'),end='')
        print()

    def length(self):
        return len(self.state)
