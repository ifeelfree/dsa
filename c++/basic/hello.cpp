#include <iostream>
#include<bits/stdc++.h>
using namespace std;

int main() {

    set<int> s;
    auto [it, success] = s.insert(10);
    cout << (success ? "Inserted" : "Duplicate") << endl;
    cout << *it << endl;


    set<int>::iterator it2;
    tie(it2, success) = s.insert(10); // Try duplicate
    cout << (success ? "Inserted" : "Duplicate") << endl;
    cout << *it2 << endl;

    return 0;
}