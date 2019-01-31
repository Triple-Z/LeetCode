#include <iostream>
#include <vector>
#include <unordered_map>
#include <climits>
#include <cassert>

using namespace std;


class Solution {
public:
    int findShortestSubArray(vector<int>& nums) {
        unordered_map<int, int> left, right, count;
        
        for (unsigned int i = 0; i < nums.size(); i++) {
            if (left.find(nums[i]) == left.end()) {
                left[nums[i]] = i;
            }
            right[nums[i]] = i;
            if (count.find(nums[i]) != count.end()) {
                count[nums[i]] += 1;
            } else {
                count[nums[i]] = 1;
            }
        }
        
        int degree = INT_MIN;
        // find the max degree
        for (auto it = count.begin(); it != count.end(); it++) {
            degree = max(degree, it->second);
        }
        
        int ret = INT_MAX;
        // find the max subarray with the max degree
        for (auto it = count.begin(); it != count.end(); it++) {
            if (degree == it->second) {
                ret = min(ret, right[it->first] - left[it->first] + 1);
            } 
        }
        
        return ret;
    }
};


int main() {
    vector<int> in = {1, 2, 2, 3, 1};
    Solution solution = Solution();
    int ret = solution.findShortestSubArray(in);
    assert(ret == 2);
    in = {1, 2, 2, 3, 1, 4, 2};
    ret = solution.findShortestSubArray(in);
    assert(ret == 6);

    cout << "Success" << endl;

    return 0;
}