#include "bits/stdc++.h"
using namespace std;

int main () {
	int n, nb;
	string s;

	cin >> n;
	cin >> s;

	nb = 0;
	for (int i = 0; i < n; ++i) {
		if (s[i] == s[i + 1]) {
			nb++;	
		}
	}

	cout << nb << endl;
}
