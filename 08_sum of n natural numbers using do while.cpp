#include <iostream>

using namespace std;

int main() {
    int n, sum = 0;
    int i = 1; // Start with the first natural number

    cout << "Enter a positive integer: ";
    cin >> n;

    if (n < 1) {
        cout << "Error: Please enter a positive integer greater than zero." << endl;
    } else {
        // Calculate the sum of the first n natural numbers using a do-while loop
        do {
            sum += i;
            ++i; // Move to the next number
        } while (i <= n);

        cout << "The sum of the first " << n << " natural numbers is " << sum << "." << endl;
    }

    return 0;
}
