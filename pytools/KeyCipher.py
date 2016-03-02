from Cipher import Cipher

class KeyCipher(Cipher):
    _key = None

    def __init__(self, s, size_element=1, keep_spaces=False, key=None):
        Cipher.__init__(self, s, size_element, keep_spaces)
        self.key = key

    @property
    def key(self):
        if self._key is None:
            print "[!] No key provided. Setting key to 'A'."
            self._key = 'A'
        return self._key
    
    @key.setter
    def key(self, key):
        self._key = KeyCipher.clean_string(key)


    @key.deleter
    def key(self):
        del self._key