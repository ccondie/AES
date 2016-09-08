import rcon


def load_initial_key(key_text):
    key_text_str = str(key_text)
    final_key = []

    for i in range(0, len(key_text_str), 2):
        add_this = '0x' + key_text_str[i:i + 2]
        final_key.append(int(add_this, 16))

    return final_key


class KeyHandler(object):
    def __init__(self, key_text):
        self.key = load_initial_key(key_text)

    def get_round_key(self):
        pass
