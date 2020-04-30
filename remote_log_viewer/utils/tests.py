import unittest
from file_utils import FileUtils

fu = FileUtils()

class FileUtilsTest(unittest.TestCase):
    def test_list():
        print(fu.list(''))

if __name__ == '__main__':
    unittest.main()
