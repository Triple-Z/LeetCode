#include <iostream>
#include <vector>
#include <algorithm>
#include <cassert>

using namespace std;


class Solution {
public:
    int maxArea(vector<int>& height) {
        auto left = height.begin(), right = height.end()-1;
        int max_area = 0;
        
        while (left < right) {
            if (min(*left, *right) * (right-left) > max_area) {
                max_area = min(*left, *right) * (right-left);
            }
            
            if (*left < *right) left++;
            else right--;
        }
        
        return max_area;
    }
};


int main () {
    vector<int> in = {1, 8, 6, 2, 5, 4, 8, 3, 7};
    Solution solution = Solution();
    int max_area = solution.maxArea(in);

    assert(max_area == 49);
    cout << "Success" << endl;

    return 0;
}