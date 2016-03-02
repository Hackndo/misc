# pytools
List of python tools I wrote 

### Text

Example

```python
# French truncated text example from http://blog.hackndo.com/retour-a-la-libc/
text = Text("Bonjour, nous avons vu dans la série [...])", keep_spaces=False)
text.analyse()
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
```

### VigenereCipher

Example

```python
# French truncated text example from http://blog.hackndo.com/retour-a-la-libc/
p = VigenereCipher("Salut les amis, je suis parti [..]")
p.key = "hackndo"
p.encipher()
p.decrypt(max_len=20, display=True)
print p.tostring()
```

Result

```
[+] Visual key length IC correspondance
1  |||||||||||||||||||||
2  |||||||||||||||||||||
3  |||||||||||||||||||||
4  |||||||||||||||||||||
5  |||||||||||||||||||||
6  |||||||||||||||||||||
7  |||||||||||||||||||||||||||||||||||||||
8  |||||||||||||||||||||
9  |||||||||||||||||||||
10 |||||||||||||||||||||
11 |||||||||||||||||||||
12 ||||||||||||||||||||
13 |||||||||||||||||||||
14 ||||||||||||||||||||||||||||||||||||||||
15 ||||||||||||||||||||||
16 |||||||||||||||||||||
17 ||||||||||||||||||||||
18 ||||||||||||||||||||
19 ||||||||||||||||||||
20 |||||||||||||||||||||

[*] Most probable key length : 14

[*] [UPDATE] Most probable key length : 7

[*] Most probable key : HACKNDO

[*] Decryption complete
SALUTLESAMISJESUISPARTIENAM [...]
```

### BeaufortCipher

Example

```python
# French truncated text example from http://blog.hackndo.com/retour-a-la-libc/
p = BeaufortCipher("Salut les amis, je suis parti [..]")
p.key = "hackndo"
p.encipher()
p.decrypt(max_len=20, display=True)
print p.tostring()
```

Result

```
[+] Visual key length IC correspondance
1  |||||||||||||||||||||
2  |||||||||||||||||||||
3  |||||||||||||||||||||
4  |||||||||||||||||||||
5  |||||||||||||||||||||
6  |||||||||||||||||||||
7  |||||||||||||||||||||||||||||||||||||||
8  |||||||||||||||||||||
9  |||||||||||||||||||||
10 |||||||||||||||||||||
11 |||||||||||||||||||||
12 ||||||||||||||||||||
13 |||||||||||||||||||||
14 ||||||||||||||||||||||||||||||||||||||||
15 |||||||||||||||||||||
16 ||||||||||||||||||||
17 |||||||||||||||||||||
18 ||||||||||||||||||||
19 ||||||||||||||||||||
20 |||||||||||||||||||||

[*] Most probable key length : 14

[*] [UPDATE] Most probable key length : 7

[*] Most probable key : HACKNDO

[*] Decryption complete
SALUTLESAMISJESUISPARTIENAM [...]
```

### PolybeCipher

Example

```python
# French truncated text example from http://blog.hackndo.com/retour-a-la-libc/
p = PolybeCipher("Salut les amis, je suis parti [..]")
p.key = "hackndo"
p.encipher()
print p.tostring()
```

Result

```
[*] Keysquare initialized
    H A C K N
    D O B E F
    G I J L M
    P Q R S T
    U V X Y Z

[*] Encipher complete

RVITSINRVJERFNRTERMVQSENKVJNQEPTNOTRTO [...]
```

