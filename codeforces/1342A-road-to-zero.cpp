#include <bits/stdc++.h>
using namespace std;

#define ull unsigned long long

int main () {

	int t;
	cin >> t;

	while (t--) {
		ull x, y, a, b;
		cin >> x >> y >> a >> b;
	
		ull s = 0;
		
		if (min(x, y) == x) {
			swap(x, y);
		}
	
		if (2 * a <= b) {
			s = (x + y) * a;
		} else {
			s = y * b + (x - y) * a;
		}	
		
		cout << s << endl;	
	}

	return 0;
}
