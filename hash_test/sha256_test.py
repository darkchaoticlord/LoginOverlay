from __future__ import annotations
from unittest import TestCase, main
from hash_algorithms.sha256 import sha256


class SHA256Testing(TestCase):

    def test_if_hashing_works(self: SHA256Testing) -> None:
        """
        Test Method that checks if the hashing algorithm works correctly
        for three different examples.

        Returns: None (void method)

        """
        self.assertEqual(sha256("The quick brown fox jumps over the lazy dog"),
                         "d7a8fbb307d7809469ca9abcb0082e4f8d5651e46d3cdb762d02d0bf37c9e592")
        self.assertTrue(sha256("The quick brown fox jumps over the lazy dog.") ==
                        "ef537f25c895bfa782526529a9b63d97aa631564d5d789c2b765448c8635fb6c")
        self.assertFalse(sha256("abc") != "ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad")

    def test_for_non_string_types(self: SHA256Testing) -> None:
        """
        Test Method that checks if the hashing alogrithm raises a
        ValueError if a string isn't provided.

        Returns: None (void method)

        """
        with self.assertRaises(ValueError):
            sha256(150)
            sha256(1.56)


if __name__ == '__main__':
    main()
