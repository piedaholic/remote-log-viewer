from file_utils import FileUtils
import sys
import threading
import time

NO_OF_CHARS = 256

# Numbers of alphabet which we call base
alphabet_size = 256
# Modulus to hash a string
modulus = 1000003

class SearchUtils:
# Python program for KMP Algorithm

    def knuth_morris_pratt_search(self, pat, txt):
        M = len(pat)
        N = len(txt)

        results = list()

        # create lps[] that will hold the longest prefix suffix
        # values for pattern
        lps = [0]*M
        j = 0 # index for pat[]

        # Preprocess the pattern (calculate lps[] array)
        self.computeLPSArray(pat, M, lps)

        i = 0 # index for txt[]
        while i < N:
            if pat[j] == txt[i]:
                i += 1
                j += 1

            if j == M:
                results.append(str(i-j))
                #print("Found pattern at index " + str(i-j))
                j = lps[j-1]

            # mismatch after j matches
            elif i < N and pat[j] != txt[i]:
                # Do not match lps[0..lps[j-1]] characters,
                # they will match anyway
                if j != 0:
                    j = lps[j-1]
                else:
                    i += 1
        return results

    def computeLPSArray(self, pat, M, lps):
    	len = 0 # length of the previous longest prefix suffix

    	lps[0] # lps[0] is always 0
    	i = 1

    	# the loop calculates lps[i] for i = 1 to M-1
    	while i < M:
    		if pat[i]== pat[len]:
    			len += 1
    			lps[i] = len
    			i += 1
    		else:
    			# This is tricky. Consider the example.
    			# AAACAAAA and i = 7. The idea is similar
    			# to search step.
    			if len != 0:
    				len = lps[len-1]

    				# Also, note that we do not increment i here
    			else:
    				lps[i] = 0
    				i += 1

    def boyer_moore_search(self, pattern, text):
        results = list()
        m = len(pattern)
        n = len(text)
        try :
            if m > n: return -1
            skip = []
            for k in range(256): skip.append(m)
            for k in range(m - 1): skip[ord(pattern[k])] = m - k - 1
            skip = tuple(skip)
            k = m - 1
            while k < n:
                j = m - 1; i = k
                while j >= 0 and text[i] == pattern[j]:
                    j -= 1; i -= 1
                if j == -1:
                    results.append(i+1)
                    #return i + 1
                k += skip[ord(text[k])]
        except Exception as e :
            print('Exception Occurred ' , e)
        return results

    def rabin_karp_search(self, pattern, text):
        """
        The Rabin-Karp Algorithm for finding a pattern within a piece of text
        with complexity O(nm), most efficient when it is used with multiple patterns
        as it is able to check if any of a set of patterns match a section of text in o(1) given the precomputed hashes.
        This will be the simple version which only assumes one pattern is being searched for but it's not hard to modify
        1) Calculate pattern hash
        2) Step through the text one character at a time passing a window with the same length as the pattern
            calculating the hash of the text within the window compare it with the hash of the pattern. Only testing
            equality if the hashes match
        """
        results = list()
        p_len = len(pattern)
        t_len = len(text)
        if p_len > t_len:
            return None

        p_hash = 0
        text_hash = 0
        modulus_power = 1

        # Calculating the hash of pattern and substring of text
        for i in range(p_len):
            p_hash = (ord(pattern[i]) + p_hash * alphabet_size) % modulus
            text_hash = (ord(text[i]) + text_hash * alphabet_size) % modulus
            if i == p_len - 1:
                continue
            modulus_power = (modulus_power * alphabet_size) % modulus

        for i in range(0, t_len - p_len + 1):
            if text_hash == p_hash and text[i : i + p_len] == pattern:
                #return True
                results.append(str(i))
            if i == t_len - p_len:
                continue
            # Calculate the https://en.wikipedia.org/wiki/Rolling_hash
            text_hash = (
                (text_hash - ord(text[i]) * modulus_power) * alphabet_size
                + ord(text[i + p_len])
            ) % modulus
        return results

    def rabin_karp(self, pattern, text):
        """
        The Rabin-Karp Algorithm for finding a pattern within a piece of text
        with complexity O(nm), most efficient when it is used with multiple patterns
        as it is able to check if any of a set of patterns match a section of text in o(1) given the precomputed hashes.
        This will be the simple version which only assumes one pattern is being searched for but it's not hard to modify
        1) Calculate pattern hash
        2) Step through the text one character at a time passing a window with the same length as the pattern
            calculating the hash of the text within the window compare it with the hash of the pattern. Only testing
            equality if the hashes match
        """
        p_len = len(pattern)
        t_len = len(text)
        if p_len > t_len:
            return False

        p_hash = 0
        text_hash = 0
        modulus_power = 1

        # Calculating the hash of pattern and substring of text
        for i in range(p_len):
            p_hash = (ord(pattern[i]) + p_hash * alphabet_size) % modulus
            text_hash = (ord(text[i]) + text_hash * alphabet_size) % modulus
            if i == p_len - 1:
                continue
            modulus_power = (modulus_power * alphabet_size) % modulus

        for i in range(0, t_len - p_len + 1):
            if text_hash == p_hash and text[i : i + p_len] == pattern:
                return True
            if i == t_len - p_len:
                continue
            # Calculate the https://en.wikipedia.org/wiki/Rolling_hash
            text_hash = (
                (text_hash - ord(text[i]) * modulus_power) * alphabet_size
                + ord(text[i + p_len])
            ) % modulus
        return False

    def regex_search(self,pattern,text):
        results = list()
        #[(m.start(0), m.end(0)) for m in re.finditer(pattern, text)]
        [ results.add(m.start(0)) for m in re.finditer(pattern, text)]
        return results
