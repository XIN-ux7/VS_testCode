#include <stdio.h>

int i = 10;
void print(int i)
{
    printf("print i =%d\n", i);
}
int main()
{
    {
        int j = 5;
    }
    printf("main i = %d\n", i);
    i = 5;
    print(i);
    return 0;
}