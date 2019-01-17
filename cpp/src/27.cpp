#include <iostream>
#include <vector>
#include <cassert>

using namespace std;


class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        if (nums.size() == 0) return 0;
        
        auto ret = nums.begin();
        
        for (auto it = nums.begin(); it != nums.end() && ret != nums.end(); it++) {
            if (*it != val) {
                *ret = *it;
                ret++;
            }
        }
        
        return ret-nums.begin();
    }
};


int main() {
    vector<int> in = {0, 1, 2, 2, 3, 0, 4, 2};
    Solution solution = Solution();
    int ret = solution.removeElement(in, 2);

    vector<int> ref = {0, 1, 3, 0, 4};
    assert(ret == 5);
    for (
        auto it_in = in.begin(), it_ref = ref.begin(); 
        it_in != in.end() && it_ref != ref.end(); 
        it_in++, it_ref++
    ) {
        assert(*it_in == *it_ref);
    }
    cout << "Success" << endl;
    
    return 0;
}