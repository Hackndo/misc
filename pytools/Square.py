# coding: utf-8
from __future__ import division
from KeyCipher import KeyCipher
from Substitution import Substitution

class Square(Substitution, KeyCipher):

    _keysquare = None

    def __init__(self, s, size_element=1, keep_spaces=False):
        Substitution.__init__(self, s, size_element, keep_spaces)
        self.s = [c.replace("J","I") for c in self.s]
        self.reference_alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"

    @property
    def keysquare(self):
        if self.reference_alphabet is None:
            self.reference_alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
        if self._keysquare is None:
            self.__initialize_keysquare()
        return self._keysquare
    

    def __initialize_keysquare(self):
        self.key = self.key.replace("J", "I")
        l = [c for c in self.reference_alphabet]
        self._keysquare = [['']*5 for i in range(5)]
        for i in range(len(self.key)):
            self._keysquare[i//5][i%5] = self.key[i]
            l.remove(self.key[i])
        for i in range(len(self.key), 25):
            self._keysquare[i//5][i%5] = l[i-len(self.key)]
    
    def encipher(self):
        self.__initialize_keysquare()
        self.substitute_alphabet = ''.join([''.join(r) for r in self.keysquare])
        print self.reference_alphabet
        print self.substitute_alphabet
        self.substitute()


    def decipher(self):
        encrypted = ['_'] * self.len
        counter = 0
        for i in range(self.len):
            if self.s[i] != " ":
                self.s[i] = chr((ord(self.s[i])-65+ord(self.key[counter])-65)%26+65)
                counter = (counter+1)%len(self.key)
        return self


    def decrypt(self, min_len=1, max_len=9, display=False):
        self.key = self._guess_key(min_len, max_len, display)
        if self.key < 0:
            print "Unable to decrypt the message. Perhaps it's to small and frequence analysis can't be used"
            return -1
        print "[*] Most probable key : " + self.key + "\n"
        self.decipher()
        print "[*] Decryption complete"


    def __guess_key(self, min_len=1, max_len=9, display=False):
        keylen = self.guess_key_length(min_len, max_len, display)
        if keylen == 0:
            print "[!] No key length found."
            return -1
        if display:
            print "[*] Most probable key length : " + str(keylen) + "\n"
        freq_fr = {'e': 14.715, 's': 7.948, 'a': 7.636, 'i': 7.529, 't': 7.244, 'n': 7.095, 'r': 6.553, 'u': 6.311, 'l': 5.456, 'o': 5.378, 'd': 3.669, 'c': 3.260, 'p': 3.021, 'm': 2.968, 'v': 1.628, 'q': 1.362, 'f': 1.066, 'b': 0.901, 'g': 0.866, 'h': 0.737, 'j': 0.545, 'x': 0.387, 'y': 0.308, 'z': 0.136, 'w': 0.114, 'k': 0.049}
        password = ""
        for i in range(keylen):
            sub_alphabet = Square(''.join([self.s[keylen*j + i] for j in range(self.len//keylen)]))
            min_differential = 99999
            password_letter = ""
            for c in range(65, 65+26):
                sub_alphabet.key = chr(c)
                decrypted = Square(sub_alphabet.decipher().tostring())
                sub_alphabet.encipher()
                freq_s = { k:round((v/decrypted.len)*100, 3) for k,v in dict(decrypted.get_frequencies()).items()}
                differential = sum([abs(freq_fr[k.lower()]-v) for k,v in freq_s.items()])
                if differential < min_differential:
                    min_differential = differential
                    password_letter = chr(c)
            password += password_letter

        # Little hack for repetitive password due to frequency analysis
        for i in range(1, len(password)):
            if len(password) % i == 0:
                duplicate = True
                s = [password[j*i:(j+1)*i] for j in range(len(password)//i)]
                ex_prec = s[0]
                for ex in s:
                    if ex != ex_prec:
                        duplicate = False
                        break
                    ex_prec = ex
                if duplicate:
                    password = ex
                    if display:
                        print "[*] [UPDATE] Most probable key length : " + str(len(password)) + "\n"
                    break
        return Square.clean_string(password)

if __name__ == "__main__":

    p = Square("Salut les amis, je suis parti en amerique du sud parce que je trouvais que l'endroit etait super sympa. Vous en pensez quoi ? Moi je trouve que c'est une idée géniale. Le voyage, tout le monde le sait, ça permet de fait de nouvelles rencontres, notamment la rencontre avec soi-même. Le voyage, tout le monde le sait, ça permet de découvrir le monde, de découvrir de nouvelles villes, de nouveaux villages, de nouveaux paysages. Le voyage, tout le monde le sait, ça permet de s'ouvrir à de nouvelles cultures, de nouvelles traditions, de nouvelles manières de vivre.  Ça, tout le monde le sait.  Mais pour moi, il y a quelque chose d'autre. Quelque chose que souvent j'oublie, que souvent je ne remarque pas, que souvent je néglige. Le voyage, je ne le savais pas, ça permet de me rendre compte que ma ville, Paris, est belle.  Paris, et tous ses quartiers plein de cafés aux multiples tintements de tasses, de terasses calmes sous les rayons de soleil, d'odeurs de baguettes sorties du four, de pavés authentiques, de façades aux magnifiques allures Hausmaniennes, de grandes portes en bois, de ruelles biscornues abritant des endroits secrets, de pont majestueux surplombant la Seine, de collines, de quais piétons aux plus grand plaisir des amoureux, de canaux promptent à des promenades dominicales sous les arbres en fleurs, de fleuristes aux coins de rues desquels émanent ces odeurs délicieuses, de vie, tout simplement.")
    p.key = "Hello"
    p.encipher()
    print p.tostring()
