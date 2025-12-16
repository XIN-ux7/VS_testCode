#include <stdio.h>
#include <stdlib.h>
int main()
{
    printf("请输入一个整形数");
    int n = 0;
    scanf("%d", &n);
    char *p = (char *)malloc(n);
    scanf("%s", p);
    printf("%s\n", p);
}