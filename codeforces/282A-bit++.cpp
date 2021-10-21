#include "bits/stdc++.h"
using namespace std;

int main () {
	int x = 0;
	int n;
	string c;

	cin >> n;

	while (n--) {
		cin >> c;
		if (c[1] == '+') {
			x++;
		} else {
			x--;
		}
	}

	cout << x << endl;
}
