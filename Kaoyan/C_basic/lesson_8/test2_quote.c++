#include <stdio.h>
#include <stdlib.h>
void modify_pointer(char *&p)
{
    p = (char *)malloc(100);
    fgets(p, 100, stdin);
}

int main()
{
    char *p = NULL;
    modify_pointer(p);
    puts(p);
    free(p);
    return 0;
}