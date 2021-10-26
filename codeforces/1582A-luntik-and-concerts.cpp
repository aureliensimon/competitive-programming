#include "bits/stdc++.h"
using namespace std;

int main () {
	int t, a, b, c, d;
	cin >> t;

	while (t--) {
		cin >> a >> b >> c;
		d = (a + c) % 2;
		cout << d << endl;
	}

	return 0;
}
