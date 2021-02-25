"""Contains a test suite for basic tests."""
import context
import unittest

from TriplesLab.__main__ import main


class MainTestSuite(unittest.TestCase):
    """Basic test cases."""

    def test_main(self):
        main()


if __name__ == '__main__':
    unittest.main()
