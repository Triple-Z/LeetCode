#include <iostream>
#include <vector>
#include <cassert>

using namespace std;


class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        if (digits.size() < 1) return digits;

        
        bool cin = false;
        digits[digits.size()-1] += 1;
        for (auto it = digits.rbegin(); it != digits.rend(); it++) {
            if (cin) *it += 1;
            if (*it > 9) {
                *it %= 10;
                cin = true;
            } else {
                cin = false;
            }
        }
        
        if(cin) digits.insert(digits.begin(), 1);

        
        return digits;
    }
};


int test_ret_ref (const vector<int> &ret, const vector<int> &ref) {
    for (
        auto it_ret = ret.begin(), it_ref = ref.begin();
        it_ret != ret.end(), it_ref != ref.end();
        it_ret++, it_ref++
    ) {
        assert(*it_ret == *it_ref);
    }

    return 0;
}


int main() {
    vector<int> in = {1, 2, 3};
    Solution solution = Solution();
    vector<int> ret = solution.plusOne(in);
    vector<int> ref = {1, 2, 4};
    test_ret_ref(ret, ref);
    in = {4, 3, 2, 1};
    ret = solution.plusOne(in);
    ref = {4, 3, 2, 2};
    test_ret_ref(ret, ref);

    cout << "Success" << endl;

    return 0;
}