// https://leetcode.com/problems/two-sum/
#include <stdio.h>
#include <stdlib.h>
#include "../../include/arrays.h"

/**
 * Finds two indices in the array whose values sum to the target.
 * Uses a brute-force approach with nested loops checking all pairs.
 * Time complexity: O(n^2) in the worst case.
 * Returns an allocated array of two indices if a pair is found;
 * otherwise, returns NULL.
 */
int *twoSum_n2(int *nums, int numsSize, int target, int *returnSize) {
    int *solution = NULL;
    *returnSize = 0;
    for (int i = 0; i < numsSize; i++) {
        for (int j = i + 1; j < numsSize; j++) {
            if (nums[i] + nums[j] == target) {
                solution = (int*) malloc(2 * sizeof(int));
                solution[0] = i;
                solution[1] = j;
                *returnSize = 2;
                return solution;
            }
        }
    }
    return solution;
}


int main(int argc, char** argv)
{
    if (argc < 3)
    {
        printf("Error: Need at least two nums and a target.\n");
        return 1;
    }

    print_sar(argc, argv);

    int numsSize = argc - 2;
    int nums[numsSize];
    int target = atoi(argv[argc - 1]);
    int *returnSize = (int*) malloc(sizeof(int));

    for (int i = 0; i < numsSize; i++)
    {
        nums[i] = atoi(argv[i + 1]);
    }

    print_iar(numsSize, nums);

    int *solution = twoSum_n2(nums, numsSize, target, returnSize);
    print_iar(*returnSize, solution);

    return 0;
}
