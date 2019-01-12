from binascii import unhexlify

CHAR_FREQUENCY = {
    'a': 0.0651738, 'b': 0.0124248, 'c': 0.0217339, 'd': 0.0349835,
    'e': 0.1041442, 'f': 0.0197881, 'g': 0.0158610, 'h': 0.0492888,
    'i': 0.0558094, 'j': 0.0009033, 'k': 0.0050529, 'l': 0.0331490,
    'm': 0.0202124, 'n': 0.0564513, 'o': 0.0596302, 'p': 0.0137645,
    'q': 0.0008606, 'r': 0.0497563, 's': 0.0515760, 't': 0.0729357,
    'u': 0.0225134, 'v': 0.0082903, 'w': 0.0171272, 'x': 0.0013692,
    'y': 0.0145984, 'z': 0.0007836, ' ': 0.1918182
}


def get_score(input_string):
    score = 0
    for char in input_string:
        char = chr(char)
        if char in CHAR_FREQUENCY:
            score += CHAR_FREQUENCY[char]
    return score


def xor(byte_str1, byte_str2):
    assert len(byte_str1) == len(byte_str2)

    return bytearray([b1 ^ b2 for (b1, b2)
                      in zip(byte_str1, byte_str2)])


def single_char_xor(buff, char):
    return xor(buff, bytearray([ord(char)] * len(buff)))


def best(input_list, key):
    return sorted(input_list, key=key, reverse=True)[0]


def bruteforce_xor_single_char(input_string):
    results = []
    for poss_key in [chr(i) for i in range(256)]:
        guess = single_char_xor(input_string, poss_key)
        score = get_score(guess)
        if score > .050:
            results.append((score, poss_key, guess))

    return best(results, lambda result: result[0])[2].decode("utf-8")


if __name__ == "__main__":
    INPUT = unhexlify('1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736')
    print(bruteforce_xor_single_char(INPUT))
