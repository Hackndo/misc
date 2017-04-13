import re
import json
import configparser as cp

DEBUG = True

class Utils(object):
    """
    Check if at least on element of el1 is in el2
    """
    @staticmethod
    def has_one_in_common(el1, el2):
        if isinstance(el1, list) and isinstance(el2, list):
            return any(str(c) in [str(d) for d in el2] for c in el1)
        elif isinstance(el2, list):
            return str(el1) in [str(c) for c in el2]
        elif isinstance(el1, list):
            return any(str(c)==str(el2) for c in el1)
        else:
            return str(el1) == str(el2)

    @staticmethod
    def is_higher_than(el1,el2):
        return int(el1) >= int(el2)
    
    @staticmethod
    def is_lower_than(el1,el2):
        return int(el1) <= int(el2)


    @staticmethod
    def log(s, force=False):
        if DEBUG or force:
            print(s)

class Settings(object):
    def __init__(self, config_file, sep=","):
        _config = cp.ConfigParser()
        _config.read(config_file)
        self.config = {}
        for section in _config.sections():
            self.config[section] = {}
            for criteria, value in _config[section].items():
                if criteria == "cs":
                    self.config[section][criteria] = True if value == "1" else False
                if sep in value:
                    self.config[section][criteria] = value.split(sep)
                else:
                    self.config[section][criteria] = value

class Cryde(object):
    def __init__(self, cipher, config_file="config.ini"):
        self.cipher = cipher
        self.settings = Settings(config_file=config_file)


    def get_possible_algorithms(self):
        result = []
        for section in self.settings.config.keys():
            Utils.log("[*] " + section)
            if self.is_valid(section):
                Utils.log("\t[OK] ")
                result.append(section)
            else:
                Utils.log("\t[KO] ")
        result.sort()
        return result
    
    def is_valid(self, section):
        # TODO : Implement case sensitive from config file
        for criteria, value in self.settings.config[section].items():
            if criteria.startswith("min_"):
                criteria = criteria.replace("min_","")
                checker = Utils.is_higher_than
            elif criteria.startswith("max_"):
                criteria = criteria.replace("max_","")
                checker = Utils.is_lower_than
            else:
                checker = Utils.has_one_in_common

            try:
                c_criteria = getattr(self.cipher,criteria)
                if not checker(c_criteria, value):
                    Utils.log("\t[-] " + criteria + " = " + str(value))
                    return False
                Utils.log("\t[+] " + criteria + " = " + str(value))
            except AttributeError:
                Utils.log("\t[!] Criteria " + criteria + " inexistant")
        
        return True


class Cipher(object):
    def __init__(self, s, *args, **kwargs):
        self.keep_spaces = kwargs.get("spaces", True)
        self.keep_ponctuation = kwargs.get("ponctuation", True)
        self.s = self.sanitize(s)
        self.length = self.get_length()
        self.length_divisors = self.get_length_divisors()
        self.unique_symbols_ci = self.get_unique_symbols(ci=True)
        self.unique_symbols_cs = self.get_unique_symbols(ci=False)
        self.unique_symbols_ci_count = self.get_unique_symbols_count(ci=True)
        self.unique_symbols_cs_count = self.get_unique_symbols_count(ci=False)
        self.possible_bases = self.get_possible_bases()

    def __str__(self):
        output = "[*] Options\n"
        output += "\t[+] Keep spaces : " + ("True" if self.keep_spaces else "False") + "\n"
        output += "\t[+] Keep ponctuation : " + ("True" if self.keep_ponctuation else "False") + "\n"
        output += "[*] Analytics (CI : Case Insensitive | CS : Case Insensitive)\n"
        output += "\t[+] String : ->" + self.s + "<-\n"
        output += "\t[+] Length : " + str(self.length) + "\n"
        output += "\t[+] Length divisors : " + str(self.length_divisors) + "\n"
        output += "\t[+] Unique symbols (CI): " + str(self.unique_symbols_ci) + "\n"
        output += "\t[+] Unique symbols count (CI): " + str(self.unique_symbols_ci_count) + "\n"
        output += "\t[+] Unique symbols (CS): " + str(self.unique_symbols_cs) + "\n"
        output += "\t[+] Unique symbols count (CS): " + str(self.unique_symbols_cs_count) + "\n"
        output += "\t[+] Possible bases : " + str(self.possible_bases) + "\n"
        return output

    def get_length(self):
        return len(self.s)

    def get_length_divisors(self):
        return [str(i) for i in range(2, self.length) if self.length%i == 0]


    def get_unique_symbols(self, ci=True):
        result = list(set([c.lower() if ci else c for c in self.s]))
        result.sort()
        return result

    def get_unique_symbols_count(self, ci=True):
        return len(self.unique_symbols_ci) if ci else len(self.unique_symbols_cs)

    def get_possible_bases(self):
        
        bases = {
            "2": {
                "ci": False,
                "chars": ['0','1']
            },
            "8": {
                "ci": False,
                "chars": ['0','1','2','3','4','5','6','7']
            },
            "16": {
                "ci": True,
                "chars": ['0','1','2','3','4','5','6','7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
            },
            "26": {
                "ci": True,
                "chars": ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
            },
            "32": {
                "ci": True,
                "chars": ['2','3','4','5','6','7','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '=']
            },
            "36": {
                "ci": True,
                "chars": ['0','1','2','3','4','5','6','7','8','9','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
            },
            "52": {
                "ci": False,
                "chars": ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
            },
            "62": {
                "ci": False,
                "chars": ['0','1','2','3','4','5','6','7','8','9','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
            },
            "64": {
                "ci": False,
                "chars": ['/','=','0','1','2','3','4','5','6','7','8','9','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
            }
        }

        possible_bases = []
        for base_k, base in bases.items():
            if all(c.lower() in base["chars"] if base["ci"] else c in base["chars"] for c in self.s):
                possible_bases.append(base_k)
        possible_bases.sort()
        return possible_bases


    def sanitize(self, s):
        if not self.keep_ponctuation:
            s = re.compile('[^a-zA-Z0-9 ]').sub('', s)
        return s if self.keep_spaces else s.replace(" ", "")


def main():
    config_file = "./config.ini"
    ciphers = [
        Cipher("019cf44a019cf44a019cf44a019cf44a", spaces=False),
        Cipher("--. .--. ---", spaces=False),
        Cipher("JBSWY3DPEB3W64TMMQ======", spaces=False),
    ]
    for cipher in ciphers:
        print("\n======= NEW CIPHER ========\n")
        print(cipher)
        c = Cryde(cipher=cipher, config_file=config_file)
        print("Results : " + str(c.get_possible_algorithms()) + "\n")
    

if __name__ == '__main__':
    main()
