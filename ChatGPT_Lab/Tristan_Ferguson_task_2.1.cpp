#include <exception>
#include <iostream>
#include <fstream>

class ErrorHandler {
public:
    ErrorHandler() = default;

    void logError(const std::exception& e) {
        std::ofstream errorLogFile("log.txt");
        errorLogFile << "Something has failed: " << e.what() << std::endl;
    }

    void printError(const std::exception& e) {
        std::cout << "Something has failed: " << e.what() << std::endl;
    }
};
