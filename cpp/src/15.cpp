#include <iostream>
#include <vector>
#include <set>
#include <algorithm>
#include <cassert>

using namespace std;

class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        if (nums.size() < 3) {
            vector<vector<int>> retv;
            return retv;
        }
        
        sort(nums.begin(), nums.end());
        set<vector<int>> ret;
        
        for (auto it_i = nums.begin(); it_i != nums.end()-1; it_i++) {
            // i+1 element
            auto it_j = it_i + 1;
            // the last element
            auto it_h = nums.end() - 1;
            
            while (it_j < it_h) {
                auto sum = *it_i + *it_j + *it_h;
                if (sum > 0) {
                    while(it_j < it_h && *it_h == *(it_h-1)) it_h--;
                    it_h--;
                } else if (sum < 0) {
                    while(it_j < it_h && *it_j == *(it_j+1)) it_j++;
                    it_j++;
                } else {
                    // find a triplet
                    vector<int> triplet = {*it_i, *it_j, *it_h};
                    ret.insert(triplet);
                    while(it_j < it_h && *it_j == *(it_j+1)) it_j++;
                    while(it_j < it_h && *it_h == *(it_h-1)) it_h--;
                    it_j++;
                    it_h--;
                }
            }
        }
        vector<vector<int>> retv(ret.rbegin(), ret.rend());
        return retv;
    }
};

int main() {
    
    Solution solution = Solution();
    vector<int> in = {-1,0,1,2,-1,-4};
    vector<vector<int>> ret = solution.threeSum(in);
    vector<vector<int>> answer = {{-1, 0, 1}, {-1, -1, 2}};
    if (ret == answer) 
        cout << "Success" << endl;
    else
        cout << "Failed" << endl;

    return 0;
}
