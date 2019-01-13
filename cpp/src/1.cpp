#include <iostream>
#include <vector>
#include <unordered_map>
#include <cassert>

using namespace std;


class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> ret;
        
        // one-pass hash table
        unordered_map<int, int>  hash_table;
        for (auto it = nums.begin(); it != nums.end(); it++) {
            auto it_find = hash_table.find(target-*it);
            if (it_find != hash_table.end()) {
                ret.push_back(it-nums.begin());
                ret.push_back(it_find->second);
                return ret;
            }
            
            hash_table.insert({*it, it-nums.begin()});
        }
        
        return ret;
    }
};


class test_Solution {
public:
    int test_twoSum(vector<int> &nums, int &target, vector<int> &answer) {
        vector<int> ret;
        Solution solution = Solution();
        ret = solution.twoSum(nums, target);
        
        // reverse answer
        vector<int> another_answer = vector<int>(answer.rbegin(), answer.rend());
        if (ret != answer && ret != another_answer) {
            return 0;
        }
        
        return 1;
    }
};

int main() {
    test_Solution test = test_Solution();

    vector<int> nums = {2, 7, 11, 15};
    vector<int> answer = {0, 1};
    int target = 9;

    int status = test.test_twoSum(nums, target, answer);
    assert(status == 1);
    cout << "Success" << endl;

    return 0;
}
