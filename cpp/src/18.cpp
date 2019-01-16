#include <iostream>
#include <vector>
#include <algorithm>
#include <cassert>

using namespace std;


class Solution {
public:
    vector<vector<int>> fourSum(vector<int>& nums, int target) {
        vector<vector<int>> total;
        int n = nums.size();
        if (n < 4)
            return total;
        sort(nums.begin(), nums.end());
        for(int i = 0; i < n-3; i++) {
            // 忽略相同 i 的值的解
            if (i > 0 && nums[i] == nums[i-1]) continue;
            // 若最小的四个数之和都大于目标值，则说明整个集合内所有组合的和都不会等于目标值，跳出循环
            if (nums[i] + nums[i+1] + nums[i+2] + nums[i+3] > target) break;  
            // 若 i 与最大的三个数之和还小于目标值，则说明 i 的值过小，需要更换 i 的值
            if (nums[i] + nums[n-3] + nums[n-2] + nums[n-1] < target) continue;
            for (int j = i+1; j < n-2; j++) {
                // 忽略相同 j 的值的解
                if (j > i+1 && nums[j] == nums[j-1]) continue;
                // 若当前 i 和最小三个数都大于目标值，则说明当前 (i, j) 内所有组合的和都不会等于目标值，跳出循环
                if (nums[i] + nums[j] + nums[j+1] + nums[j+2] > target) break;
                // 若 (i, j) 与最大的两个数之和还小于目标值，则说明 j 的值过小，需要更换 j 的值
                if (nums[i] + nums[j] + nums[n-2] + nums[n-1] < target) continue;
                int left = j+1, right = n-1;
                // 双指针
                while(left < right){
                    int sum = nums[left] + nums[right] + nums[i] + nums[j];
                    if (sum < target) left++;
                    else if (sum > target) right--;
                    else {
                        total.push_back(vector<int>{nums[i], nums[j], nums[left], nums[right]});
                        do {left++;} while (nums[left] == nums[left-1] && left < right);
                        do {right--;} while (nums[right] == nums[right+1] && left < right);
                    }
                }
            }
        }
        return total;
    }
};


int main() {
    vector<int> in = {1, 0, -1, 0, -2, 2};
    Solution solution = Solution();
    vector<vector<int>> ret = solution.fourSum(in, 0);

    vector<vector<int>> answer = {{-2, -1, 1, 2}, {-2, 0, 0, 2}, {-1, 0, 0, 1}};

    for (auto it_ri = ret.begin(), it_ai = answer.begin(); it_ri != ret.end() && it_ai != answer.end(); it_ri++, it_ai++) {
        for (auto it_rj = it_ri->begin(), it_aj = it_ai->begin(); it_rj != it_ri->end(), it_aj != it_ai->end(); it_rj++, it_aj++) {
            // cout << *it_rj << " " << *it_aj << endl;
            assert(*it_rj == *it_aj);
        }
    }
    cout << "Success" << endl;

    return 0;
}
