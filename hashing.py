from typing import List, Tuple

# Constants
CHUNK_SIZE = 512
LENGTH_SIZE = 64
WORD_SIZE = 32
TOTAL_WORDS = 16
CHAR_SIZE = 8
TOTAL_ITERATIONS = 80


def _left_rotate(n: int, d: int) -> int:
    return ((n << d) | (n >> (WORD_SIZE - d))) & 0xffffffff


def sha1(message: str) -> str:
    h: Tuple[int, int, int, int, int] = (0x67452301, 0xEFCDAB89, 0x98BADCFE, 0x10325476, 0xC3D2E1F0)

    # Converting string into bit-string
    bit_string: str = ""
    for char in message:
        bit_string += bin(ord(char))[2:].zfill(CHAR_SIZE)

    # Padding the bit-string
    bit_string += "1" + "0" * (CHUNK_SIZE - LENGTH_SIZE - (len(bit_string) % CHUNK_SIZE) - 1)
    bit_string += bin(len(message) * CHAR_SIZE)[2:].zfill(LENGTH_SIZE)

    # Create chunks to process
    chunks = [bit_string[i:i + CHUNK_SIZE] for i in range(0, len(bit_string), CHUNK_SIZE)]
    for chunk in chunks:
        words = [int(chunk[i:i + WORD_SIZE], 2) for i in range(0, len(chunk), WORD_SIZE)] + \
                [0] * (TOTAL_ITERATIONS - TOTAL_WORDS)
        for i in range(TOTAL_WORDS, TOTAL_ITERATIONS):
            words[i] = _left_rotate(words[i - 3] ^ words[i - 8] ^ words[i - 14] ^ words[i - 16], 1)

        a, b, c, d, e = h
        for i in range(TOTAL_ITERATIONS):
            if 0 <= i <= 19:
                f = (b & c) | (~b & d)
                k = 0x5A827999
            elif 20 <= i <= 39:
                f = b ^ c ^ d
                k = 0x6ED9EBA1
            elif 40 <= i <= 59:
                f = (b & c) | (b & d) | (c & d)
                k = 0x8F1BBCDC
            else:
                f = b ^ c ^ d
                k = 0xCA62C1D6

            a, b, c, d, e = (_left_rotate(a, 5) + f + e + k + words[i]) & 0xffffffff, a, _left_rotate(b, 30), c, d

        h = ((h[0] + a) & 0xffffffff, (h[1] + b) & 0xffffffff, (h[2] + c) & 0xffffffff,
             (h[3] + d) & 0xffffffff, (h[4] + e) & 0xffffffff)

    return f"{(h[0] << 128 | h[1] << 96 | h[2] << 64 | h[3] << 32 | h[4]):02x}"


if __name__ == '__main__':
    # value1 = '01010100011010000110010100100000'
    # value2 = '01110001011101010110100101100011'
    # value3 = '01101011001000000110001001110010'
    # print(_or(value1, value2, value3))
    # print(bin(_left_rotate_bits(int(value1, 2), 6))[2:].zfill(32))
    # print(sha1("The quick brown fox jumps over the lazy dog. There is something I would like to talk about today."))
    print(sha1("abc"))
