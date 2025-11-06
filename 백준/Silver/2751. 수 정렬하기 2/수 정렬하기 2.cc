#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
	// 코드 작성
	int N;
	cin >> N;
	vector<int> vec(0);

	for (int i= 0; i < N; i++) {
		int a;
		cin >> a;
		vec.push_back(a);
	}
	sort(vec.begin(), vec.end());
	
	for (int v : vec) {
		cout << v << "\n";
	}
	return 0;
}