#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    vector<int> sortArrayByParity(vector<int>& A) {
        vector<int> even, odd;
        
        for (auto it = A.begin(); it != A.end(); it++) {
            if (*it % 2 == 0) { //even
                even.push_back(*it);
                
            } else { // odd
                odd.push_back(*it);
            }
        }
        
        // move odd elements to even vector
        for (auto it = odd.begin(); it != odd.end(); it++) {
            even.push_back(*it);
        }
        
        return even;
    }
};


int main() {
    Solution solution = Solution();

    vector<int> A = {4,5,6,7,8};
    vector<int> res = solution.sortArrayByParity(A);

    // print results
    for (auto it = res.begin(); it != res.end(); it++) {
        cout << *it << " ";
    }
    cout << endl;

    return 0;
}
