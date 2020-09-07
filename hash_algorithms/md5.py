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
    """
    This function calculates the MD5 hash value of the message provided.

    Args:
        message: The string that needs to be processed.

    Returns: The 128-bit hash value of the message.

    """
    if not isinstance(message, str):
        raise ValueError("Message provided must be a string.")

    k: List[int] = [math.floor(2 ** WORD_SIZE * abs(math.sin(i + 1))) for i in range(LENGTH_SIZE)]
    h: Tuple[int, int, int, int] = (0x67452301, 0xefcdab89, 0x98badcfe, 0x10325476)

    # Converting string into bit-string in little endian format.
    bit_string: str = char_big_to_little_endian(message_bit_padding(message))
    bit_string += bin(len(message) * CHAR_SIZE)[2:].zfill(LENGTH_SIZE)[::-1]

    # Create chunks to process.
    chunks: List[str] = [bit_string[i:i + CHUNK_SIZE] for i in range(0, len(bit_string), CHUNK_SIZE)]
    for chunk in chunks:
        # Each chunk is broken into 16 32-bit values called 'words'.
        words: List[int] = [int(chunk[i:i + WORD_SIZE][::-1], 2) for i in range(0, len(chunk), WORD_SIZE)]

        # Bitwise operations are carried out to process each chunk.
        a, b, c, d = h
        for i in range(LENGTH_SIZE):
            # Logical functions and s values are used to process the h values.
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

            # The variables are assigned partially calculated hask of the chunk after every iteration.
            temp: int = (f + a + k[i] + words[g]) & TRIMMING_VALUE
            a, b, c, d = d, (b + left_rotate(temp, s[i % 4])) & TRIMMING_VALUE, b, c

        # The result of the chunk’s hash is stored to the overall hash value of all chunks.
        h = ((h[0] + a) & TRIMMING_VALUE,
             (h[1] + b) & TRIMMING_VALUE,
             (h[2] + c) & TRIMMING_VALUE,
             (h[3] + d) & TRIMMING_VALUE)

    # The result of the chunk’s hash is then converted into its big endian format.
    h = (int_little_to_big_endian(h[0]),
         int_little_to_big_endian(h[1]),
         int_little_to_big_endian(h[2]),
         int_little_to_big_endian(h[3]))

    # The total hashed values have their hex values appeneded to each other and returned as a hex-string.
    return f"{(h[0] << 96 | h[1] << 64 | h[2] << 32 | h[3]):02x}"
