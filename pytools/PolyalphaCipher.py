from Cipher import Cipher
from Text import Text
import math

class PolyalphaCipher(Cipher):
    _key = None

    @property
    def key(self):
        return self._key
    
    @key.setter
    def key(self, key):
        self._key = Text.clean_string(key)


    @key.deleter
    def key(self):
        del self._key


    def guess_key_length(self, min_len=1, max_len=9, display=False):
        """
        Guess key length based on frequence analysis
        """

        res = {}
        max_ic = 0
        probable_key_length = 0
        # We try different key lengths
        for i in range(min_len, max_len+1):

            if self._len < i*2:
                continue
            ics = []
            for j in range(i):
                var = []
                for k in range(self._len//i):
                    var.append(self._s[k*i + j])
                text = Text(''.join(var))
                ics.append(text.get_ic())
            total_ic = round(sum(ics)/len(ics),4)
            if total_ic > max_ic:
                max_ic = total_ic
                probable_key_length = i
            res[i] = total_ic
        if display:
            print "\n[+] Visual key length IC correspondance"
            for k,v in res.items():
                v = int(round(v*1000,0))
                print str(k) + (int(math.floor(math.log10(len(res))))+1-len(str(k)))*" ",
                print ''.join(['|' for i in range(v//2)])
            print ""
        return probable_key_length