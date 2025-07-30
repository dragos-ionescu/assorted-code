// https://leetcode.com/problems/merge-two-sorted-lists/
#include <iostream>
#include "../../include/collections.hpp"

/**
 * Merges two sorted singly linked lists into a single sorted list.
 * Iterates through both lists once, comparing nodes and linking them.
 * Time complexity: O(n + m), where n and m are the lengths of the two lists.
 * Returns the head of the newly merged sorted list.
 */
class Solution {
public:
    static IntNode* mergeTwoLists(IntNode* list1, IntNode* list2) {
        auto *merged = new IntNode();
        auto *builder = merged;

        while (list1 && list2) {
            if (list1->val <= list2->val) {
                builder->next = new IntNode(list1->val);
                list1 = list1->next;
            } else {
                builder->next = new IntNode(list2->val);
                list2 = list2->next;
            }
            builder = builder->next;
        }
        while (list1) {
            builder->next = new IntNode(list1->val);
            list1 = list1->next;
            builder = builder->next;
        }
        while (list2) {
            builder->next = new IntNode(list2->val);
            list2 = list2->next;
            builder = builder->next;
        }

        auto *result = merged->next;
        delete merged;
        return result;
    }
};

int main(int argc, char **argv) {
    auto *list1 = new IntLinkedList();
    auto *list2 = new IntLinkedList();

    list1->add(2);
    list1->add(3);
    list1->add(10);

    list2->add(-2);
    list2->add(-3);
    list2->add(-10);

    IntNode *solution = Solution::mergeTwoLists(list1->get_list(), list2->get_list());
    auto merged = new IntLinkedList(solution);
    std::cout << *merged << std::endl;
    return 0;
}
