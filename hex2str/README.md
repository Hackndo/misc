# Hex2Str
Converts hex ascii to string (usefull for printing special chars for shellcodes)

### Version
1.0.0

### Compile
```sh
$ gcc -Wall -o hex2str hex2str.c
```

### Usage

```sh
$ ./hex2str <hex_string>
```

### Examples

```sh
$ ./hex2str "68 61 63 6b 6e 64 6f"
hackndo
$ ./hex2str "0x68 0x61 0x63 0x6b 0x6e 0x64 0x6f"
hackndo
$ ./hex2str "\x68 \x61 \x63 \x6b \x6e \x64 \x6f"
hackndo
$ ./hex2str "\x68\x61\x63\x6b\x6e\x64\x6f"
hackndo

```
