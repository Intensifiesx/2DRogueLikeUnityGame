#include <exception>
#include <iostream>
class ErrorHandler
{
  ErrorHandler()
  {
  }
public:
  void logError(std::exception& e)
  {
    auto errorLogFIle = fopen("log.txt", "w");
    fprintf(errorLogFIle, "Something has failed: %s", e.what());
    fclose(errorLogFIle);
  }
  void printError(std::exception& e)
  {
    printf("Something has failed: %s", e.what());
  }
private:
};
