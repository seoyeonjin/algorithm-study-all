#include <iostream>
#include <algorithm>
#include <queue>

using namespace std;

int main() {

    int N; 
	cin >> N;
	priority_queue<pair<int, int>, vector<pair<int, int> >, greater<pair<int, int> > > pq;

	// 1. 빨리 끝나는 회의 순으로 정렬한다.
	for (int i = 0; i < N ; i++){
		int a,b;
		cin >> a >> b;
		pq.push(make_pair(b,a));
	}

	// 2. 최근에 끝난 회의의 끝나는 시간보다 앞에 시작하면 넘기고, 뒤에 시작하면 회의를 시작한다.
	// sort(pq.begin(), pq.end(), []())
	int last = 0;
	int cnt = 0 ;
	while (!pq.empty()) {
		auto temp = pq.top();
    	int b = temp.first;
    	int a = temp.second;

		pq.pop(); 
		if (a < last) {
			continue;
		} else {
			last = b;
			cnt++;
		}
		
		// cout << b << a << endl;
	}

	cout << cnt << endl;

}