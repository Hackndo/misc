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

[*] TWOFISH
	[-] length_divisors = 32
	[KO] 
[*] CRC-16
	[-] length = 16
	[KO] 
[*] ROT13
	[-] possible_bases = 26
	[KO] 
[*] sha-224
	[-] length = 40
	[KO] 
[*] md5
	[+] length = 32
	[+] possible_bases = 16
	[OK] 
[*] morse
	[-] unique_symbols_ci = ['-', '.']
	[KO] 
[*] DES
	[+] length_divisors = 16
	[+] possible_bases = 16
	[OK] 
[*] md4
	[+] length = 32
	[+] possible_bases = 16
	[OK] 
[*] sha-1
	[-] length = 40
	[KO] 
[*] b64
	[+] length_divisors = 4
	[+] possible_bases = 64
	[OK] 
[*] md2
	[+] length = 32
	[+] possible_bases = 16
	[OK] 
[*] AES
	[-] length_divisors = 32
	[KO] 
[*] sha-384
	[-] length = 96
	[KO] 
[*] MISTY
	[+] length_divisors = 16
	[+] possible_bases = 16
	[OK] 
[*] polybe
	[+] unique_symbols_ci_count = 25
	[-] possible_bases = 26
	[KO] 
[*] sha-512
	[-] length = 128
	[KO] 
[*] Wolseley
	[+] unique_symbols_ci_count = 25
	[-] possible_bases = 26
	[KO] 
[*] 3DES
	[+] length_divisors = 16
	[+] possible_bases = 16
	[OK] 
[*] md6
	[-] length = 128
	[KO] 
[*] sha-256
	[-] length = 64
	[KO] 
[*] CRC-64
	[-] length = 64
	[KO] 
[*] Vigenere
	[+] possible_bases = ['26', '36', '52', '56']
	[OK] 
[*] Rail Fence
	[-] possible_bases = 26
	[KO] 
[*] CRC-32
	[+] length = 32
	[+] possible_bases = 16
	[OK] 
Results : ['3DES', 'CRC-32', 'DES', 'MISTY', 'Vigenere', 'b64', 'md2', 'md4', 'md5']


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

[*] TWOFISH
	[-] length_divisors = 32
	[KO] 
[*] CRC-16
	[-] length = 16
	[KO] 
[*] ROT13
	[-] possible_bases = 26
	[KO] 
[*] sha-224
	[-] length = 40
	[KO] 
[*] md5
	[-] length = 32
	[KO] 
[*] morse
	[+] unique_symbols_ci = ['-', '.']
	[OK] 
[*] DES
	[-] length_divisors = 16
	[KO] 
[*] md4
	[-] length = 32
	[KO] 
[*] sha-1
	[-] length = 40
	[KO] 
[*] b64
	[-] length_divisors = 4
	[KO] 
[*] md2
	[-] length = 32
	[KO] 
[*] AES
	[-] length_divisors = 32
	[KO] 
[*] sha-384
	[-] length = 96
	[KO] 
[*] MISTY
	[-] length_divisors = 16
	[KO] 
[*] polybe
	[+] unique_symbols_ci_count = 25
	[-] possible_bases = 26
	[KO] 
[*] sha-512
	[-] length = 128
	[KO] 
[*] Wolseley
	[+] unique_symbols_ci_count = 25
	[-] possible_bases = 26
	[KO] 
[*] 3DES
	[-] length_divisors = 16
	[KO] 
[*] md6
	[-] length = 128
	[KO] 
[*] sha-256
	[-] length = 64
	[KO] 
[*] CRC-64
	[-] length = 64
	[KO] 
[*] Vigenere
	[-] possible_bases = ['26', '36', '52', '56']
	[KO] 
[*] Rail Fence
	[-] possible_bases = 26
	[KO] 
[*] CRC-32
	[-] length = 32
	[KO] 
Results : ['morse']


======= NEW CIPHER ========

[*] Options
	[+] Keep spaces : False
	[+] Keep ponctuation : True
[*] Analytics (CI : Case Insensitive | CS : Case Insensitive)
	[+] String : ->019cf44a019cf44a019cf44a019cf44a019cf44a019cf44<-
	[+] Length : 47
	[+] Length divisors : []
	[+] Unique symbols (CI): ['0', '1', '4', '9', 'a', 'c', 'f']
	[+] Unique symbols count (CI): 7
	[+] Unique symbols (CS): ['0', '1', '4', '9', 'a', 'c', 'f']
	[+] Unique symbols count (CS): 7
	[+] Possible bases : ['16', '36', '62', '64']

[*] TWOFISH
	[-] length_divisors = 32
	[KO] 
[*] CRC-16
	[-] length = 16
	[KO] 
[*] ROT13
	[-] possible_bases = 26
	[KO] 
[*] sha-224
	[-] length = 40
	[KO] 
[*] md5
	[-] length = 32
	[KO] 
[*] morse
	[-] unique_symbols_ci = ['-', '.']
	[KO] 
[*] DES
	[-] length_divisors = 16
	[KO] 
[*] md4
	[-] length = 32
	[KO] 
[*] sha-1
	[-] length = 40
	[KO] 
[*] b64
	[-] length_divisors = 4
	[KO] 
[*] md2
	[-] length = 32
	[KO] 
[*] AES
	[-] length_divisors = 32
	[KO] 
[*] sha-384
	[-] length = 96
	[KO] 
[*] MISTY
	[-] length_divisors = 16
	[KO] 
[*] polybe
	[+] unique_symbols_ci_count = 25
	[-] possible_bases = 26
	[KO] 
[*] sha-512
	[-] length = 128
	[KO] 
[*] Wolseley
	[+] unique_symbols_ci_count = 25
	[-] possible_bases = 26
	[KO] 
[*] 3DES
	[-] length_divisors = 16
	[KO] 
[*] md6
	[-] length = 128
	[KO] 
[*] sha-256
	[-] length = 64
	[KO] 
[*] CRC-64
	[-] length = 64
	[KO] 
[*] Vigenere
	[+] possible_bases = ['26', '36', '52', '56']
	[OK] 
[*] Rail Fence
	[-] possible_bases = 26
	[KO] 
[*] CRC-32
	[-] length = 32
	[KO] 
Results : ['Vigenere']

```
