#include <iostream>
#include <vector>
#include <cassert>

using namespace std;


class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        if (nums.size() == 0)
            return 0;
        else if (nums.size() == 1)
            return 1;
        
        auto ret = nums.begin()+1;
        
        for (auto it = nums.begin(); it != nums.end() && ret != nums.end(); it++) {
            if (it != nums.begin()) {
                if (*it == *(it-1)) {
                    // duplicate
                    continue;
                } else {
                    *ret = *it;
                    ret++;
                }
            }
        }
        
        return ret-nums.begin();
    }
};


int main() {
    vector<int> in = {0, 0, 1, 1, 1, 2, 2, 3, 3, 4};
    vector<int> ref = {0, 1, 2, 3, 4};
    Solution solution = Solution();
    int ret = solution.removeDuplicates(in);
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