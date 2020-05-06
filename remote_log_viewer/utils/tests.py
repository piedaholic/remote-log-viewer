import unittest
from file_utils import FileUtils
from search_utils import SearchUtils
from file_search_utils import FileSearchUtils
import os
import re
import time

fu = FileUtils()
se = SearchUtils()
fse = FileSearchUtils()

class Test(unittest.TestCase):
    # def test_list(self):
    #      f = fu.find('D:\\','Harsh(.*)\.zip',False,True,2)
    #      print(f)

    def test_search_string_knuth_morris_pratt(self):
        blockStart = "-----Knuth Morris Pratt Starts-----"
        blockEnd = "-----Knuth Morris Pratt Ends-----"
        start = time.time()
        print(blockStart)
        # results = fse.string_search_kmp0('D:\\Temp\\MyLogs\\', '.*', 'Exception', None)
        # print('Pattern found at ' + str(len(results)) + ' instances')
        # for result in results:
        #     arr = result.split('~')
        #     print(f'Index:{arr[0]};Line:{arr[1]};File:{arr[2]}')
        print(se.knuth_morris_pratt_search('AB','ABCABDEGFFGEAB  RG !~@@##$%'))
        end = time.time()
        print('Time elapsed :: ' , str(end-start))
        print(blockEnd)

    def test_search_string_in_files_knuth_morris_pratt(self):
        blockStart = "-----Knuth Morris Pratt Starts-----"
        blockEnd = "-----Knuth Morris Pratt Ends-----"
        results = []
        start = time.time()
        print(blockStart)
        results = fse.string_search_kmp0('D:\\Temp\\MyLogs\\', '.*', 'Exception', None)
        print('Pattern found at ' + str(len(results)) + ' instances')
        print('Pattern found in ' + str(fse.count_lines(results)) + ' lines')
        print('Pattern found in ' + str(fse.count_files(results)) + ' files')
        # for result in results:
        #     arr = result.split('~')
        #     print(f'Index:{arr[0]};Line:{arr[1]};File:{arr[2]}')
        end = time.time()
        print('Time elapsed :: ' , str(end-start))
        print(blockEnd)

    def test_search_string_boyer_moore(self):
            blockStart = "-----Boyer Moore Starts-----"
            blockEnd = "-----Boyer Moore Ends-----"
            # pattern = 'Exception'
            print(blockStart)
            start = time.time()
            print(se.boyer_moore_search('AB','ABCABDEGFFGEAB  RG !~@@##$%'))
            end = time.time()
            print('Time elapsed :: ' , str(end-start))
            print(blockEnd)

    def test_search_string_in_files_boyer_moore(self):
        blockStart = "-----Boyer Moore Starts-----"
        blockEnd = "-----Boyer Moore Ends-----"
        results = []
        start = time.time()
        print(blockStart)
        results = fse.string_search_bmp0('D:\\Temp\\MyLogs\\', '.*', 'Exception', None)
        print('Pattern found at ' + str(len(results)) + ' instances')
        print('Pattern found in ' + str(fse.count_lines(results)) + ' lines')
        print('Pattern found in ' + str(fse.count_files(results)) + ' files')
        # for result in results:
        #     arr = result.split('~')
        #     print(f'Index:{arr[0]};Line:{arr[1]};File:{arr[2]}')
        end = time.time()
        print('Time elapsed :: ' , str(end-start))
        print(blockEnd)

    def test_search_string_rabin_karp(self):
            blockStart = "-----Rabin Karp Starts-----"
            blockEnd = "-----Rabin Karp Ends-----"
            # pattern = 'Exception'
            print(blockStart)
            start = time.time()
            print(se.rabin_karp_search('AB','ABCABDEGFFGEAB  RG !~@@##$%'))
            end = time.time()
            print('Time elapsed :: ' , str(end-start))
            print(blockEnd)

    def test_search_string_in_files_rabin_karp(self):
        blockStart = "-----Rabin Karp Starts-----"
        blockEnd = "-----Rabin Karp Ends-----"
        results = []
        start = time.time()
        print(blockStart)
        results = fse.string_search_rk0('D:\\Temp\\MyLogs\\', '.*', 'Exception', None)
        print('Pattern found at ' + str(len(results)) + ' instances')
        print('Pattern found in ' + str(fse.count_lines(results)) + ' lines')
        print('Pattern found in ' + str(fse.count_files(results)) + ' files')
        # for result in results:
        #     arr = result.split('~')
        #     print(f'Index:{arr[0]};Line:{arr[1]};File:{arr[2]}')
        end = time.time()
        print('Time elapsed :: ' , str(end-start))
        print(blockEnd)

    def test_rabin_karp(self):
        """
        >>> test_rabin_karp()
        Success.
        """
        # Test 1)
        pattern = "abc1abc12"
        text1 = "alskfjaldsabc1abc1abc12k23adsfabcabc"
        text2 = "alskfjaldsk23adsfabcabc"
        assert se.rabin_karp(pattern, text1) and not se.rabin_karp(pattern, text2)

        # Test 2)
        pattern = "ABABX"
        text = "ABABZABABYABABX"
        assert se.rabin_karp(pattern, text)

        # Test 3)
        pattern = "AAAB"
        text = "ABAAAAAB"
        assert se.rabin_karp(pattern, text)

        # Test 4)
        pattern = "abcdabcy"
        text = "abcxabcdabxabcdabcdabcy"
        assert se.rabin_karp(pattern, text)

        # Test 5)
        pattern = "Lü"
        text = "Lüsai"
        assert se.rabin_karp(pattern, text)
        pattern = "Lue"
        assert not se.rabin_karp(pattern, text)
        print("Success.")

    # def test_search_zip_files(self):
    #     f = fu.find('D:\\','*\.zip',False,True,2)
    #     print(f)

if __name__ == '__main__':
    unittest.main()
