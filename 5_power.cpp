#include <iostream>
#include <cmath>  // Include cmath for the pow function
using namespace std;

int main() {
    double base, result;
    int exponent;

    // Input the base and exponent
    cout << "Enter the base: ";
    cin >> base;
    cout << "Enter the exponent: ";
    cin >> exponent;

    // Calculate the power using pow function
    result = pow(base, exponent);

    // Output the result
    cout << base << " raised to the power of " << exponent << " is: " << result << endl;
    return 0;
}
