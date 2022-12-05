#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
    int biggestCarrier = 0;
    FILE *fp;
    char *line = NULL;
    size_t len = 0;
    ssize_t read;

    fp = fopen("input.txt", "r");
    if (fp == NULL)
        exit(EXIT_FAILURE);

    int current = 0;
    while ((read = getline(&line, &len, fp)) != -1)
    {
        if (read == 1)
        {
            if (current > biggestCarrier)
            {
                biggestCarrier = current;
                current = 0;
            }
            else
            {
                current = 0;
            }
        }
        else
        {
            current += atoi(line);
        }
    }
    printf("The elf that carries the most calories carries [%d] calories\n", biggestCarrier);

    fclose(fp);
    if (line)
        free(line);
    exit(EXIT_SUCCESS);
}