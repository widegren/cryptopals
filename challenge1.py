#set 1 challenge 1
def hex_to_base64(str):
	return str.decode("hex").encode("base64")

print hex_to_base64('49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d')

#set 1 challenge 2
def xor_strings(xs, ys):
    return "".join(chr(ord(x) ^ ord(y)) for x, y in zip(xs, ys))

print xor_strings('1c0111001f010100061a024b53535009181c'.decode("hex"), '686974207468652062756c6c277320657965'.decode("hex")).encode("hex")
