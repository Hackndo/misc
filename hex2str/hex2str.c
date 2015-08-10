/*
 * Hex ascii values to string
 * Compile :
 * $ gcc -Wall -o hex2str hex2str.c
 * Usage :
 * $ ./hex2str <hex_string>
 * Example :
 * $ ./hex2str "0x68 0x61 0x63 0x6b 0x6e 0x64 0x6f"
 * hackndo
 */

#include <string.h>
#include <stdio.h>
#include <stdlib.h>



int main(int argc, char *argv[]) {
    if (argc != 2) {
        printf("Usage : %s <hex_str>\n", argv[0]);
        printf("\nDifferent formats are allowed. Here are some examples :\n");
        printf("\t%s \"68 61 63 6b 6e 64 6f\"\n", argv[0]);
        printf("\t%s \"0x68 0x61 0x63 0x6b 0x6e 0x64 0x6f\"\n", argv[0]);
        printf("\t%s \"\\x68 \\x61 \\x63 \\x6b \\x6e \\x64 \\x6f\"\n", argv[0]);
        printf("\t%s \"\\x68\\x61\\x63\\x6b\\x6e\\x64\\x6f\"\n", argv[0]);
        return 1;
    }
    printf("%s\n", hex2str(argv[1]));
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
    char *result; // the return string
    char *ins;    // the next insert point
    char *tmp;    // varies
    int len_rep;  // length of rep
    int len_with; // length of with
    int len_front; // distance between rep and end of last rep
    int count;    // number of replacements

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

    // first time through the loop, all the variable are set correctly
    // from here on,
    //    tmp points to the end of the result string
    //    ins points to the next occurrence of rep in orig
    //    orig points to the remainder of orig after "end of rep"
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
