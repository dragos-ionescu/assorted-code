// https://leetcode.com/problems/roman-to-integer/
#include <string>
#include <iostream>
#include <unordered_map>
#include <utility>
#include "../../lib/tests.cpp"
#include <cmath>
#include <vector>

std::string int_to_roman_1(int number) {
    std::vector<std::pair<int, std::string>> map = {
        {1000, "M"}, {900, "CM"}, {500, "D"}, {400, "CD"}, {100, "C"},
        {90, "XC"}, {50, "L"}, {40, "XL"}, {10, "X"},
        {9, "IX"}, {5, "V"}, {4, "IV"}, {1, "I"}
    };
    std::string result = std::string();
    for (const auto &x : map) {
        while (x.first <= number) {
            result += x.second;
            number -= x.first;
        }
    }
    return result;
}

std::string int_to_roman_n(int number) {
    std::unordered_map<int, std::string> map = {
        {1, "I"}, {4, "IV"}, {5, "V"}, {9, "IX"},
        {10, "X"}, {40, "XL"}, {50, "L"}, {90, "XC"},
        {100, "C"}, {400, "CD"}, {500, "D"}, {900, "CM"}, {1000, "M"}
    };
    std::string solution = std::string();
    int i = 0;

    while (number > 0) {
        int digit = number % 10;
        int multiplier = std::pow(10, i);
        while (digit > 0) {
            if (map.find(digit * multiplier) != map.end()) {
                solution = map[digit * multiplier] + solution;
                digit = 0;
            } else if (map.find(multiplier) != map.end()) {
                solution = map[multiplier] + solution;
                digit--;
            }
        }
        number /= 10;
        i++;
    }
    return solution;
}

int roman_to_int_n(const std::string roman) {
    int solution = 0;
    std::unordered_map<std::string, int> map = {
        {"I", 1},
        {"IV", 4},
        {"V", 5},
        {"IX", 9},
        {"X", 10},
        {"XL", 40},
        {"L", 50},
        {"XC", 90},
        {"C", 100},
        {"CD", 400},
        {"D", 500},
        {"CM", 900},
        {"M", 1000}
    };

    for (int i = roman.length() - 1; i >= 0; i--) {
        if (i != 0 && map[{roman[i - 1], roman[i]}] != 0) {
            solution += map[{roman[i - 1], roman[i]}];
            i--;
        } else if (map[{roman[i]}] != 0){
            solution += map[{roman[i]}];
        } else {
            return -1;
        }
    }
    return solution;
}

int main() {

    std::ifstream testfile("tests.txt");
    if (!testfile.is_open()) {
        std::cerr << "Error: failed while opening file." << std::endl;
        return 1;
    }

    auto map = get_all_tests(testfile);
    for (const auto &pair : map) {
        int key;
        try {
            key = std::stoi(pair.first);
        } catch (const std::invalid_argument& e) {
            std::cerr << "Error: not a valid number."<< std::endl;
        } catch (const std::out_of_range& e) {
            std::cerr << "Error: out of range number." << std::endl;
        }

        std::string result = int_to_roman_1(key);
        if (result == pair.second) {
            std::cout << pair.first << ": " << pair.second << " CORRECT!" << std::endl;
        } else {
            std::cout << pair.first << ": " << pair.second << " WRONG! GOT " << result << std::endl;
        }
    }

    testfile.close();
    return 0;
}
