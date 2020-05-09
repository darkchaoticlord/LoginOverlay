from typing import List, Tuple
from hash_algorithms.hash_utils import (
    left_rotate,
    message_bit_padding,
    TRIMMING_VALUE,
    CHAR_SIZE,
    CHUNK_SIZE,
    LENGTH_SIZE,
    TOTAL_WORDS,
    TOTAL_ITERATIONS,
    WORD_SIZE
)


def sha1(message: str) -> str:
    """
    This function calculates the SHA-1 hash value of the message provided.

    Args:
        message: The string that needs to be processed.

    Returns: The 160-bit hash value of the message.

    """
    h: Tuple[int, int, int, int, int] = (0x67452301, 0xEFCDAB89, 0x98BADCFE, 0x10325476, 0xC3D2E1F0)

    # Converting string into bit-string
    bit_string: str = message_bit_padding(message)
    bit_string += bin(len(message) * CHAR_SIZE)[2:].zfill(LENGTH_SIZE)

    # Create chunks to process
    chunks: List[str] = [bit_string[i:i + CHUNK_SIZE] for i in range(0, len(bit_string), CHUNK_SIZE)]
    for chunk in chunks:
        # Each chunk is broken into 16 32-bit values called 'words'
        words: List[int] = [int(chunk[i:i + WORD_SIZE], 2) for i in range(0, len(chunk), WORD_SIZE)] + \
                           [0] * (TOTAL_ITERATIONS - TOTAL_WORDS)

        # First 16 words are used to calculate the next 64 words (total 80 words).
        for i in range(TOTAL_WORDS, TOTAL_ITERATIONS):
            words[i] = left_rotate(words[i - 3] ^ words[i - 8] ^ words[i - 14] ^ words[i - 16], 1)

        # Each calculated word is used to process the h values
        a, b, c, d, e = h
        for i in range(TOTAL_ITERATIONS):
            # Logical functions and k values are used to process the h values.
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

            # The variables are assigned partially calculated hask of the chunk after every iteration.
            a, b, c, d, e = (left_rotate(a, 5) + f + e + k + words[i]) & TRIMMING_VALUE, a, left_rotate(b, 30), c, d

        # The result of the chunk’s hash is stored to the overall hash value of all chunks
        h = ((h[0] + a) & TRIMMING_VALUE,
             (h[1] + b) & TRIMMING_VALUE,
             (h[2] + c) & TRIMMING_VALUE,
             (h[3] + d) & TRIMMING_VALUE,
             (h[4] + e) & TRIMMING_VALUE)

    # The total hashed values have their hex values appeneded to each other and returned as a hex-string.
    return f"{(h[0] << 128 | h[1] << 96 | h[2] << 64 | h[3] << 32 | h[4]):02x}"


# if __name__ == '__main__':
#     # Testing the hashing algorithm by running it with example values.
#
#     # Testing out SHA-1 hashing algorithm to see if it works.
#     print(sha1("The quick brown fox jumps over the lazy dog"))  # Answer: 2fd4e1c67a2d28fced849ee1bb76e7391b93eb12
#     print(sha1("abc"))  # Answer: a9993e364706816aba3e25717850c26c9cd0d89d
