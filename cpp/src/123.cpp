#include <iostream>
#include <vector>
#include <climits>
#include <cassert>

using namespace std;


class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int buy1 = INT_MIN, buy2 = INT_MIN;
        int sell1 = 0, sell2 = 0;
        
        for (int price: prices) {
            buy1 = max(buy1, -price);
            sell1 = max(sell1, price + buy1);
            buy2 = max(buy2, sell1 - price);
            sell2 = max(sell2, price + buy2);
        }

        return sell2;
    }
};


int main() {
    vector<int> in = {3, 3, 5, 0, 0, 3, 1, 4};
    Solution solution = Solution();
    int ret = solution.maxProfit(in);
    assert(ret == 6);
    in = {1, 2, 3, 4, 5};
    ret = solution.maxProfit(in);
    assert(ret == 4);
    in = {7, 6, 4, 3, 1};
    ret = solution.maxProfit(in);
    assert(ret == 0);

    cout << "Success" << endl;

    return 0;
}
