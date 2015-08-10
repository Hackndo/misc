#include <string.h>
#include <stdlib.h>
#include <math.h>
#include <stdio.h>
#include <ctype.h>
#include <stdio.h>

#define UNKNOWN_BASE 0
#define BASE_2 2
#define BASE_8 8
#define BASE_10 10
#define BASE_16 16
#define BASE_36 36
#define BASE_52 52
#define BASE_62 62
#define BASE_64 64


void display_help(char *pname);
int guess_base(char *nbr);
char *parse_num(char *nbr);
char *convert_10_to_n(long int number_to_convert, int base);
long int convert_n_to_10(const char *number_to_convert, int base);
