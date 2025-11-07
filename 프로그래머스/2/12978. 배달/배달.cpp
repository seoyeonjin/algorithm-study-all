#include <iostream>
#include <vector>
#include <iostream>
#include <queue>
using namespace std;

int solution(int N, vector<vector<int> > road, int K) {
    int answer = 0;
    vector<int> roots(N+1, 500001); // 초기화
    roots[1] = 0;
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int,int>>> heap; 
    vector<vector<pair<int, int>>> edges(N + 1, vector<pair<int, int>>());

    for (auto& r : road) {
        int a = r[0];
        int b = r[1];
        int c = r[2];
        edges[a].push_back({b,c});
        edges[b].push_back({a,c});
    }
    
    // for (auto& e : edges) {
    //     for (auto& ee : e) {
    //         cout << ee.first << " " << ee.second << " "; 
    //     }
    //     cout << endl;
    // }
    heap.push({0, 1});
    
    while (!heap.empty()) {
        // for (auto& r : roots) cout << r << " "; 
        auto temp = heap.top();
        int dist = temp.first;
        int node = temp.second;
        heap.pop();
        // cout << dist << node << " "; 
        if (dist > roots[node]) continue;
        for (auto& e : edges[node]) {
            int new_dist = e.second + dist;
            int new_node = e.first;
            
            if (new_dist < roots[new_node]) {
                roots[new_node] = new_dist;
                heap.push({new_dist, new_node});
            }
        }
    }
    
    // for (auto& r : roots) {
    //     cout << r << " "; 
    // }
    
    for (int i = 1; i <= N; i++){
        if (roots[i] <= K) answer++;
    }

    return answer;
}