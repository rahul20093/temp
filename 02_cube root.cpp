#include <iostream>
#include <cmath>

using namespace std;

int main() {
    double number, result;

    cout << "Enter a number: ";
    cin >> number;

        // Compute the cube root
    result = cbrt(number);

        // Print the result
    cout << "The cube root of " << number << " is " << result << "." << endl;
    
	return 0;
}
