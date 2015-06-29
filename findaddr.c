/*
 * Find address of an environment variale
 * Compile :
 * $ gcc -Wall -o findaddr findaddr.c
 * Usage : 
 * $ ./findaddr <variable>
 * Example : 
 * $ ./findaddr SHELL
 * 
 */
 
#include <unistd.h>
#include <stdio.h>
int main(int argc, char* argv[])
    {
        if (argc != 2) {
        printf("%s\n", "Usage : findaddr ENV_NAME");
        return 0;
    }
    printf("%s address: 0x%lx\n",argv[1], getenv(argv[1]));
    return 0;
}
