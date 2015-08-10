#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
int main(int argc, char* argv[])
    {
        if (argc != 2) {
        printf("%s\n", "Usage : findaddr ENV_NAME");
        return 0;
    }
    printf("%s address: %p\n",argv[1], (void *)getenv(argv[1]));
    return 0;
}
