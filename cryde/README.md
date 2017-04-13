# CRYDE - CRYpto DEtector

This tool aims to detect which kind of algorithm was used to produce a hash/cipher/checksum

### Requirements

Python3.5+

### Example

```sh
pixis@hackndo:~/cryde $ python cryde.py

======= NEW CIPHER ========

[*] Options
	[+] Keep spaces : False
	[+] Keep ponctuation : True
[*] Analytics (CI : Case Insensitive | CS : Case Insensitive)
	[+] String : ->019cf44a019cf44a019cf44a019cf44a<-
	[+] Length : 32
	[+] Length divisors : ['2', '4', '8', '16']
	[+] Unique symbols (CI): ['0', '1', '4', '9', 'a', 'c', 'f']
	[+] Unique symbols count (CI): 7
	[+] Unique symbols (CS): ['0', '1', '4', '9', 'a', 'c', 'f']
	[+] Unique symbols count (CS): 7
	[+] Possible bases : ['16', '36', '62', '64']

[*] md5
	[+] possible_bases = 16
	[+] length = 32
	[OK] 
[*] Decimal
	[+] length_divisors = 2
	[-] possible_bases = 10
	[KO] 
[*] TWOFISH
	[+] possible_bases = 16
	[-] length_divisors = 32
	[KO] 
[*] sha-224
	[+] possible_bases = 16
	[-] length = 40
	[KO] 
[*] Octodecimal
	[-] possible_bases = 8
	[KO] 
[*] 3DES
	[+] possible_bases = 16
	[+] length_divisors = 16
	[OK] 
[*] Binary
	[-] possible_bases = 2
	[KO] 
[*] sha-256
	[+] possible_bases = 16
	[-] length = 64
	[KO] 
[*] Vigenere
	[+] possible_bases = ['26', '36', '52', '56']
	[OK] 
[*] AES
	[+] possible_bases = 16
	[-] length_divisors = 32
	[KO] 
[*] CRC-32
	[+] possible_bases = 16
	[+] length = 32
	[OK] 
[*] CRC-64
	[+] possible_bases = 16
	[-] length = 64
	[KO] 
[*] sha-512
	[+] possible_bases = 16
	[-] length = 128
	[KO] 
[*] MISTY
	[+] possible_bases = 16
	[+] length_divisors = 16
	[OK] 
[*] polybe
	[-] possible_bases = 26
	[KO] 
[*] CRC-16
	[+] possible_bases = 16
	[-] length = 16
	[KO] 
[*] Hexadecimal
	[+] length_divisors = 2
	[+] possible_bases = 16
	[OK] 
[*] b64
	[+] length_divisors = 4
	[+] possible_bases = 64
	[OK] 
[*] Wolseley
	[-] possible_bases = 26
	[KO] 
[*] Rail Fence
	[-] possible_bases = 26
	[KO] 
[*] md2
	[+] possible_bases = 16
	[+] length = 32
	[OK] 
[*] md4
	[+] possible_bases = 16
	[+] length = 32
	[OK] 
[*] md6
	[+] possible_bases = 16
	[-] length = 128
	[KO] 
[*] sha-384
	[+] possible_bases = 16
	[-] length = 96
	[KO] 
[*] sha-1
	[+] possible_bases = 16
	[-] length = 40
	[KO] 
[*] morse
	[-] unique_symbols_ci = ['-', '.']
	[KO] 
[*] ROT13
	[-] possible_bases = 26
	[KO] 
[*] DES
	[+] possible_bases = 16
	[+] length_divisors = 16
	[OK] 
[*] b32
	[+] length_divisors = 8
	[-] possible_bases = 32
	[KO] 
Results : ['3DES', 'CRC-32', 'DES', 'Hexadecimal', 'MISTY', 'Vigenere', 'b64', 'md2', 'md4', 'md5']


======= NEW CIPHER ========

[*] Options
	[+] Keep spaces : False
	[+] Keep ponctuation : True
[*] Analytics (CI : Case Insensitive | CS : Case Insensitive)
	[+] String : ->--..--.---<-
	[+] Length : 10
	[+] Length divisors : ['2', '5']
	[+] Unique symbols (CI): ['-', '.']
	[+] Unique symbols count (CI): 2
	[+] Unique symbols (CS): ['-', '.']
	[+] Unique symbols count (CS): 2
	[+] Possible bases : []

[*] md5
	[-] possible_bases = 16
	[KO] 
[*] Decimal
	[+] length_divisors = 2
	[-] possible_bases = 10
	[KO] 
[*] TWOFISH
	[-] possible_bases = 16
	[KO] 
[*] sha-224
	[-] possible_bases = 16
	[KO] 
[*] Octodecimal
	[-] possible_bases = 8
	[KO] 
[*] 3DES
	[-] possible_bases = 16
	[KO] 
[*] Binary
	[-] possible_bases = 2
	[KO] 
[*] sha-256
	[-] possible_bases = 16
	[KO] 
[*] Vigenere
	[-] possible_bases = ['26', '36', '52', '56']
	[KO] 
[*] AES
	[-] possible_bases = 16
	[KO] 
[*] CRC-32
	[-] possible_bases = 16
	[KO] 
[*] CRC-64
	[-] possible_bases = 16
	[KO] 
[*] sha-512
	[-] possible_bases = 16
	[KO] 
[*] MISTY
	[-] possible_bases = 16
	[KO] 
[*] polybe
	[-] possible_bases = 26
	[KO] 
[*] CRC-16
	[-] possible_bases = 16
	[KO] 
[*] Hexadecimal
	[+] length_divisors = 2
	[-] possible_bases = 16
	[KO] 
[*] b64
	[-] length_divisors = 4
	[KO] 
[*] Wolseley
	[-] possible_bases = 26
	[KO] 
[*] Rail Fence
	[-] possible_bases = 26
	[KO] 
[*] md2
	[-] possible_bases = 16
	[KO] 
[*] md4
	[-] possible_bases = 16
	[KO] 
[*] md6
	[-] possible_bases = 16
	[KO] 
[*] sha-384
	[-] possible_bases = 16
	[KO] 
[*] sha-1
	[-] possible_bases = 16
	[KO] 
[*] morse
	[+] unique_symbols_ci = ['-', '.']
	[OK] 
[*] ROT13
	[-] possible_bases = 26
	[KO] 
[*] DES
	[-] possible_bases = 16
	[KO] 
[*] b32
	[-] length_divisors = 8
	[KO] 
Results : ['morse']


======= NEW CIPHER ========

[*] Options
	[+] Keep spaces : False
	[+] Keep ponctuation : True
[*] Analytics (CI : Case Insensitive | CS : Case Insensitive)
	[+] String : ->JBSWY3DPEB3W64TMMQ======<-
	[+] Length : 24
	[+] Length divisors : ['2', '3', '4', '6', '8', '12']
	[+] Unique symbols (CI): ['3', '4', '6', '=', 'b', 'd', 'e', 'j', 'm', 'p', 'q', 's', 't', 'w', 'y']
	[+] Unique symbols count (CI): 15
	[+] Unique symbols (CS): ['3', '4', '6', '=', 'B', 'D', 'E', 'J', 'M', 'P', 'Q', 'S', 'T', 'W', 'Y']
	[+] Unique symbols count (CS): 15
	[+] Possible bases : ['32', '64']

[*] md5
	[-] possible_bases = 16
	[KO] 
[*] Decimal
	[+] length_divisors = 2
	[-] possible_bases = 10
	[KO] 
[*] TWOFISH
	[-] possible_bases = 16
	[KO] 
[*] sha-224
	[-] possible_bases = 16
	[KO] 
[*] Octodecimal
	[-] possible_bases = 8
	[KO] 
[*] 3DES
	[-] possible_bases = 16
	[KO] 
[*] Binary
	[-] possible_bases = 2
	[KO] 
[*] sha-256
	[-] possible_bases = 16
	[KO] 
[*] Vigenere
	[-] possible_bases = ['26', '36', '52', '56']
	[KO] 
[*] AES
	[-] possible_bases = 16
	[KO] 
[*] CRC-32
	[-] possible_bases = 16
	[KO] 
[*] CRC-64
	[-] possible_bases = 16
	[KO] 
[*] sha-512
	[-] possible_bases = 16
	[KO] 
[*] MISTY
	[-] possible_bases = 16
	[KO] 
[*] polybe
	[-] possible_bases = 26
	[KO] 
[*] CRC-16
	[-] possible_bases = 16
	[KO] 
[*] Hexadecimal
	[+] length_divisors = 2
	[-] possible_bases = 16
	[KO] 
[*] b64
	[+] length_divisors = 4
	[+] possible_bases = 64
	[OK] 
[*] Wolseley
	[-] possible_bases = 26
	[KO] 
[*] Rail Fence
	[-] possible_bases = 26
	[KO] 
[*] md2
	[-] possible_bases = 16
	[KO] 
[*] md4
	[-] possible_bases = 16
	[KO] 
[*] md6
	[-] possible_bases = 16
	[KO] 
[*] sha-384
	[-] possible_bases = 16
	[KO] 
[*] sha-1
	[-] possible_bases = 16
	[KO] 
[*] morse
	[-] unique_symbols_ci = ['-', '.']
	[KO] 
[*] ROT13
	[-] possible_bases = 26
	[KO] 
[*] DES
	[-] possible_bases = 16
	[KO] 
[*] b32
	[+] length_divisors = 8
	[+] possible_bases = 32
	[OK] 
Results : ['b32', 'b64']

```
