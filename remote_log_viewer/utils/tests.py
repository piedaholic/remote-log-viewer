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

search_directory = 'D:\\Temp\\MyLogs'
file_pattern = '.*'
search_pattern = 'Exception'

class Test(unittest.TestCase):

    def test_search_string_in_files(self):
        search_algo_list = ['Knuth_Morris_Pratt' , 'Boyer_Moore', 'Rabin_Karp', 'Regex']
        for search_algo in search_algo_list:
            results = []
            fse.search = search_algo
            print('----'+search_algo + ' starts'+'----')
            start = time.time()
            results = fse.string_search(search_directory, file_pattern, search_pattern, None)
            end = time.time()
            for result in results:
                arr = result.split('~')
                print(f'Index:{arr[0]};Line:{arr[1]};File:{arr[2]}')
            print('Summary'+'\n' + '*********************************')
            print('Time elapsed :: ' , str(end-start))
            print('Pattern found at ' + str(len(results)) + ' instances')
            print('Pattern found in ' + str(fse.count_lines(results)) + ' lines')
            print('Pattern found in ' + str(fse.count_files(results)) + ' files')
            print('----' + search_algo + ' ends' + '----')

    def test_rabin_karp(self):
        '''
        >>> test_rabin_karp()
        Success.
        '''
        # Test 1)
        pattern = 'abc1abc12'
        text1 = 'alskfjaldsabc1abc1abc12k23adsfabcabc'
        text2 = 'alskfjaldsk23adsfabcabc'
        assert se.rabin_karp(pattern, text1) and not se.rabin_karp(pattern, text2)

        # Test 2)
        pattern = 'ABABX'
        text = 'ABABZABABYABABX'
        assert se.rabin_karp(pattern, text)

        # Test 3)
        pattern = 'AAAB'
        text = 'ABAAAAAB'
        assert se.rabin_karp(pattern, text)

        # Test 4)
        pattern = 'abcdabcy'
        text = 'abcxabcdabxabcdabcdabcy'
        assert se.rabin_karp(pattern, text)

        # Test 5)
        pattern = 'Lü'
        text = 'Lüsai'
        assert se.rabin_karp(pattern, text)
        pattern = 'Lue'
        assert not se.rabin_karp(pattern, text)

    def test_regex(self):
        '''
        >>> test_regex()
        Success.
        '''
        # Test 1)
        pattern = 'abc1abc12'
        text1 = 'alskfjaldsabc1abc1abc12k23adsfabcabc'
        text2 = 'alskfjaldsk23adsfabcabc'
        assert se.regex(pattern, text1) and not se.regex(pattern, text2)

        # Test 2)
        pattern = 'ABABX'
        text = 'ABABZABABYABABX'
        assert se.regex(pattern, text)

        # Test 3)
        pattern = 'AAAB'
        text = 'ABAAAAAB'
        assert se.regex(pattern, text)

        # Test 4)
        pattern = 'abcdabcy'
        text = 'abcxabcdabxabcdabcdabcy'
        assert se.regex(pattern, text)

        # Test 5)
        pattern = 'Lü'
        text = 'Lüsai'
        assert se.regex(pattern, text)
        pattern = 'Lue'
        assert not se.regex(pattern, text)

    def test_knuth_morris_pratt(self):
        '''
        >>> test_knuth_morris_pratt()
        Success.
        '''
        # Test 1)
        pattern = 'abc1abc12'
        text1 = 'alskfjaldsabc1abc1abc12k23adsfabcabc'
        text2 = 'alskfjaldsk23adsfabcabc'
        assert se.knuth_morris_pratt(pattern, text1) and not se.knuth_morris_pratt(pattern, text2)

        # Test 2)
        pattern = 'ABABX'
        text = 'ABABZABABYABABX'
        assert se.knuth_morris_pratt(pattern, text)

        # Test 3)
        pattern = 'AAAB'
        text = 'ABAAAAAB'
        assert se.knuth_morris_pratt(pattern, text)

        # Test 4)
        pattern = 'abcdabcy'
        text = 'abcxabcdabxabcdabcdabcy'
        assert se.knuth_morris_pratt(pattern, text)

        # Test 5)
        pattern = 'Lü'
        text = 'Lüsai'
        assert se.knuth_morris_pratt(pattern, text)
        pattern = 'Lue'
        assert not se.knuth_morris_pratt(pattern, text)

    def test_boyer_moore(self):
        '''
        >>> test_boyer_moore()
        Success.
        '''
        # Test 1)
        pattern = 'abc1abc12'
        text1 = 'alskfjaldsabc1abc1abc12k23adsfabcabc'
        text2 = 'alskfjaldsk23adsfabcabc'
        assert se.boyer_moore(pattern, text1) and not se.boyer_moore(pattern, text2)

        # Test 2)
        pattern = 'ABABX'
        text = 'ABABZABABYABABX'
        assert se.boyer_moore(pattern, text)

        # Test 3)
        pattern = 'AAAB'
        text = 'ABAAAAAB'
        assert se.boyer_moore(pattern, text)

        # Test 4)
        pattern = 'abcdabcy'
        text = 'abcxabcdabxabcdabcdabcy'
        assert se.boyer_moore(pattern, text)

        # Test 5)
        pattern = 'Lü'
        text = 'Lüsai'
        assert se.boyer_moore(pattern, text)
        pattern = 'Lue'
        assert not se.boyer_moore(pattern, text)

if __name__ == '__main__':
    unittest.main()
