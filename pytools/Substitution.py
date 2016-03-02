from __future__ import division
from Cipher import Cipher
import math

class Substitution(Cipher):

    _reference_alphabet = None
    _substitute_alphabet = None

    @property
    def substitute_alphabet(self):
        if self._substitute_alphabet is None:
            print "[!] Substitution alphabet not given. Using standard alphabet"
            self._substitute_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        return self._substitute_alphabet

    @substitute_alphabet.setter
    def substitute_alphabet(self, alphabet):
        self._substitute_alphabet = alphabet


    @property
    def reference_alphabet(self):
        if self._reference_alphabet is None:
            print "[!] Reference alphabet not given. Using standard alphabet"
            self._reference_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        return self._reference_alphabet

    @reference_alphabet.setter
    def reference_alphabet(self, alphabet):
        self._reference_alphabet = alphabet
    

    def substitute(self):
        self.s = [self.__substitute_letter(c) for c in self.s]


    def __substitute_letter(self, letter):
        for i in range(len(self.reference_alphabet)):
            if letter == self.reference_alphabet[i]:
                return self.substitute_alphabet[i]
        return '?'