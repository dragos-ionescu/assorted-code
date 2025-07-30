#!/bin/bash
# https://leetcode.com/problems/valid-phone-numbers/
grep -Ex "(\([0-9]{3}\) [0-9]{3}-[0-9]{4})|([0-9]{3}-[0-9]{3}-[0-9]{4})" test_cases.txt
