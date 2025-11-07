#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
#include <climits>
#include <queue>

using namespace std;

int solution(int n, vector<vector<int>> edge) {
    int answer = 0;
    priority_queue<pair<int, int>, vector<pair<int,int>>, greater<pair<int,int>>> que; 
    vector<int> roots(n+1, INT_MAX);
    roots[1] = 0; // 초기화
    vector<vector<int>> edges(n+1);
    
    for (auto& e : edge) {
        int a = e[0]; 
        int b = e[1];
        edges[a].push_back(b);
        edges[b].push_back(a);
    }
    que.push({0, 1});
    while (!que.empty()) {
        auto temp  = que.top();
        int dist = temp.first;
        int node = temp.second;
        que.pop();
        
        if (dist > roots[node]) continue;
        
        for (auto& e : edges[node]) {
            int new_dist = dist + 1;
            int new_node = e;
            if (new_dist < roots[new_node]) {
                roots[new_node] = new_dist;
                que.push({new_dist, new_node});
            }
        }
    }
    
    int max_num = 0;
    for (auto& r : roots) {
        if (r != INT_MAX && r > max_num) {
            max_num = r;
        }
    }
    // int max_num = *max(roots.begin()+1, roots.end()-1); 
    // cout << max_num; 
    for (int i = 1; i < n+1; i++) {
        if (roots[i] == max_num) {
            answer++;
        }
    }
    
    return answer;
}