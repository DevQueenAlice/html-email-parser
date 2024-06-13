import unittest


class BaseTest(unittest.TestCase):
    def setUp(self):
        print("setUp")

    def tearDown(self):
        print("tearDown")


if __name__ == '__main__':
    unittest.main()