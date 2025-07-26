#include <stdio.h>

/**
 * @brief Prints the elements of an integer array in a comma-separated format.
 *
 * The output is enclosed in square brackets.
 * Runs in O(n) time, where n is the number of elements.
 *
 * @param arc Number of elements in the array. Must be >= 0.
 * @param arv Pointer to the integer array.
 *
 * @return 0 on success, or 1 if arc is negative (invalid input).
 */
int print_iar(int arc, int *arv) {
    if (arc < 0) {
        return 1;
    }

    printf("[");
    for (int i = 0; i < arc - 1; i++) {
        printf("%d, ", arv[i]);
    }
    if (arc == 0) {
        printf("]\n");
    } else {
        printf("%d]\n", arv[arc - 1]);
    }
    return 0;
}

/**
 * @brief Prints the elements of a string array in a comma-separated format.
 *
 * The output is enclosed in square brackets.
 * Runs in O(n * m) time, where n is the number of strings and m is the length of the longest string.
 *
 * @param arc Number of strings in the array. Must be >= 0.
 * @param arv Pointer to the array of string pointers.
 *
 * @return 0 on success, or 1 if arc is negative (invalid input).
 */
int print_sar(int arc, char **arv) {
    if (arc < 0) {
        return 1;
    }

    printf("[");
    for (int i = 0; i < arc - 1; i++) {
        printf("%s, ", arv[i]);
    }
    if (arc == 0) {
        printf("]\n");
    } else {
        printf("%s]\n", arv[arc - 1]);
    }
    return 0;
}
