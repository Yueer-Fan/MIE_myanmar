import unittest
import sys
sys.path.append('../..')

test_dir = './test_case'

suite = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')


if __name__ == "__main__":
    runner = unittest.TextTestRunner()

    runner.run(suite)
