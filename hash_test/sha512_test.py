from __future__ import annotations
from unittest import TestCase, main
from hash_algorithms.sha512 import sha512


class SHA512Testing(TestCase):

    def test_if_hashing_works(self: SHA512Testing) -> None:
        """
        Test Method that checks if the hashing algorithm works correctly
        for three different examples.

        Returns: None (void method)

        """
        self.assertEqual(sha512("The quick brown fox jumps over the lazy dog"),
                         "07e547d9586f6a73f73fbac0435ed76951218fb7d0c8d788a309d785436bbb642e93a252a954f23912547d1e8a3b"
                         "5ed6e1bfd7097821233fa0538f3db854fee6")
        self.assertTrue(sha512("The quick brown fox jumps over the lazy dog.") == "91ea1245f20d46ae9a037a989f54f1f790f"
                                                                                  "0a47607eeb8a14d12890cea77a1bbc6c7ed"
                                                                                  "9cf205e67b7f2b8fd4c7dfd3a7a8617e45f"
                                                                                  "3c463d481c7e586c39ac1ed")
        self.assertFalse(sha512("abc") != "ddaf35a193617abacc417349ae20413112e6fa4e89a97ea20a9eeee64b55d39a2192992a274"
                                          "fc1a836ba3c23a3feebbd454d4423643ce80e2a9ac94fa54ca49f")

    def test_for_non_string_types(self: SHA512Testing) -> None:
        """
        Test Method that checks if the hashing alogrithm raises a
        ValueError if a string isn't provided.

        Returns: None (void method)

        """
        with self.assertRaises(ValueError):
            sha512(150)
            sha512(1.56)


if __name__ == '__main__':
    main()
