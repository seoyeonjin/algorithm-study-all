#include <string>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

string solution(vector<int> numbers) {
    string answer = "";
    vector<string> nums;
    
    for (int& num: numbers) {
        string str = to_string(num);
        nums.push_back(str);
    }
        
    sort(nums.begin(), nums.end(), [](const string &a, const string &b) {
        return a + b > b + a;  
    });
    
    if (nums[0] == "0") return "0";
    
    for (auto s: nums) {
        // cout << s << " ";
        answer = answer + s;
    }

    return answer;
}