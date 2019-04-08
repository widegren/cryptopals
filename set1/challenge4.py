from binascii import unhexlify
from challenge3 import bruteforce_xor_single_char, get_score

if __name__ == "__main__":
    solutions = []
    for line in open("challenge4-data.txt", "r"):
        try:
            solution = bruteforce_xor_single_char(unhexlify(line.strip()))
            b = bytearray()
            b.extend(map(ord, solution))
            score = get_score(b)
            solutions.append((solution, score))
        except:
            pass

    print(sorted(solutions, key=lambda result: result[1], reverse=True)[0][0].strip())
