#include "functions.h"

int main(int argc, char *argv[]) {
    if (argc < 2 || (argc == 2 && strncmp(argv[1], "-h", 2) != 0)) {
        fprintf(stderr, "Usage : %s number [from_base] to_base\n", argv[0]);
        exit(EXIT_FAILURE);
    }
    if (argc == 2 && strncmp(argv[1], "-h", 2) == 0) {
        display_help(argv[0]);
        exit(EXIT_SUCCESS);
    }

    char *number;
    int base_from;
    int base_to;
    bool are_cla_present = false;

    if (argc == 3) {
        base_from = guess_base(argv[1]);
        if (base_from == UNKNOWN_BASE) {
            printf("Couldn't find original base.\n");
            return 1;
        }
        number = parse_num(argv[1]);
        base_to = atoi(argv[2]);
    } else {

        number = argv[1];
        base_from = atoi(argv[2]);
        base_to = atoi(argv[3]);
    }

    printf("%s from base %d to base %d\n", number, base_from, base_to);
    printf("%s\n", convert_10_to_n(convert_n_to_10(number, base_from), base_to));
    return 0;
}
