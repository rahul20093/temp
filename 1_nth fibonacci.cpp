#include <iostream>

using namespace std;

// Function to find the Nth Fibonacci number
int fibonacci(int n) {
    if (n <= 0) {
        return 0; // Base case: F(0) = 0
    } else if (n == 1) {
        return 1; // Base case: F(1) = 1
    } else {
        // Recursive case: F(n) = F(n-1) + F(n-2)
        return fibonacci(n - 1) + fibonacci(n - 2);
    }
}

int main() {
    int n;

    cout << "Enter the position (N) to find the Nth Fibonacci number: ";
    cin >> n;

    if (n < 0) {
        cout << "Error: Please enter a non-negative integer." << endl;
    } else {
        int result = fibonacci(n);
        cout << "The " << n << "th Fibonacci number is " << result << "." << endl;
    }

    return 0;
}
