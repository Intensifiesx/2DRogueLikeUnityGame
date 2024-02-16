#include <iostream>

int main()
{
    int n = 0;
    std::cout << "Enter your number ";
    std::cin >> n;    

    for(int i = 1; i <= n; i++)
    {
        // ChatGPT commented out the two lines below
        // if(i % 15 == 0)
        //     std::cout << "FizzBuzz\n";
        if(i % 3 == 0)  // changed this to an if statement, rather than a else if statement
            std::cout << "Fizz\n";
        else if(i % 5 == 0)
            std::cout << "Buzz\n";
        else
            std::cout << i << "\n";       
    }
}