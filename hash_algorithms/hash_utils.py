from typing import List

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


def message_bit_padding(message: str) -> str:
    # Converting string into bit-string
    bit_string: str = ""
    for char in message:
        bit_string += bin(ord(char))[2:].zfill(CHAR_SIZE)

    # Padding the bit-string
    bit_string += "1" + "0" * (CHUNK_SIZE - LENGTH_SIZE - (len(bit_string) % CHUNK_SIZE) - 1)
    return bit_string


def char_big_to_little_endian(bit_string: str) -> str:
    result: str = ""
    for i in range(0, len(bit_string), CHAR_SIZE):
        result += bit_string[i: i + CHAR_SIZE][::-1]
    return result


def int_little_to_big_endian(int_value: int) -> int:
    bit_string: str = bin(int_value)[2:].zfill(WORD_SIZE)
    bit_string_list: List[str] = [bit_string[i: i + CHAR_SIZE] for i in range(0, len(bit_string), CHAR_SIZE)]
    return int("".join(bit_string_list[::-1]), 2)


# if __name__ == '__main__':
#     # Testing the hashing algorithm by running it with example values.
#
#     # Word examples.
#     value1 = '01010100011010000110010100100000'
#     value2 = '01110001011101010110100101100011'
#     value3 = '01101011001000000110001001110010'
#     print(bin(left_rotate(int(value1, 2), 6))[2:].zfill(32))
#
#     # Checking big to little endian conversion
#     value_big = "011000010110001001100011"
#     value_little = "100001100100011011000110"
#     print(char_big_to_little_endian(value_big) == value_little)
#
#     # Checking little to big endian conversion
#     int_value_little = 2555380112
#     int_value_big = 2416005272
#     print(int_little_to_big_endian(int_value_little) == int_value_big)
