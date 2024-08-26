#include <iostream>
using namespace std;

int main() {
    int number, n;

    // Input the number and the bit position
    cout << "Enter the number: ";
    cin >> number;
    cout << "Enter the bit position to set (0-based index): ";
    cin >> n;

    // Check if the position is valid
    if (n >= 0 && n < sizeof(int) * 8) {
        // Set the Nth bit using bitwise OR
        number |= (1 << n);
        cout << "The new number after setting the " << n << "th bit is: " << number << endl;
    } else {
        cout << "Invalid bit position!" << endl;
    }

    return 0;
}
