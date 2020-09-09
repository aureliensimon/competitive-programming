#include <bits/stdc++.h>
using namespace std;

int main () {

	int n;
	cin >> n;

	int v[3] = {0, 0, 0};

	while (n--) {
		int x, y, z;
		cin >> x >> y >> z;
		
		v[0] += x;
		v[1] += y;
		v[2] += z;
	}

	if (v[0] == v[1] && v[1] == v[2] && v[0] == 0) {
		cout << "YES" << endl;
	} else {
		cout << "NO" << endl;
	}

	return 0;
}
