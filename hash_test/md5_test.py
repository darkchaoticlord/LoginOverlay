from __future__ import annotations
from unittest import TestCase, main
from hash_algorithms.md5 import md5


class MD5Testing(TestCase):

    def test_if_hashing_works(self: MD5Testing) -> None:
        """
        Test Method that checks if the hashing algorithm works correctly
        for three different examples.

        Returns: None (void method)

        """
        self.assertEqual(md5("The quick brown fox jumps over the lazy dog"), "9e107d9d372bb6826bd81d3542a419d6")
        self.assertTrue(md5("The quick brown fox jumps over the lazy dog.") == "e4d909c290d0fb1ca068ffaddf22cbd0")
        self.assertFalse(md5("abc") != "900150983cd24fb0d6963f7d28e17f72")

    def test_for_non_string_types(self: MD5Testing) -> None:
        """
        Test Method that checks if the hashing alogrithm raises a
        ValueError if a string isn't provided.

        Returns: None (void method)

        """
        with self.assertRaises(ValueError):
            md5(150)
            md5(True)


if __name__ == '__main__':
    main()
