#include <iostream>
#include <string>

using namespace std;

class StringConverter {
    string str;

public:
    // Function to get the string from the user
    void getString() {
        cout << "Enter a string: ";
        getline(cin, str);
    }

    // Function to convert the string to uppercase
    void toUpperCase() {
        for (char &c : str) {
            c = toupper(c);
        }
        cout << "String in uppercase: " << str << endl;
    }

    // Function to convert the string to lowercase
    void toLowerCase() {
        for (char &c : str) {
            c = tolower(c);
        }
        cout << "String in lowercase: " << str << endl;
    }
};

int main() {
    StringConverter converter;
    converter.getString();

    int choice;
    cout << "Choose conversion:\n";
    cout << "1. Convert to Uppercase\n";
    cout << "2. Convert to Lowercase\n";
    cout << "Enter your choice: ";
    cin >> choice;

    if (choice == 1) {
        converter.toUpperCase();
    } else if (choice == 2) {
        converter.toLowerCase();
    } else {
        cout << "Invalid choice!" << endl;
    }

    return 0;
}
