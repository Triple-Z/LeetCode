#include <iostream>
#include <vector>
#include <cassert>

using namespace std;


class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        for (auto it = nums.begin(); it != nums.end(); it++) {
            if (*it < target) continue;
            else return it-nums.begin();
        }
        
        return nums.size();
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
