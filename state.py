def build_state(plaintext_32hex):
    plaintext_str = str(plaintext_32hex)
    final_state = []

    for i in range(0, len(plaintext_str), 2):
        add_this = '0x' + plaintext_str[i:i + 2]
        final_state.append(add_this)

    return final_state


class State(object):
    def __init__(self, plaintext_32hex):
        self.state = build_state(plaintext_32hex)

    def get(self, x, y):
        return self.state[y * 4 + x]

    def set(self, x, y, val):
        self.state[y * 4 + x] = val

    def get_row(self, index):
        pass

    def get_column(self, index):
        return_me = []
        for x in range(0, 4):
            return_me.append(self.get(x, index))
        return return_me

    def pretty_print(self):
        for x in range(0, 4):
            for y in range(0, 4):
                print(self.get(x, y), end=' ')
            print()
