from __future__ import annotations
from unittest import TestCase, main
from hash_algorithms.sha1 import sha1


class SHA1Testing(TestCase):

    def test_if_hashing_works(self: SHA1Testing) -> None:
        """
        Test Method that checks if the hashing algorithm works correctly
        for three different examples.

        Returns: None (void method)

        """
        self.assertEqual(sha1("The quick brown fox jumps over the lazy dog"),
                         "2fd4e1c67a2d28fced849ee1bb76e7391b93eb12")
        self.assertTrue(sha1("The quick brown fox jumps over the lazy dog.") ==
                        "408d94384216f890ff7a0c3528e8bed1e0b01621")
        self.assertFalse(sha1("abc") != "a9993e364706816aba3e25717850c26c9cd0d89d")

    def test_for_non_string_types(self: SHA1Testing) -> None:
        """
        Test Method that checks if the hashing alogrithm raises a
        ValueError if a string isn't provided.

        Returns: None (void method)

        """
        with self.assertRaises(ValueError):
            sha1(150)
            sha1(1.56)


if __name__ == '__main__':
    main()
