#include <iostream>
using namespace std;

int main() {
    int n;
    cout << "Enter the value of n: ";
    cin >> n;

    int a = 0, b = 1, fib;

    if (n == 1) {
        fib = a;
    } else if (n == 2) {
        fib = b;
    } else {
        for (int i = 3; i <= n; i++) {
            fib = a + b;
            a = b;
            b = fib;
        }
    }

    cout << "The " << n << "th Fibonacci number is: " << fib << endl;
    return 0;
}
