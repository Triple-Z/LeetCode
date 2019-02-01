#include <iostream>
#include <vector>
#include <cassert>

using namespace std;


class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        int i = m - 1, j = n - 1, g = m + n - 1;
        
        while (i >= 0 && j >= 0) {
            if (nums2[j] >= nums1[i]) 
                nums1[g--] = nums2[j--];
            else
                nums1[g--] = nums1[i--];
        }
        
        while (j >= 0) {
            nums1[g--] = nums2[j--];
        }
    }
};


int main() {
    vector<int> nums1 = {1,2,3,0,0,0};
    vector<int> nums2 = {2, 5, 6};
    Solution solution = Solution();
    solution.merge(nums1, 3, nums2, 3);
    vector<int> ref = {1,2,2,3,5,6};
    
    for (
        auto it_ref = ref.cbegin(), it_in = nums1.cbegin();
        it_ref != ref.cend(), it_in != nums1.cend();
        it_ref++, it_in++
    ) {
        assert(*it_ref == * it_in);
    }

    cout << "Success" << endl;

    return 0;
}
