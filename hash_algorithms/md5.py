from typing import List, Tuple
from .hash_utils import left_rotate, message_bit_padding, CHUNK_SIZE, LENGTH_SIZE, \
    TOTAL_WORDS, TRIMMING_VALUE, WORD_SIZE
import math


def md5(message: str) -> str:
    s: List[int] = [7, 12, 17, 22] * 4 + [5, 9, 14, 20] * 4 + [4, 11, 16, 23] * 4 + [6, 10, 15, 21] * 4
    # for i in range(0, 64, 16):
    #     print(s[i:i + 16])

    k: List[int] = [math.floor(2 ** WORD_SIZE * abs(math.sin(i + 1))) for i in range(LENGTH_SIZE)]
    # for i in range(0, 64, 4):
    #     print([hex(x) for x in k[i:i + 4]])

    h: Tuple[int, int, int, int] = (0x67452301, 0xefcdab89, 0x98badcfe, 0x10325476)

    bit_string: str = message_bit_padding(message)
    # print(len(bit_string))

    chunks: List[str] = [bit_string[i:i + CHUNK_SIZE] for i in range(0, len(bit_string), CHUNK_SIZE)]
    # print(chunks)
    for chunk in chunks:
        words: List[int] = [int(chunk[i:i + WORD_SIZE], 2) for i in range(0, len(chunk), WORD_SIZE)]

        a, b, c, d = h
        for i in range(LENGTH_SIZE):
            if 0 <= i <= 15:
                f = (b & c) | (~b & d)
                g = i
            elif 16 <= i <= 31:
                f = (d & b) | (~d & c)
                g = (5 * i + 1) % TOTAL_WORDS
            elif 32 <= i <= 47:
                f = b ^ c ^ d
                g = (3 * i + 5) % TOTAL_WORDS
            else:
                f = c ^ (b | ~d)
                g = (7 * i) % TOTAL_WORDS

            # print(str(g).zfill(2), f"{words[g]:032b}")
            f = (f + a + k[i] + words[g]) & TRIMMING_VALUE
            a = d
            d = c
            c = b
            b = (b + left_rotate(f, s[i])) & TRIMMING_VALUE
            # a, b, c, d = d, (b + left_rotate(f + a + k[i] + words[g], s[i])) & TRIMMING_VALUE, b, c

        h = ((h[0] + a) & TRIMMING_VALUE,
             (h[1] + b) & TRIMMING_VALUE,
             (h[2] + c) & TRIMMING_VALUE,
             (h[3] + d) & TRIMMING_VALUE)

    result: str = f"{(h[0] << 96 | h[1] << 64 | h[2] << 32 | h[3]):02x}"
    # result = "".join([hex(x)[2:] for x in h])
    return result


# if __name__ == '__main__':
#     # Testing the hashing algorithm by running it with example values.
#
#     # Testing out MD5 hashing algorithm to see if it works.
#     print(md5("The quick brown fox jumps over the lazy dog"))  # Answer: 9e107d9d372bb6826bd81d3542a419d6
#     print(md5("abc"))  # Answer: 900150983cd24fb0d6963f7d28e17f72
