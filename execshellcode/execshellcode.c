/*
 * Execute given shellcode
 * Compile :
 * $ gcc -Wall -m32 -Wl,-z,execstack -o execshellcode execshellcode.c
 * Usage :
 * $ ./execshellcode <shellcode>
 * Example (from http://shell-storm.org/shellcode/files/shellcode-811.php):
 * hackndo@hackndo:~ $ ./execshellcode "\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x89\xc1\x89\xc2\xb0\x0b\xcd\x80\x31\xc0\x40\xcd\x80"
 * Shellcode Length: 28
 * $ 
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char *hex2str(char *str);
int char_count(char *str, char search);
char *str_replace(char *orig, char *rep, char *with);

int main(int argc, char **argv)
{
    if (argc != 2) {
        printf("Usage : %s <shellcode>\n", argv[0]);
        printf("\nDifferent shellcode formats are allowed :\n");
        printf("\t%s \"31 c0 50 68 2f 2f 73 68 68 2f 62 69 6e 89 e3 89 c1 89 c2 b0 0b cd 80 31 c0 40 cd 80\"\n", argv[0]);
        printf("\t%s \"0x31 0xc0 0x50 0x68 0x2f 0x2f 0x73 0x68 0x68 0x2f 0x62 0x69 0x6e 0x89 0xe3 0x89 0xc1 0x89 0xc2 0xb0 0x0b 0xcd 0x80 0x31 0xc0 0x40 0xcd 0x80\"\n", argv[0]);
        printf("\t%s \"\\x31 \\xc0 \\x50 \\x68 \\x2f \\x2f \\x73 \\x68 \\x68 \\x2f \\x62 \\x69 \\x6e \\x89 \\xe3 \\x89 \\xc1 \\x89 \\xc2 \\xb0 \\x0b \\xcd \\x80 \\x31 \\xc0 \\x40 \\xcd \\x80\"\n", argv[0]);
        printf("\t%s \"\\x31\\xc0\\x50\\x68\\x2f\\x2f\\x73\\x68\\x68\\x2f\\x62\\x69\\x6e\\x89\\xe3\\x89\\xc1\\x89\\xc2\\xb0\\x0b\\xcd\\x80\\x31\\xc0\\x40\\xcd\\x80\"\n", argv[0]);
        return 1;
    }
    char *shellcode = hex2str(argv[1]);
    printf("Shellcode Length: %zd\n", strlen(shellcode));
    int (*ret)() = (int(*)())shellcode;
    ret();
    return 0;
}

char *hex2str(char *str) {
    char *shellcode= str_replace(str_replace(str, "\\x", " "), "0x", " ");
    char *pEnd;
    long int j = strtol(shellcode, &pEnd, 16);
    char *sc;
    sc = malloc(strlen(shellcode)-char_count(shellcode, ' '));
    int counter=0;
    while (j != 0) {
       sprintf(sc+counter*sizeof(char), "%c", (int) j);
        counter++;
        j = strtol(pEnd, &pEnd, 16);
    }
    return sc;
}

int char_count(char *str, char search) {
    int i;
    int charcount = 0;
    for (i=0; str[i]; i++) {
        if (str[i] == search) charcount++;
    }
    return charcount;
}

char *str_replace(char *orig, char *rep, char *with) {
    char *result;
    char *ins;
    char *tmp;
    int len_rep;
    int len_with;
    int len_front;
    int count;

    if (!orig)
        return NULL;
    if (!rep)
        rep = "";
    len_rep = strlen(rep);
    if (!with)
        with = "";
    len_with = strlen(with);

    ins = orig;
    for (count = 0; (tmp = strstr(ins, rep)) != NULL; ++count) {
        ins = tmp + len_rep;
    }

    tmp = result = malloc(strlen(orig) + (len_with - len_rep) * count + 1);

    if (!result)
        return NULL;

    while (count--) {
        ins = strstr(orig, rep);
        len_front = ins - orig;
        tmp = strncpy(tmp, orig, len_front) + len_front;
        tmp = strcpy(tmp, with) + len_with;
        orig += len_front + len_rep; // move to next "end of rep"
    }
    strcpy(tmp, orig);
    return result;
}