# coding: utf-8
from __future__ import division
import collections
import math
class Text:
    def __init__(self, s, size_element=1, keep_spaces=False):
        """
        s: Text to analyse
        size_element: Size of one element

        Example
        if a = "AAA", b = "BBB", ..., z = "ZZZ"
        One element is 3 bytes
        text = Text("HHHEEELLLLLLOOOWWWOOORRRLLLDDD", 3)
        """

        s = self._clean_string(s, keep_spaces)
        self.s = [s[size_element*j:(j+1)*size_element] for j in range(len(s)//size_element)]
        self.len = self._set_len()
        self.frequencies = self.get_frequencies()


# ---------------------------------- PUBLIC ----------------------------------


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

        print "[+] set_text(s, size_element=1, keep_spaces=False)"
        print "    Set new text"
        print "    s: Text to analyse"
        print "    size_element: Size of one element"
        print "    keep_spaces: Keep spaces\n"

        print "[+] display()"
        print "    Display analysed text\n"

        print "[+] get_len()"
        print "    Return length of analysed text\n"

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

        print "[+] vigenere_encrypt(key)"
        print "    Encrypt text with Vigenere cipher with the key 'key'\n"

        print "[+] vigenere_decrypt(key=None, min_len=1, max_len=9, display=False)"
        print "    Decrypt Vigenere cipher, either with the key of with the guessed key\n"

        print "[+] analyse()"
        print "    Display general information about analysed text\n"


    def set_text(self, s, size_element=1, keep_spaces=False):
        """
        Set new text
        """

        s = self._clean_string(s, keep_spaces)
        self.s = [s[size_element*j:(j+1)*size_element] for j in range(len(s)//size_element)]
        self.len = self._set_len()
        self.frequencies = self.get_frequencies()


    def display(self):
        """
        Display analysed text
        """

        print ''.join(self.s)


    def get_len(self):
        """
        Return length of analysed text
        """

        return self.len


    def get_number_of_different_char(self):
        """
        Return number of unique chars
        """

        copy = self.s
        return len(set(copy))


    def get_frequencies(self, n=1):
        """
        Return frequencies of 'n' size group of letters
        """

        l = []
        for i in range(n):
            l.extend([''.join(self.s[j*n+i:j*n+n+i]) for j in range((len(self.s)-i)//n)])
        return collections.Counter(l)


    def get_double_letters_frequencies(self):
        """
        Return frenquencies of double letters
        """
        l = []
        for i in range(2):
            l.extend([''.join(self.s[j*2+i:(j+1)*2+i]) if self.s[j*2+i] == self.s[(j+1)*2+i-1] else '' for j in range((len(self.s)-i)//2)])
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
            [self.frequencies.values()[i]*(self.frequencies.values()[i]-1)
            /(self.len*(self.len-1)) for i in range(len(self.frequencies))]), 4)


    def vigenere_encrypt(self, key):
        """
        Encrypt text with Vigenere cipher with the key 'key'
        """

        encrypted = ['_'] * self.len
        key = self._clean_string(key).strip()
        counter = 0
        for i in range(self.len):
            if self.s[i] != " ":
                encrypted[i] = chr((ord(self.s[i])-65+ord(key[counter])-65)%26+65)
                counter = (counter+1)%len(key)
        return ''.join(encrypted)


    def vigenere_decrypt(self, key=None, min_len=1, max_len=9, display=False):
        """
        Decrypt Vigenere cipher, either with the key of with the guessed key
        """
        if key is None:
            print "[*] Will try to decrypt based on frequence analysis"
            key = self._guess_key(min_len, max_len, display)
            print "[*] Most probable key : " + key + "\n"
        key = key.upper()
        counter = 0
        decrypted = ['_'] * self.len
        for i in range(self.len):
            if self.s[i] != " ":
                decrypted[i] = chr((ord(self.s[i])-65-(ord(key[counter])-65))%26+65)
                counter = (counter+1)%len(key)
        return ''.join(decrypted)


    def analyse(self):
        """
        Display general information about analysed text
        """

        print "[*] ANALYSIS\n"
        print "    [+] Size"
        print "    " + str(self.get_len()) + " chars"

        print "\n    [+] Number of unique chars"
        print "    " + str(self.get_number_of_different_char())
        r = list(set(self.s))
        r.sort()
        print "    " + str(r)

        print "\n    [+] Most common frequencies"
        print "    " + str(self.get_most_common_frequencies(n=1, m=5))

        print "\n    [+] Double letters frequencies"
        print "    " + str(self.get_double_letters_frequencies())

        print "\n    [+] IC"
        print "    " + str(self.get_ic())

        print ""


# ---------------------------------- PRIVATE ----------------------------------


    def _set_len(self):
        """
        Set len of analysed text
        """

        return len(self.s)


    def _clean_string(self, s, keep_spaces=False):
        s = s.lower().replace("’", "").replace("é","e").replace("è","e").replace("ê","e").replace("ë","e").replace("à","a").replace("ç","c").replace("Ç", "c").replace(".","").replace(",","").replace("?","").replace("!","").replace(":","").replace(";","").replace("-","").replace("'","").replace("\"","").replace("(","").replace(")","").replace("ù","u").replace("ô","o").replace("ü","u")
        if not keep_spaces:
            s = s.replace(" ","")
        return s.upper()


    def _guess_key_length(self, min_len=1, max_len=9, display=False):
        """
        Guess key length in case of Vigenere cipher based on frequence analysis
        """

        res = {}
        max_ic = 0
        # We try different key lengths
        for i in range(min_len, max_len+1):

            if self.len < i*2:
                continue
            ics = []
            for j in range(i):
                var = []
                for k in range(self.len//i):
                    var.append(self.s[k*i + j])
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


    def _guess_key(self, min_len=1, max_len=9, display=False):
        keylen = self._guess_key_length(min_len, max_len, display)
        print "[*] Most probable key length : " + str(keylen) + "\n"
        freq_fr = {'e': 14.715, 's': 7.948, 'a': 7.636, 'i': 7.529, 't': 7.244, 'n': 7.095, 'r': 6.553, 'u': 6.311, 'l': 5.456, 'o': 5.378, 'd': 3.669, 'c': 3.260, 'p': 3.021, 'm': 2.968, 'v': 1.628, 'q': 1.362, 'f': 1.066, 'b': 0.901, 'g': 0.866, 'h': 0.737, 'j': 0.545, 'x': 0.387, 'y': 0.308, 'z': 0.136, 'w': 0.114, 'k': 0.049}
        password = ""
        for i in range(keylen):
            sub_alphabet = Text(''.join([self.s[keylen*j + i] for j in range(self.len//keylen)]))
            min_differential = 99999
            password_letter = ""
            for c in range(65, 65+26):
                decrypted = Text(sub_alphabet.vigenere_decrypt(chr(c)))
                freq_s = { k:round((v/decrypted.len)*100, 3) for k,v in dict(decrypted.get_frequencies()).items()}
                differential = sum([abs(freq_fr[k.lower()]-v) for k,v in freq_s.items()])
                if differential < min_differential:
                    min_differential = differential
                    password_letter = chr(c)
            password += password_letter
        return password

if __name__ == "__main__":
    # French text example from http://blog.hackndo.com/retour-a-la-libc/
    text = Text("Bonjour, nous avons vu dans la série d’articles précédents comment fonctionnait la mémoire d’un processus au sein d’un système Unix. Grâce à cette compréhension, nous avons exposé une vulnérabilité très connue qu’est le dépassement de tampon en utilisant la pile (buffer overflow stack based). Pour rappel, le buffer overflow est une vulnérabilité présente lorsque le programmeur ne vérifie pas la taille d’une variable fournie par l’utilisateur, et qu’il stocke cette variable en mémoire. Il est alors possible pour l’attaquant d’entrer une valeur de taille supérieure à ce qui était prévu, et lorsque cette valeur (appelée buffer) est copiée en mémoire, elle dépasse de l’espace qui lui était alloué (dépassement de tampon). Cela peut engendrer une erreur de segmentation car ce dépassement va probablement écraser la sauvegarde du registre EIP (sauvegarde effectuée afin que lorsque la fonction en cours se termine, le processeur retrouve l’adresse de l’instruction suivant l’appel de cette fonction), donc comme EIP est partiellement ou totalement écrasé, les chances sont fortes pour que cette nouvelle valeur pointe soit vers une zone mémoire non autorisée en lecture, soit vers zone mémoire contenant des instructions non valides. Cependant, si l’attaquant fourni une adresse mémoire soigneusement choisie pour pointer vers un code malveillant (placé dans le buffer, dans nos exemples précédents, d’où le stack based), alors le flow d’exécution du programme peut être modifié, et l’attaquant peut faire ce qu’on appelle une escalade de privilèges (sous réserve que le programme en question appartenait à une utilisateur avec des droits plus élevés et que le programme était SUID, c’est à dire qu’il s’exécutait avec les droits du propriétaire de ce logiciel)", keep_spaces=False)
    text.analyse()
    text.set_text(text.vigenere_encrypt("hackndo"))
    print text.vigenere_decrypt(min_len=1, max_len=10, display=True)