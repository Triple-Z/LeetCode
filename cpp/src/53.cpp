#include <iostream>
#include <vector>
#include <climits>
#include <cassert>

using namespace std;


class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int max_ending_here = 0, max_so_far = INT_MIN;
        
        for (int num: nums) {
            max_ending_here = max(num, max_ending_here + num);
            max_so_far = max(max_so_far, max_ending_here);
        }
        
        return max_so_far;
    }
};


int main() {
    vector<int> in = {-2, 1, -3, 4, -1, 2, 1, -5, 4};
    Solution solution = Solution();
    int ret = solution.maxSubArray(in);
    assert(ret == 6);
    cout << "Success" << endl;

    return 0;
}
