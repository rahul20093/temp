#include <iostream>
#include <vector>

using namespace std;

int findSmallestMissingElement(const vector<int>& arr) {
    int expected = 0; // Start with the smallest possible missing element

    int i = 0; // Index for iteration
    while (i < arr.size()) {
        if (arr[i] == expected) {
            // If current element matches the expected value, move to the next expected value
            ++expected;
        }
        // Move to the next element
        ++i;
    }

    return expected;
}

int main() {
    // Example sorted array
    vector<int> arr = {0, 1, 2, 4, 5, 6};

    int missingElement = findSmallestMissingElement(arr);

    cout << "The smallest missing element is " << missingElement << "." << endl;

    return 0;
}
