# pytools
List of python tools I wrote 

### Text

```python
# French truncated text example from http://blog.hackndo.com/retour-a-la-libc/
text = Text("Bonjour, nous avons vu dans la série [...])", keep_spaces=False)
text.analyse()
text.set_text(text.vigenere_encrypt("hackndo"))
print text.vigenere_decrypt(min_len=1, max_len=10, display=True)
```

Result

```
[*] ANALYSIS

    [+] Size
    1444 chars

    [+] Number of unique chars
    28
    ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '\xa2', '\xc3']

    [+] Most common frequencies
    [('E', 271), ('T', 108), ('A', 103), ('S', 103), ('R', 103)]

    [+] Double letters frequencies
    Counter({'EE': 16, 'SS': 12, 'LL': 9, 'TT': 8, 'MM': 6, 'PP': 5, 'FF': 5, 'NN': 3, 'RR': 3, 'CC': 1})

    [+] IC
    0.0801

[*] Will try to decrypt based on frequence analysis

[+] Visual key length IC correspondance
1  ||||||||||||||||||||||
2  |||||||||||||||||||||
3  ||||||||||||||||||||||
4  |||||||||||||||||||||
5  ||||||||||||||||||||||
6  |||||||||||||||||||||
7  ||||||||||||||||||||||||||||||||||||||||
8  |||||||||||||||||||||
9  |||||||||||||||||||||
10 ||||||||||||||||||||||

[*] Most probable key length : 7

[*] Most probable key : HACKNDO

BONJOURNOUSAVONSVUDANSLASERIE [...]
```

### Usage

```sh
$ ./findaddr <variable>
```

### Examples

```sh
$ ./findaddr SHELL
SHELL address: 0x7fff0417d64c
```
