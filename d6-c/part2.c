#include <stdio.h>
#include <stdlib.h>

// Quicksort algorithm to sort array of char

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
        // Create array for keeping queue of characters
        char seek[14];
        int index = 0;

        while ((ch = fgetc(filePointer)) != EOF)
        {
            // Shift array left
            for (int i = 0; i < 13; i++)
            {
                seek[i] = seek[i + 1];
            }
            seek[13] = ch;
            index++;

            if (index > 13)
            {
                // Create a copy of the array so we dont mess up ordering of original array
                char copy[14];
                for (int i = 0; i < 14; i++)
                {
                    copy[i] = seek[i];
                }

                // Sort characters with quicksort
                quickSort(copy, 0, 13);
                int unique = 0;

                // Check for duplicates by simply iterating once since array is sorted
                for (int i = 0; i < 13; i++)
                {
                    if (copy[i] == copy[i + 1])
                    {
                        unique = 1;
                        break;
                    }
                }
                if (unique == 0)
                {
                    // If we found an array without duplicates we are finished.
                    printf("Took [%d] characters to find start-of-message marker\n", index);
                    break;
                }
            }
        }
    }
    fclose(filePointer);

    return 0;
}