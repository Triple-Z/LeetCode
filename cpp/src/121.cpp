#include <iostream>
#include <vector>
#include <climits>
#include <cassert>

using namespace std;


class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int min_price = INT_MAX;
        int max_profit = 0;
        
        for (int price: prices) {
            if (price < min_price) 
                min_price = price;
            if (price - min_price > max_profit) 
                max_profit = price - min_price;
        }
        
        return max_profit;
    }
};


int main() {
    vector<int> in = {7, 1, 5, 3, 6, 4};
    Solution solution = Solution();
    int ret = solution.maxProfit(in);
    assert(ret == 5);

    in = {7, 6, 4, 3, 1};
    ret = solution.maxProfit(in);
    assert(ret == 0);

    cout << "Success" << endl;

    return 0;
}
