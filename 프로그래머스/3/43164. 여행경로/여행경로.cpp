#include <string>
#include <vector>
#include <unordered_map>
#include <iostream>
#include <algorithm>
#include <set>

using namespace std;
bool dfs(unordered_map<string, vector<string>>& edges, vector<string>& route, int used, int total) {
    if (used == total) return true; // 모든 티켓 사용 완료
    
    string now = route.back();
    for (auto& next : edges[now]) {
        if (next != "") {
            // 티켓 사용
            string temp = next;
            next = ""; // 사용 처리
            route.push_back(temp);
            
            if (dfs(edges, route, used + 1, total)) return true;
            
            // 백트래킹 (복구)
            route.pop_back();
            next = temp;
        }
    }
    return false;
}

vector<string> solution(vector<vector<string>> tickets) {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
    vector<string> answer;
    vector<string> visited;
    visited.push_back("ICN"); 
    
    unordered_map<string, vector<string>> edges;
    // vector<vector<int>> edges;
    for (auto& t : tickets) {
        string s = t[0];
        string e = t[1];
        edges[s].push_back(e);
    }
    
    for (auto& [k, v] : edges)
        sort(v.begin(), v.end());
    
    vector<string> route = {"ICN"};
    dfs(edges, route, 0, tickets.size());
    
    // visited = dfs(edges, "ICN", visited, tickets.size()); 
    
    // return visited;
    return route;
}