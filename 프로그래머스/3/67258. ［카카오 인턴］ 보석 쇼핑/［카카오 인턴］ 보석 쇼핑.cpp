#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
#include <unordered_set>
#include <unordered_map>
#include <queue>
#include <set>

using namespace std;

vector<int> solution(vector<string> gems) {
    vector<int> answer;
    set<tuple<int,int,int>> temp;
    
    unordered_set<string> gset(gems.begin(), gems.end());
    unordered_map<string, int> gmap;
    
    int start= 0;
    int end = 0 ;
    
    // cout << gmap.size() << endl; 
    
    while (end < gems.size()) {
        string gem = gems[end];
        gmap[gem]++;
        while (gmap.size() == gset.size()) {
            // start 크게 하기
            gmap[gems[start]]--;
            if (gmap[gems[start]] == 0) {
                temp.insert({end-start, start+1, end+1});
                // answer.push_back(end-start);
                // answer.push_back(start+1);
                // answer.push_back(end+1);
                gmap.erase(gems[start]);
            }
            start++; 
        }
        end++;
    }
    
    auto [len, s, e] = *temp.begin();
    answer.push_back(s);
    answer.push_back(e);
    // cout << start << " " << end<< endl;
    
    return answer;
}