from file_utils import FileUtils
from search_utils import SearchUtils
import re
import os
import sys
from os import listdir
from os.path import isfile, join
from os import walk

class FileSearchUtils:

    def __init__(self, search):
        self.se = SearchUtils()
        self.search = search

    def string_search(self, path, file_pattern, search_pattern, recursionLevel):
        results = set()
        displayFullPath = True
        displayOnlyFiles = True
        path = FileUtils.normalize_path(path)
        count1 = len(re.findall(re.escape(os.sep),path))
        if re.compile('^(.*)'+re.escape(os.sep)+'$').match(path):
            count1 = count1 - 1
        if recursionLevel is None:
            recursionLevel = sys.maxsize
        for (dirpath, dirnames, filenames) in walk(path):
            count2 = len(re.findall(re.escape(os.sep),dirpath))
            #count2 = dirpath.count(re.escape(os.sep))
            if re.compile('^(.*)'+re.escape(os.sep)+'$').match(dirpath):
                count2 = count2 - 1
            level = count2 - count1
            if ( level <= recursionLevel):
                for filename in filenames:
                    if re.search(file_pattern, filename):
                        lines = FileUtils.read_file_line_wise(os.path.join(dirpath,filename))
                        count = 0
                        if lines is not None:
                            for line in lines:
                                if (self.search == 'Rabin_Karp'):
                                    searchResults = self.se.rabin_karp_search(pattern,line)
                                elif (self.search == 'Boyer_Moore_Search'):
                                    searchResults = self.se.rabin_karp_search(pattern,line)
                                elif (self.search == 'Regex_Search'):
                                    searchResults = self.se.regex_search(pattern,line)
                                else:
                                    self.search == 'Knuth_Morris_Pratt'
                                    searchResults = self.se.knuth_morris_pratt_search(pattern,line)
                                count += 1
                                if  searchResults is not None:
                                    for searchResult in searchResults:
                                        results.add(str(searchResult)+'~'+str(count)+'~'+file)

        return results

    def string_search_kmp1(self, pattern, file, results):
        lines = FileUtils.read_file_line_wise(file)
        count = 0
        if lines is not None:
            for line in lines:
                searchResults = self.se.knuth_morris_pratt_search(pattern,line)
                count += 1
                if  searchResults is not None and isinstance(searchResults, list):
                    for searchResult in searchResults:
                        results.add(str(searchResult)+'~'+str(count)+'~'+file)


    def string_search_bmp1(self, pattern, file, results):
        lines = FileUtils.read_file_line_wise(file)
        count = 0
        if lines is not None:
            for line in lines:
                searchResults = self.se.boyer_moore_search(pattern,line)
                count += 1
                if  searchResults is not None and isinstance(searchResults, list):
                    for searchResult in searchResults:
                        results.add(str(searchResult)+'~'+str(count)+'~'+file)

    def string_search_rk1(self, pattern, file, results):
        lines = FileUtils.read_file_line_wise(file)
        count = 0
        if lines is not None:
            for line in lines:
                searchResults = self.se.rabin_karp_search(pattern,line)
                count += 1
                if  searchResults is not None and isinstance(searchResults, list):
                    for searchResult in searchResults:
                        results.add(str(searchResult)+'~'+str(count)+'~'+file)

    def string_search_bmp0(self, path, file_pattern, search_pattern, recursionLevel):
        results = set()
        path = FileUtils.normalize_path(path)
        count1 = len(re.findall(re.escape(os.sep),path))
        if re.compile('^(.*)'+re.escape(os.sep)+'$').match(path):
            count1 = count1 - 1
        if recursionLevel is None:
            recursionLevel = sys.maxsize
        for (dirpath, dirnames, filenames) in walk(path):
            count2 = len(re.findall(re.escape(os.sep),dirpath))
            #count2 = dirpath.count(re.escape(os.sep))
            if re.compile('^(.*)'+re.escape(os.sep)+'$').match(dirpath):
                count2 = count2 - 1
            level = count2 - count1
            if ( level <= recursionLevel):
                for filename in filenames:
                    if re.search(file_pattern, filename):
                                self.string_search_bmp1(search_pattern, os.path.join(dirpath,filename), results)
        return results

    def string_search_kmp0(self, path, file_pattern, search_pattern, recursionLevel):
        results = set()
        displayFullPath = True
        displayOnlyFiles = True
        path = FileUtils.normalize_path(path)
        count1 = len(re.findall(re.escape(os.sep),path))
        if re.compile('^(.*)'+re.escape(os.sep)+'$').match(path):
            count1 = count1 - 1
        if recursionLevel is None:
            recursionLevel = sys.maxsize
        for (dirpath, dirnames, filenames) in walk(path):
            count2 = len(re.findall(re.escape(os.sep),dirpath))
            #count2 = dirpath.count(re.escape(os.sep))
            if re.compile('^(.*)'+re.escape(os.sep)+'$').match(dirpath):
                count2 = count2 - 1
            level = count2 - count1
            if ( level <= recursionLevel):
                for filename in filenames:
                    if re.search(file_pattern, filename):
                                self.string_search_kmp1(search_pattern, os.path.join(dirpath,filename), results)
        return results

    def string_search_rk0(self, path, file_pattern, search_pattern, recursionLevel):
        results = set()
        displayFullPath = True
        displayOnlyFiles = True
        path = FileUtils.normalize_path(path)
        count1 = len(re.findall(re.escape(os.sep),path))
        if re.compile('^(.*)'+re.escape(os.sep)+'$').match(path):
            count1 = count1 - 1
        if recursionLevel is None:
            recursionLevel = sys.maxsize
        for (dirpath, dirnames, filenames) in walk(path):
            count2 = len(re.findall(re.escape(os.sep),dirpath))
            #count2 = dirpath.count(re.escape(os.sep))
            if re.compile('^(.*)'+re.escape(os.sep)+'$').match(dirpath):
                count2 = count2 - 1
            level = count2 - count1
            if ( level <= recursionLevel):
                for filename in filenames:
                    if re.search(file_pattern, filename):
                                self.string_search_rk1(search_pattern, os.path.join(dirpath,filename), results)
        return results

    def count_lines(self, results):
        lines = set()
        for result in results:
            arr = result.split('~')
            lines.add(arr[1]+'~'+arr[2])
        return len(lines)

    def count_files(self, results):
        files = set()
        for result in results:
            arr = result.split('~')
            files.add(arr[2])
        #print(files)
        return len(files)
