def xor_two_str(str1, str2):
    string1 = int(str1, base=16)
    string2 = int(str2, base=16)
    return format(string1 ^ string2, 'x')


print(xor_two_str('1c0111001f010100061a024b53535009181c', '686974207468652062756c6c277320657965'))
