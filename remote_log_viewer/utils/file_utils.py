from pathlib import Path
from shutil import copyfile
import os
import sys
import re
from os import listdir
from os.path import isfile, join
from os import walk
# re.compile(r"^([a-z0-9.-]+|\[[a-f0-9]*:[a-f0-9\.:]+\])(:\d+)?$")
'''
Mode 	Description
'r' 	This is the default mode. It Opens file for reading.
'w' 	This Mode Opens file for writing.
        If file does not exist, it creates a new file.
        If file exists it truncates the file.
'x' 	Creates a new file. If file already exists, the operation fails.
'a' 	Open file in append mode.
        If file does not exist, it creates a new file.
        Does not truncate the file, instead appends text to it
't' 	This is the default mode. It opens in text mode.
'b' 	This opens in binary mode.
'+' 	This will open a file for reading and writing (updating)
'r+'	Open the file for reading and writing both
'''

class FileUtils():
    """docstring for ."""

    #def __init__(self):
        #super(self).__init__()

    def create_directory(directory_path):
        if not Path(directory_path).exists():
            os.mkdir(directory_path)


    def write_to_file(file_path, text):
        my_file = Path(file_path)
        if my_file.exists():
            f = open(file_path, "a")
        else:
            create_directory(os.path.dirname(file_path))
            f = open(file_path, "w")
        f.write(text)
        f.close()


    def write(file_path, text):
        my_file = Path(file_path)
        if my_file.exists():
            f = open(file_path, "w")
        else:
            create_directory(os.path.dirname(file_path))
            f = open(file_path, "w")
        f.write(text)
        f.close()


    def read_file(file_path):
        my_file = Path(file_path)
        #if my_file.exists():
        try:
            f = open(file_path, mode='r', encoding='utf-8')
            file_content = f.read()
        except Exception:
            file_content = None
        return file_content


    def read_file_line_wise(file_path):
        #my_file = Path(file_path)
        lines = list()
        #if my_file.exists():
        f = None
        try:
            f = open(file_path, mode='r', encoding='utf-8')
            # lines = list(f)
            lines = f.readlines()
            '''
            # use readline() to read the first line
            line = f.readline()
            # use the read line to read further.
            # If the file is not empty keep reading one line
            # at a time, till the file is empty
            while line:
                # in python 2+
                # print line
                # in python 3 print is a builtin function, so
                # use readline() to read next line
                line = f.readline()
            '''
            f.close()
        except Exception as e:
            lines=None
            if f is not None:
                f.close()
            #print('Errored File' + file_path + ' ' + format(e))
        return lines


    '''
    def copy_binary_file(source_path, destination_path):
        if not Path(source_path).exists():
            return False
        create_directory(os.path.dirname(destination_path))
        destination_file = open(destination_path, "wb")
        with open(source_path, "rb") as source_file:
            byte = source_file.read(1)
            while byte != b"":
                # Do stuff with byte.
                destination_file.write(byte)
                byte = source_file.read(1)
        # Close open file handles
        source_file.close()
        destination_file.close()
        return True
    '''


    def copy_binary_file(source_path, destination_path):
        if not Path(source_path).exists():
            return False
        create_directory(os.path.dirname(destination_path))
        with open(source_path, 'rb') as f1:
            with open(destination_path, 'wb') as f2:
                f2.write(f1.read())
        return True


    def copy_binary_file_with_buffer(source_path, destination_path, buffer):
        if not Path(source_path).exists():
            return False
        create_directory(os.path.dirname(destination_path))
        success = True
        with open(source_path, 'rb') as f1:
            with open(destination_path, 'wb') as f2:
                while True:
                    buf = f1.read(buffer)
                    if buf and success:
                        # for byte in buf:
                        # pass
                        # process the bytes if this is what you want. Make sure your changes are in buf
                        success = success and f2.write(buf)
                    else:
                        break
        return success


    def write_binary_file(file_path, file_content):
        if Path(file_path).exists():
            file = open(file_path, "wb")
            file.write(file_content)
            file.close()
        else:
            create_directory(os.path.dirname(file_path))
            file = open(file_path, "wb")
            file.write(file_content)
            file.close()


    def append_binary_file(file_path, file_content):
        if Path(file_path).exists():
            file = open(file_path, "ab")
            file.write(file_content)
            file.close()
        else:
            create_directory(os.path.dirname(file_path))
            file = open(file_path, "ab")
            file.write(file_content)
            file.close()


    def copy_file(source, destination):
        copyfile(source, destination)


    def read_properties_file(path):
        prop_file = open(path, "r")
        prop_dict = dict()
        for prop_line in prop_file:
            prop_def = prop_line.strip()
            if len(prop_def) == 0:
                continue
            if prop_def[0] in ('!', '#'):
                continue
            punctuation = [prop_def.find(c) for c in '='] + [len(prop_def)]
            found = min([pos for pos in punctuation if pos != -1])
            name = prop_def[:found].rstrip()
            print(name)
            value = prop_def[found:].lstrip("=").rstrip()
            print(value)
            prop_dict[name] = value
        prop_file.close()
        # print propDict
        return prop_dict

    def list_files(self, path):
        onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
        return onlyfiles

    def list(self, path):
        f = []
        for (dirpath, dirnames, filenames) in walk(path):
            f.extend(filenames)
            print(dirnames)
            break
        return f

    def find(self, path, regex, displayOnlyFiles, displayFullPath, recursionLevel):
        f = set()
        path = normalize_path(path)
        count1 = len(re.findall(re.escape(os.sep),path))
        if re.compile('^(.*)'+re.escape(os.sep)+'$').match(path):
            count1 = count1 - 1

        # print('displayOnlyFiles:'+str(displayOnlyFiles))
        # print('displayFullPath:'+str(displayFullPath))
        # print('recursionLevel:'+str(recursionLevel))
        # print('path:'+ path)
        # print('count1:'+ str(count1))

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
                    if re.search(regex, filename):
                            if (displayFullPath):
                                f.add(os.path.join(dirpath,filename))
                                # print('count2:' + str(count2))
                                # print('level:' + str(level))
                                # print('dirpath:' + dirpath)
                            else:
                                f.add(filename)
                    if displayOnlyFiles:
                        for dirname in dirnames:
                            if re.search(regex, dirname):
                                if (displayFullPath):
                                    f.add(os.path.join(dirpath,dirname))
                                else:
                                    f.add(dirname)
        return f

    def normalize_path(path):
        # path=re.sub(r'/|\\', re.escape(os.sep), path)
        # if re.compile('^(.*)'+re.escape(os.sep)+'$').match(path):
        #         path = re.compile('^(.*)'+re.escape(os.sep)+'$').match(path).group(1)
        # return path
        return re.sub(r'/|\\', re.escape(os.sep), path)
