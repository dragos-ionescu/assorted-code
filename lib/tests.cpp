#include <fstream>
#include <string>
#include <unordered_map>
#include "../include/tests.hpp"

std::unordered_map<std::string, std::string> get_all_tests(std::ifstream &filestream) {
    std::unordered_map<std::string, std::string> map{};
    std::string buf;

    while (std::getline(filestream, buf)) {
        if (buf[0] == '#') {
            continue;
        }

        int i = 0;
        std::string last_key;
        while (i < buf.length()) {
            for (; i < buf.length() && buf[i] == ' '; i++);
            int start = i;
            for (; i < buf.length() && buf[i] != ' '; i++);
            int end = i;

            auto entry = buf.substr(start, end - start);
            if (last_key.empty()) {
                map[entry];
                last_key = entry;
            } else {
                map[last_key] = entry;
                last_key = std::string();
            }
        }
    }
    return map;
}
