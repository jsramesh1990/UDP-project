#include "logic.h"
#include <algorithm>

std::string process_message(const std::string &msg) {
    // Example logic: convert message to uppercase
    std::string out = msg;
    std::transform(out.begin(), out.end(), out.begin(), ::toupper);
    return out;
}

