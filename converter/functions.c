#include "functions.h"

void display_help(char *pname) {
    printf("Usage : %s number [from_base] to_base\n", pname);
    printf("Examples :\n");
    printf("  %s \\x1c 10\n", pname);
    printf("  => 28\n");
    printf("  %s 0b1010010 8\n", pname);
    printf("  => 122\n");
    printf("  %s 1djZj 62 10\n", pname);
    printf("  => 24246323\n");
}

int guess_base(char *nbr) {
    if (strlen(nbr) <= 2) {
        return UNKNOWN_BASE;
    }
    switch (nbr[1]) {
        case 'b':
            return BASE_2;
        case 'o':
            return BASE_8;
        case 'd':
            return BASE_10;
        case 'x':
            return BASE_16;
        default:
            return UNKNOWN_BASE;
    }
}

char *parse_num(char *nbr) {
    char *result;
    int i;
    size_t size = strlen(nbr);

    result = (char *) malloc(size*sizeof(char) - 2 + 1);
    for (i=2; i < size; i++) {
        result[i-2] = nbr[i];
    }
    result[size-2] = '\0';
    return result;
}

char *convert_10_to_n(long int number_to_convert, int base) {
    char base_digits[63] = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz";
    int converted_number[64];
    int index=0;

    /* convert to the indicated base */
    while (number_to_convert != 0)
    {
        converted_number[index] = (int) number_to_convert % base;
        number_to_convert = number_to_convert / base;
        ++index;
    }
    char *result = (char *) malloc(index * sizeof(char));
    /* now print the result in reverse order */
    --index;  /* back up to last entry in the array */
    int tmp = index;
    for(  ; index>=0; index--) /* go backward through array */
    {
        result[tmp-index] = base_digits[converted_number[index]];
    }
    return result;
}

long int convert_n_to_10(const char *number_to_convert, int base) {
    if (base == 10) {
        return atol(number_to_convert);
    }
    char base_digits[63] = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz";
    int index = 0;
    size_t size = strlen(number_to_convert);
    long int result= 0;
    for( ; index < size; index++) {
        char current_value = base <= 36 ?
                             (char) toupper(number_to_convert[index]) :
                             number_to_convert[index];
        int pos = (int) (strchr(base_digits, current_value) - base_digits);
        result += pow(base, size-index-1) * pos;
    }
    return result;
}