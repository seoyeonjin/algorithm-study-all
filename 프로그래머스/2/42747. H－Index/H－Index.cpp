#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

int solution(vector<int> citations) {
    int answer = 0;
    // n 편중 , h번 이상 인용된 논문이 h편 이상
    // 나머지 논문이 h번 이하 인용 -> h가 H-inex
    int begin = 0;
    int end = citations.size()+1;

    while (begin < end) {
        int mid = (begin + end) / 2;
        int temp = 0;
        for (int& c : citations) {
            if (mid <= c) {
                temp += 1;
            }
        }
        if (temp >= mid) {
            begin = mid + 1;
        } else {
            end = mid;
        }
    }
    
    // cout << end - 1;
    answer = end -1;
    // cout << s << " ";
    // for (int& c : citations) {
    //     cout << " "; 
    // }
    return answer;
}