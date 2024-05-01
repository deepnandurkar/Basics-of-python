#include <iostream>
#include <vector>

int main() {
    int N;
    std::cin >> N;

    std::vector<int> numbers(N);
    for (int i = 0; i < N; ++i) {
        std::cin >> numbers[i];
    }

    int totalTickets = 0;

    for (int i = 0; i < N; ++i) {
        int number = numbers[i];
        int maxDigit = -1;  // Initialize to a value lower than any digit
        int minDigit = 10;  // Initialize to a value higher than any digit

        while (number > 0) {
            int digit = number % 10;
            maxDigit = std::max(maxDigit, digit);
            minDigit = std::min(minDigit, digit);
            number /= 10;
        }

        int modifiedNumber = (maxDigit * 10 + minDigit);
        totalTickets += modifiedNumber;
    }

    std::cout << totalTickets << std::endl;

    return 0;
}