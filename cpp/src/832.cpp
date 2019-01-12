#include <iostream>
#include <vector>
#include <cassert>

using namespace std;


class Solution {
public:
    vector<vector<int>> flipAndInvertImage(vector<vector<int>>& A) {
        
        // reverse
        vector<int> row;
        
        for (auto itr = A.begin(); itr != A.end(); itr++) {
            for (auto itc = itr->rbegin(); itc != itr->rend(); itc++) {
                // inverse
                *itc ^= 1;
                row.push_back(*itc);
            }
            *itr = row;
            row.clear();
        }
        
        return A;
    }
};


class test_Solution {
public:
    int test_flipAndInvertImage(vector<vector<int>>& A, vector<vector<int>>& result) {
        vector<vector<int>> test_sample1; 
        Solution solution = Solution();
        test_sample1 = solution.flipAndInvertImage(A);
        
        for (auto it_test_sample1 = test_sample1.begin(), it_result = result.begin(); it_test_sample1 != test_sample1.end() && it_result != result.end(); it_test_sample1++, it_result++) {
            for (auto it_test_sample1_c = it_test_sample1->begin(), it_result_c = it_result->begin(); it_test_sample1_c != it_test_sample1->end() && it_result_c != it_result->end(); it_test_sample1_c++, it_result_c++) {
                if (*it_test_sample1_c != *it_result_c) {
                    return 0;
                }
            }
        }
        return 1;
    }
};

int main() {
    test_Solution test = test_Solution();
    
    vector<vector<int>> sample1 = {{1,1,0,0},{1,0,0,1},{0,1,1,1},{1,0,1,0}};
    vector<vector<int>> sample1_result = {{1,1,0,0},{0,1,1,0},{0,0,0,1},{1,0,1,0}};
    
    int status = test.test_flipAndInvertImage(sample1, sample1_result);
    assert(status == 1);
    cout << "Success" << endl;

    return 0;
}
