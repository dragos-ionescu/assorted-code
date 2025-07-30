// Not A LeeCode Problem
#include <fstream>
#include <iostream>
#include <string>

bool solution_nlogn(std::string str, char c1, char c2) {
    for (int i = 0; i < str.length() / 2; i++) {
        if (str[i] == c2) {
            return false;
        }
    }
    for (int i = str.length() / 2; i < str.length(); i++) {
        if (str[i] == c1) {
            return false;
        }
    }

    int crossed = 0;
    while (crossed < str.length()) {
        if ((str.length() - crossed) % 2 == 1) {
            return false;
        }

        for (int i = 0; i < str.length() / 2; i++) {
            if (str[i] != '#') {
                for (int j = i; j < str.length() / 2; j+=2) {
                    str[j] = '#';
                    crossed++;
                }
                break;
            }
        }

        for (int i = str.length() / 2; i < str.length(); i++) {
            if (str[i] != '#') {
                for (int j = i; j < str.length(); j+=2) {
                    str[j] = '#';
                    crossed++;
                }
                break;
            }
        }
    }
    return true;
}

int main() {
    std::ifstream test_cases("test_cases.txt");

    if (!test_cases.is_open()) {
        std::cerr << "Error opening file!" << std::endl;
        return 1;
    }

    std::string str;
    while (std::getline(test_cases, str)) {
        if (str[0] != '#') {
            std::string result = (solution_nlogn(str, '0', '1') ? "True" : "False");
            std::cout << str << ": " << result << std::endl;
        }
    }
    test_cases.close();
}
