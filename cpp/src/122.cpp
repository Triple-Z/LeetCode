#include <iostream>
#include <vector>
#include <climits>
#include <cassert>

using namespace std;


class Solution {
public:
    int maxProfit(vector<int>& prices) {
        if (prices.size() == 0)
            return 0;
        
        int max_profit = 0;
        
        for (auto it = prices.begin()+1; it != prices.end(); it++) {
            if (*it > *(it-1))
                max_profit += *it - *(it-1);
        }
        
        return max_profit;
    }
};


int main() {
    vector<int> in = {7, 1, 5, 3, 6, 4};
    Solution solution = Solution();
    int ret = solution.maxProfit(in);
    assert(ret == 7);
    in = {1, 2, 3, 4, 5};
    ret = solution.maxProfit(in);
    assert(ret == 4);
    in = {7, 6, 4, 3, 1};
    ret = solution.maxProfit(in);
    assert(ret == 0);

    cout << "Success" << endl;

    return 0;
}