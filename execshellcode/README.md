# Converter

### Version
1.0.0

### Compile
**32 bits shellcodes**
```sh
$ gcc -Wall -m32 -Wl,-z,execstack -o execshellcode32 execshellcode.c
```
**64 bits shellcodes**
```sh
$ gcc -Wall -Wl,-z,execstack -o execshellcode64 execshellcode.c
```

### Usage

```sh
$ ./execshellcode <shellcode>
```

### Examples
**32 bits shellcodes**
```sh
$ ./execshellcode32 "31 c0 50 68 2f 2f 73 68 68 2f 62 69 6e 89 e3 89 c1 89 c2 b0 0b cd 80 31 c0 40 cd 80"
Shellcode Length: 28
$ exit
$ ./execshellcode32 "0x31 0xc0 0x50 0x68 0x2f 0x2f 0x73 0x68 0x68 0x2f 0x62 0x69 0x6e 0x89 0xe3 0x89 0xc1 0x89 0xc2 0xb0 0x0b 0xcd 0x80 0x31 0xc0 0x40 0xcd 0x80"
Shellcode Length: 28
$ exit
$ ./execshellcode32 "\x31 \xc0 \x50 \x68 \x2f \x2f \x73 \x68 \x68 \x2f \x62 \x69 \x6e \x89 \xe3 \x89 \xc1 \x89 \xc2 \xb0 \x0b \xcd \x80 \x31 \xc0 \x40 \xcd \x80"
Shellcode Length: 28
$ exit
$ ./execshellcode32 "\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x89\xc1\x89\xc2\xb0\x0b\xcd\x80\x31\xc0\x40\xcd\x80"
Shellcode Length: 28
$ exit
$ 
```
**64 bits shellcodes**
```sh
$ ./execshellcode64 "\x31\xc0\x48\xbb\xd1\x9d\x96\x91\xd0\x8c\x97\xff\x48\xf7\xdb\x53\x54\x5f\x99\x52\x57\x54\x5e\xb0\x3b\x0f\x05"
Shellcode Length: 27
$ exit
$

```

