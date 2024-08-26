#include <iostream>

using namespace std;

int main() {
    int number, sum = 0;

    cout << "Enter a positive integer: ";
    cin >> number;

    if (number < 1) {
        cout << "Error: Please enter a positive integer greater than zero." << endl;
    } else {
        // Calculate the sum of proper divisors using a for loop
        for (int i = 1; i <= number / 2; ++i) {
            if (number % i == 0) {
                sum += i; // Add the divisor to the sum
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
