#include <bits/stdc++.h>
using namespace std;

#define ull unsigned long long

int main () {

	int n, t;
	cin >> n >> t;

	ull r = round(pow(10, n - 1));

	if (n == 1 && t == 10) {
		cout << -1 << endl;
	} else {
		if (n <= 20) {
			while (r % t) r++;
			cout << r << endl;
		} else {
			if (t == 10) {
				for (int i = 0; i < n - 1; ++i) {
					cout << 1;
				}
				cout << 0 << endl;
			} else {
				for (int i = 0; i < n; ++i) {
					cout << t;
				}	
			}
		}
	}

	return 0;
}
