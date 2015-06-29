/*
 * Execute given shellcode
 * Compile :
 * $ gcc -Wall -m32 -Wl,-z,execstack -o shellcode shellcode.c
 * Usage :
 * $ ./execshellcode $(perl -e 'print "<shellcode>"')
 * Example (from http://shell-storm.org/shellcode/files/shellcode-827.php):
 * $ ./execshellcode $(perl -e 'print "\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\xb0\x0b\xcd\x80"')
 * $
 */

#include<stdio.h>
#include<string.h>
int main(int argc, char **argv)
{
    if (argc != 2) {
        printf("Usage : %s <shellcode>\n", argv[0]);
        return 1;
    }
    printf("Shellcode Length: %zd\n", strlen(argv[1]));
    int (*ret)() = (int(*)())argv[1];
    ret();
    return 0;
}
