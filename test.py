"""
    To test: python test.py
"""
import ABSplitter
import unittest


class ABSplitter_Test(unittest.TestCase):
    def setUp(self):
        self.ab = ABSplitter.ABSplitter()

    def test(self):
        self.ab.reset(30.0, 70.0)
        for i in range(100):
            state = ""
            if self.ab.getNextVersion() == 'VERSION_A':
                state = 'VERSION_A'
            else:
                state = '            VERSION_B'
            print("User" + str(i) + " " + state)


if __name__ == '__main__':
    unittest.main()
