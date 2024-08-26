#include <iostream>

using namespace std;

int main() {
    int number, sum = 0;

    cout << "Enter a number: ";
    cin >> number;

    if (number <= 0) {
        cout << "Error: Enter a positive number." << endl;
    } else {
        // Calculate the sum of proper divisors
        for (int i = 1; i <= number / 2; ++i) {
            if (number % i == 0) {
                sum += i;
            }
        }

        // Check if the number is a perfect number
        if (sum == number) {
            cout << number << " is a perfect number." << endl;
        } else {
            cout << number << " is not a perfect number." << endl;
        }
    }

    return 0;
}
