#include <stdio.h>
#include <stdlib.h>

void swap(char *a, char *b)
{
    char t = *a;
    *a = *b;
    *b = t;
}

// Just use last element as pivot
int partition(char arr[], int low, int high)
{
    int pivot = arr[high];
    int i = (low - 1);

    for (int j = low; j < high; j++)
    {
        if (arr[j] <= pivot)
        {
            i++;
            swap(&arr[i], &arr[j]);
        }
    }

    swap(&arr[i + 1], &arr[high]);

    return (i + 1);
}

// Quicksort with characters
void quickSort(char arr[], int low, int high)
{
    if (low < high)
    {
        int pi = partition(arr, low, high);

        quickSort(arr, low, pi - 1);

        quickSort(arr, pi + 1, high);
    }
}

int main()
{
    FILE *filePointer;
    char ch;
    filePointer = fopen("input.txt", "r");

    if (filePointer == NULL)
    {
        printf("File is not available \n");
    }
    else
    {
        // Queue of characters
        char seek[4];
        int index = 0;

        while ((ch = fgetc(filePointer)) != EOF)
        {
            // Shift array
            for (int i = 0; i < 3; i++)
            {
                seek[i] = seek[i + 1];
            }
            seek[3] = ch;
            index++;

            if (index > 3)
            {
                // Copy array to look for duplicates and not to mess up ordering of original array
                char copy[4];
                for (int i = 0; i < 4; i++)
                {
                    copy[i] = seek[i];
                }

                quickSort(copy, 0, 3);
                int unique = 0;

                // Since copy is sorted just have to iterate array
                for (int i = 0; i < 3; i++)
                {
                    if (copy[i] == copy[i + 1])
                    {
                        unique = 1;
                        break;
                    }
                }
                if (unique == 0)
                {
                    // If no equal neighbour's were found we are done.
                    printf("Needed [%d] to find start-of-packet marker\n", index);
                    break;
                }
            }
        }
    }
    fclose(filePointer);

    return 0;
}
