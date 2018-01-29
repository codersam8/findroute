import unittest

import find_route


class TestFindRoute(unittest.TestCase):

    def test_positive(self):
        self.assertEqual(find_route.find_route([['a1', 'a2'], ['a2', 'a3']]), ['a1', 'a2', 'a3'])


if __name__ == '__main__':
    unittest.main()
