#ifndef COLLECTIONS_HPP
#define COLLECTIONS_HPP
#include <string>

class IntNode {
public:
    int val;
    IntNode *next;
    IntNode();
    IntNode(int val);
    IntNode(int val, IntNode *next);
};

class IntLinkedList {
private:
    IntNode *first;
    IntNode *curr;
    int size_;
public:
    IntLinkedList();
    IntLinkedList(IntNode *first);
    std::string toString() const;
    void add(int val);
    int size();
    IntNode *get_list();
    friend std::ostream& operator<<(std::ostream& os, const IntLinkedList& list);
};

#endif //COLLECTIONS_HPP
