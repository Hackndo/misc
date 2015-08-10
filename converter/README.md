# Converter

### Version
1.0.0

### Compile
Go to `converter` directory then run `make`

```sh
$ git clone https://github.com/Hackndo/misc.git
$ cd misc/converter
$ make
```

### Usage

```sh
$ ./converter number [from_base] to_base
```

### Help
```sh
$ ./converter -h
```

### Examples
```sh
$ ./converter 0x1c 10
1c from base 16 to base 10
28
$ ./converter 0b1001 16
1001 from base 2 to base 16
9
$ ./converter ab7Z 62 8
ab7Z from base 62 to base 8
41214111
$ ./converter hackndo 36 10
hackndo from base 36 to base 10
3763108020
```

