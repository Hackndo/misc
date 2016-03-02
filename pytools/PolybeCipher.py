# coding: utf-8
from __future__ import division
from KeyCipher import KeyCipher
from Substitution import Substitution

class PolybeCipher(Substitution, KeyCipher):

    _keysquare = None

    def __init__(self, s, size_element=1, keep_spaces=False):
        Substitution.__init__(self, s, size_element, keep_spaces)
        self.s = [c.replace("W","V") for c in self.s]
        self.reference_alphabet = "ABCDEFGHIJKLMNOPQRSTUVXYZ"

    @property
    def keysquare(self):
        if self._keysquare is None:
            self.__initialize_keysquare()
        return self._keysquare
    

    def __initialize_keysquare(self):
        self.key = self.key.replace("W", "V")
        l = [c for c in self.reference_alphabet]
        self._keysquare = [['']*5 for i in range(5)]
        for i in range(len(self.key)):
            self._keysquare[i//5][i%5] = self.key[i]
            l.remove(self.key[i])
        for i in range(len(self.key), 25):
            self._keysquare[i//5][i%5] = l[i-len(self.key)]
        print "[*] Keysquare initialized"
        for row in self._keysquare:
            print "    " + ' '.join(row)
        print ""
    
    def encipher(self):
        self.__initialize_keysquare()
        self.substitute_alphabet = ''.join([''.join(r) for r in self.keysquare])
        self.substitute()
        print "[*] Encipher complete\n"


if __name__ == "__main__":
    p = PolybeCipher("Salut les amis, je suis parti en amerique du sud parce que je trouvais que l'endroit etait super sympa. Vous en pensez quoi ? Moi je trouve que c'est une idée géniale. Le voyage, tout le monde le sait, ça permet de fait de nouvelles rencontres, notamment la rencontre avec soi-même. Le voyage, tout le monde le sait, ça permet de découvrir le monde, de découvrir de nouvelles villes, de nouveaux villages, de nouveaux paysages. Le voyage, tout le monde le sait, ça permet de s'ouvrir à de nouvelles cultures, de nouvelles traditions, de nouvelles manières de vivre.  Ça, tout le monde le sait.  Mais pour moi, il y a quelque chose d'autre. Quelque chose que souvent j'oublie, que souvent je ne remarque pas, que souvent je néglige. Le voyage, je ne le savais pas, ça permet de me rendre compte que ma ville, Paris, est belle.  Paris, et tous ses quartiers plein de cafés aux multiples tintements de tasses, de terasses calmes sous les rayons de soleil, d'odeurs de baguettes sorties du four, de pavés authentiques, de façades aux magnifiques allures Hausmaniennes, de grandes portes en bois, de ruelles biscornues abritant des endroits secrets, de pont majestueux surplombant la Seine, de collines, de quais piétons aux plus grand plaisir des amoureux, de canaux promptent à des promenades dominicales sous les arbres en fleurs, de fleuristes aux coins de rues desquels émanent ces odeurs délicieuses, de vie, tout simplement.")
    p.key = "HACKNDO"
    p.encipher()
    print p.tostring()
