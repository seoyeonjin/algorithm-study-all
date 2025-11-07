#include <string>
#include <vector>
#include <algorithm>
// #include <cmath>
#include <math.h>
#include <iostream>

using namespace std;

bool check(long long mid, vector<int> times, int n ) {
    long long temp = 0;
    for (auto& t : times) {
        // cout << t << " "; 
        // cout << mid << " "; 
        temp += mid / t;
    }
    
    // cout << temp << endl; 
    
    if (temp >= n) return true;
    else return false;
}

long long solution(int n, vector<int> times) {
    long long answer = 0;
    
    // 가능한 최솟값을 return한다. 
    long long end = pow(10, 18);
    long long start = 0;
    
    while (start < end) {
        long long mid = (start + end) /2 ;
        
        if (check(mid, times, n) == true) {
            end = mid ;
        } else {
            start = mid + 1;
        }
        // break; 
    }
    
    answer = start; 
    return answer;
}