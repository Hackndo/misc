# coding: utf-8
from __future__ import division
import collections
import math
class Text(object):
    def __init__(self, s, size_element=1, keep_spaces=False):
        """
        s: Text to analyse
        size_element: Size of one element

        Example
        if a = "AAA", b = "BBB", ..., z = "ZZZ"
        One element is 3 bytes
        text = Text("HHHEEELLLLLLOOOWWWOOORRRLLLDDD", 3)
        """
        s = Text.clean_string(s, keep_spaces)
        self._s = [s[size_element*j:(j+1)*size_element] for j in range(len(s)//size_element)]
        self._len = len(self.s)
        self._frequencies = self.get_frequencies()
        


# ---------------------------------- PUBLIC ----------------------------------
    
    # s getter, setter
    @property
    def s(self):
        return self._s


    @s.setter
    def s(self, s):
        self._s = s

    # len getter
    @property
    def len(self):
        return self._len
    

    def help(self):
        print "************************"
        print "* Text analysis module *"
        print "************************\n"
        print "+-------------------+"
        print "| Available methods |"
        print "+-------------------+\n"

        print "[+] Text(s, size_element=1, keep_spaces=False)"
        print "    s: Text to analyse"
        print "    size_element: Size of one element"
        print "    keep_spaces: Keep spaces\n"

        print "[+] display()"
        print "    Display analysed text\n"

        print "[*] get_number_of_different_char()"
        print "    Return number of unique chars\n"

        print "[+] get_frequencies(n=1)"
        print "    Return frequencies of 'n' size group of letters\n"

        print "[+] get_double_letters_frequencies()"
        print "    Return frenquencies of double letters\n"

        print "[+] get_most_common_frequencies(n=1, m=5)"
        print "    Return 'm' most frequent 'n' size group of letters\n"

        print "[+] get_ic()"
        print "    Return indice of coincidence of analysed text\n"

        print "[+] analyse()"
        print "    Display general information about analysed text\n"


    def display(self):
        """
        Display analysed text
        """

        print ''.join(self._s)


    def tostring(self):

        return ''.join(self._s)


    def get_number_of_different_char(self):
        """
        Return number of unique chars
        """

        copy = self._s
        return len(set(copy))


    def get_frequencies(self, n=1):
        """
        Return frequencies of 'n' size group of letters
        """

        l = []
        for i in range(n):
            l.extend([''.join(self._s[j*n+i:j*n+n+i]) for j in range((len(self._s)-i)//n)])
        return collections.Counter(l)


    def get_double_letters_frequencies(self):
        """
        Return frenquencies of double letters
        """
        l = []
        for i in range(2):
            l.extend([''.join(self._s[j*2+i:(j+1)*2+i]) if self._s[j*2+i] == self._s[(j+1)*2+i-1] else '' for j in range((len(self._s)-i)//2)])
        counter = collections.Counter(l)
        del counter['']
        return counter


    def get_most_common_frequencies(self, n=1, m=5):
        """
        Return 'm' most frequent 'n' size group of letters
        """

        return self.get_frequencies(n).most_common(m)


    def get_ic(self):
        """
        Return indice of coincidence of analysed text
        """
        return round(sum(
            [self._frequencies.values()[i]*(self._frequencies.values()[i]-1)
            /(self._len*(self._len-1)) for i in range(len(self._frequencies))]), 4)
        

    def analyse(self):
        """
        Display general information about analysed text
        """

        print "[*] ANALYSIS\n"
        print "    [+] Size"
        print "    " + str(self.len) + " chars"

        print "\n    [+] Number of unique chars"
        print "    " + str(self.get_number_of_different_char())
        r = list(set(self._s))
        r.sort()
        print "    " + str(r)

        print "\n    [+] Most common frequencies"
        print "    " + str(self.get_most_common_frequencies(n=1, m=5))

        print "\n    [+] Double letters frequencies"
        print "    " + str(self.get_double_letters_frequencies())

        print "\n    [+] IC"
        print "    " + str(self.get_ic())

        print ""

# ---------------------------------- STATIC ----------------------------------

    @staticmethod
    def clean_string(s, keep_spaces=False):
        if s == "" or s is None:
            return None
        s = s.lower().replace("’", "").replace("é","e").replace("è","e").replace("ê","e").replace("ë","e").replace("à","a").replace("ç","c").replace("Ç", "c").replace(".","").replace(",","").replace("?","").replace("!","").replace(":","").replace(";","").replace("-","").replace("'","").replace("\"","").replace("(","").replace(")","").replace("ù","u").replace("ô","o").replace("ü","u")
        if not keep_spaces:
            s = s.replace(" ","")
        return s.upper()