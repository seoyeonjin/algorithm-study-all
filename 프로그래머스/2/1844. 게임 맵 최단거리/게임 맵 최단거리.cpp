#include<vector>
#include<iostream>
#include<queue>
#include<algorithm>

using namespace std;

int solution(vector<vector<int> > maps)
{
    int answer = -1;
    int dx[4] = {0,0,1,-1};
    int dy[4] = {1,-1,0,0};
    queue<tuple<int, int, int>> que;
    int N = maps.size();
    int M = maps[0].size();
    
    vector<vector<int>> visited(N, vector<int>(M, 0));
    
    
    que.push({0,0,1});
    visited[0][0] = 1;
    
    while (!que.empty()) {
        auto [x,y, cnt] = que.front(); que.pop();
        
        if (x == N-1 && y == M-1) {
            return cnt;
        } 
        else {
            for (int i = 0; i < 4; i++) {
                int nx = dx[i] + x;
                int ny = dy[i] + y;
                if (0 <= nx && nx < N && 0 <= ny && ny < M && visited[nx][ny] != 1 && maps[nx][ny] == 1) {
                    visited[nx][ny] = 1;
                    que.push({nx, ny, cnt+1});
                }
            }
        }
    }
    
    
    
    return answer;
}