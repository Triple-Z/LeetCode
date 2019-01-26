#include <iostream>
#include <vector>
#include <cassert>

using namespace std;


class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        int low = 0, high = nums.size() - 1;
        
        while (low <= high) {
            int mid = low + (high-low)/2;
            
            if (target <= nums[mid]) {
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }
        
        return low;
    }
};


int main() {
    vector<int> in = {1, 3, 5, 6};
    Solution solution = Solution();
    int ret = solution.searchInsert(in, 5);
    assert(ret == 2);
    ret = solution.searchInsert(in, 2);
    assert(ret == 1);
    ret = solution.searchInsert(in, 7);
    assert(ret == 4);
    ret = solution.searchInsert(in, 0);
    assert(ret == 0);
    cout << "Success" << endl;

    return 0;
}
