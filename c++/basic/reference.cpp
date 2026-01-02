#include <iostream>
using namespace std;

void wrongUpdate(int *p) {
    int x = 100;
    *p = x; // Changing the pointer locally, not the original address
}

int main() {
    int a = 10;
    int *ptr = &a;
    wrongUpdate(ptr);
    cout << "Value: " << *ptr << endl; // Will still print 10
    return 0;
}