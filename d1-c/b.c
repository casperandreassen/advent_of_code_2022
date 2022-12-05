#define _GNU_SOURCE
#include <stdio.h>
#include <stdlib.h>

int main(void)
{
	FILE *fp;
	char *line = NULL;
	size_t len = 0;
	ssize_t read;

	fp = fopen("input.txt", "r");
	if (fp == NULL)
	{
		exit(EXIT_FAILURE);
	}

	int biggestCarriers[] = {0, 0, 0};
	int current = 0;

	while ((read = getline(&line, &len, fp)) != -1)
	{
		if (read == 1)
		{
			for (int i = 0; i < 3; i++)
			{
				if (current > biggestCarriers[i])
				{
					// Top pos, shift all down one
					if (i == 0)
					{
						biggestCarriers[2] = biggestCarriers[1];
						biggestCarriers[1] = biggestCarriers[0];
					}
					// Middle pos shift down one
					else if (i == 1)
					{
						biggestCarriers[2] = biggestCarriers[1];
					};
					biggestCarriers[i] = current;
					current = 0;
					break;
				}
			}
			current = 0;
		}
		else
		{
			current += atoi(line);
		}
	}

	fclose(fp);

	int sumBiggest = 0;
	for (int i = 0; i < 3; i++)
	{
		sumBiggest += biggestCarriers[i];
	};

	printf("Sum of three biggest carriers [%d]\n", sumBiggest);
	if (line)
	{
		free(line);
	}
	exit(EXIT_SUCCESS);
}
