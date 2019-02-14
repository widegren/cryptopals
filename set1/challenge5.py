KEY = b"ICE"
MESSAGE = b"""Burning 'em, if you ain't quick and nimble \nI go crazy when I
    hear a cymbal"""


def repeating_key_xor(message_bytes, key_bytes):
    output_bytes = b''
    index = 0
    for byte in message_bytes:
        output_bytes += bytes([byte ^ key_bytes[index]])
        index = (index + 1) % 3
    return output_bytes


def main():
    ciphertext = repeating_key_xor(MESSAGE, KEY)

    print(ciphertext.hex())


if __name__ == "__main__":
    main()
