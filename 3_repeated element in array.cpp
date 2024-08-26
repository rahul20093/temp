#include <iostream>
#include <unordered_map>
using namespace std;

int main() {
    int n, maxCount = 0, mostFrequent;
    cout << "Enter the number of elements: ";
    cin >> n;

    int arr[n];
    unordered_map<int, int> freq;

    cout << "Enter the elements: ";
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
        if (++freq[arr[i]] > maxCount) {
            maxCount = freq[arr[i]];
            mostFrequent = arr[i];
        }
    }

    cout << "Most frequent element: " << mostFrequent << endl;
    return 0;
}
