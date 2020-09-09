#include <bits/stdc++.h>
using namespace std;

int main () {
	
	int t;
	cin >> t;

	while (t--) {
		int a, b;
		cin >> a >> b;

		int m = (abs(a - b) / 10) + (a % 10 != b % 10);

		cout << m << endl;
	}	

	return 0;
}
