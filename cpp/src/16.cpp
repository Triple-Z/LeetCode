#include <iostream>
#include <vector>
#include <cassert>
#include <algorithm>

using namespace std;


class Solution {
public:
    int threeSumClosest(vector<int>& nums, int target) {
        int sum = 0;
        
        if (nums.size() <= 3) {
            for (auto it = nums.begin(); it != nums.end(); it++) {
                sum += *it;
            }
            return sum;
        }
        
        int min_diff_sum = nums[0] + nums[1] + nums[2];
        int min_diff = min_diff_sum - target;
        
        sort(nums.begin(), nums.end());
        
        for (auto it_i = nums.begin(); it_i != nums.end(); it_i++) {
            auto it_j = it_i + 1;
            auto it_h = nums.end() - 1;
            
            while (it_j < it_h) {
                sum = *it_i + *it_j + *it_h;

                if (abs(min_diff) > abs(sum - target)) {
                    // find a better solution
                    min_diff_sum = sum;
                    min_diff = sum - target;
                    
                } else if (sum - target >= 0) {
                    // smaller
                    it_h--;
                } else if (sum - target < 0) {
                    // bigger
                    it_j++;
                }
            }
        }
        
        return min_diff_sum;
    }
};


int main() {
    vector<int> in = {-1, 2, 1, -4};
    Solution solution = Solution();
    int ret = solution.threeSumClosest(in, 1);
    assert(ret == 2);
    cout << "Success" << endl;
    return 0;
}
