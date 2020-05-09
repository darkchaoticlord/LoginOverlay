from typing import List, Tuple
from hash_algorithms.hash_utils import (
    left_rotate,
    message_bit_padding,
    char_big_to_little_endian,
    int_little_to_big_endian,
    CHAR_SIZE,
    CHUNK_SIZE,
    LENGTH_SIZE,
    TOTAL_WORDS,
    TRIMMING_VALUE,
    WORD_SIZE
)
import math


def md5(message: str) -> str:
    k: List[int] = [math.floor(2 ** WORD_SIZE * abs(math.sin(i + 1))) for i in range(LENGTH_SIZE)]
    h: Tuple[int, int, int, int] = (0x67452301, 0xefcdab89, 0x98badcfe, 0x10325476)

    bit_string: str = char_big_to_little_endian(message_bit_padding(message))
    bit_string += bin(len(message) * CHAR_SIZE)[2:].zfill(LENGTH_SIZE)[::-1]

    chunks: List[str] = [bit_string[i:i + CHUNK_SIZE] for i in range(0, len(bit_string), CHUNK_SIZE)]
    # print(chunks)
    for chunk in chunks:
        words: List[int] = [int(chunk[i:i + WORD_SIZE][::-1], 2) for i in range(0, len(chunk), WORD_SIZE)]

        a, b, c, d = h
        for i in range(LENGTH_SIZE):
            if 0 <= i <= 15:
                f: int = (b & c) | (~b & d)
                g: int = i
                s: List[int] = [7, 12, 17, 22]
            elif 16 <= i <= 31:
                f: int = (d & b) | (~d & c)
                g: int = (5 * i + 1) % TOTAL_WORDS
                s: List[int] = [5, 9, 14, 20]
            elif 32 <= i <= 47:
                f: int = b ^ c ^ d
                g: int = (3 * i + 5) % TOTAL_WORDS
                s: List[int] = [4, 11, 16, 23]
            else:
                f: int = c ^ (b | ~d)
                g: int = (7 * i) % TOTAL_WORDS
                s: List[int] = [6, 10, 15, 21]

            temp: int = (f + a + k[i] + words[g]) & TRIMMING_VALUE
            a, b, c, d = d, (b + left_rotate(temp, s[i % 4])) & TRIMMING_VALUE, b, c

        h = ((h[0] + a) & TRIMMING_VALUE,
             (h[1] + b) & TRIMMING_VALUE,
             (h[2] + c) & TRIMMING_VALUE,
             (h[3] + d) & TRIMMING_VALUE)

    h = (int_little_to_big_endian(h[0]),
         int_little_to_big_endian(h[1]),
         int_little_to_big_endian(h[2]),
         int_little_to_big_endian(h[3]))

    return f"{(h[0] << 96 | h[1] << 64 | h[2] << 32 | h[3]):02x}"


# if __name__ == '__main__':
#     # Testing the hashing algorithm by running it with example values.
#
#     # Testing out MD5 hashing algorithm to see if it works.
#     print(md5("The quick brown fox jumps over the lazy dog"))  # Answer: 9e107d9d372bb6826bd81d3542a419d6
#     print(md5("abc"))  # Answer: 900150983cd24fb0d6963f7d28e17f72
