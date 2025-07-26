#include <iostream>
#include <sstream>
#include "../include/lists.h"

IntNode::IntNode() : val(0), next(nullptr) {}
IntNode::IntNode(int val) : val(val), next(nullptr) {}
IntNode::IntNode(int val, IntNode *next) : val(val), next(next) {}

IntLinkedList::IntLinkedList() : size_(0), first(nullptr) {}
IntLinkedList::IntLinkedList(IntNode *first) : size_(0), first(first) {}
std::string IntLinkedList::toString() const {
    auto looper = this->first;
    std::ostringstream buf;

    buf << "[";
    while (looper) {
        buf << looper->val;
        if (looper->next) {
            buf << ", ";
        }
        looper = looper->next;
    }
    buf << "]" << std::endl;

    return buf.str();
}

void IntLinkedList::add(int val) {
    if (this->curr) {
        this->curr->next = new IntNode(val);
        this->curr = this->curr->next;
    } else {
        this->first = new IntNode(val);
        this->curr = this->first;
    }
    this->size_++;
}

int IntLinkedList::size() {
    return this->size_;
}

IntNode *IntLinkedList::get_list() {
    return this->first;
}

std::ostream& operator<<(std::ostream& os, const IntLinkedList& list) {
    return os << list.toString();
}
