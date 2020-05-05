# Constants
TRIMMING_VALUE = 0xffffffff
CHUNK_SIZE = 512
LENGTH_SIZE = 64
WORD_SIZE = 32
TOTAL_WORDS = 16
CHAR_SIZE = 8
TOTAL_ITERATIONS = 80


def left_rotate(n: int, d: int) -> int:
    """
        Circular rotation of value 'n' by 'd' bits.

        Args:
            n: The value to be processed.
            d: The numbers of bits to rotate by.

        Returns: The value processed after being left rotated.

        """
    return ((n << d) | (n >> (WORD_SIZE - d))) & TRIMMING_VALUE
