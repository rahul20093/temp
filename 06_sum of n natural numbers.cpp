#include <iostream>

using namespace std;

int main() {
    int n, sum = 0;

    cout << "Enter a positive integer: ";
    cin >> n;

    if (n < 1) {
        cout << "Error: Please enter a positive integer greater than zero." << endl;
    } else {
        // Calculate the sum of the first n natural numbers using a for loop
        for (int i = 1; i <= n; ++i) {
            sum += i;
        }

        cout << "The sum of the first " << n << " natural numbers is " << sum << "." << endl;
    }

    return 0;
}
