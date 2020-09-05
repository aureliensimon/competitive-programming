#include <bits/stdc++.h>
using namespace std;

#define ll long long

int main () {

	int n, m, a;
	cin >> n >> m >> a;

	ll h, v;

	h = n / a;
	v = m / a;

	if (n % a) h += 1;
	if (m % a) v += 1;
		
	cout << h * v << endl;
	return 0;
}
