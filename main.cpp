/******************************************************************************

                              Online C++ Compiler.
               Code, Compile, Run and Debug C++ program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <iostream>
#include <vector>
#include <algorithm>

const int MOD = 1000000007;

bool is_valid_permutation(const std::vector<int>& perm) {
    int n = perm.size();
    for (int i = 1; i < n; ++i) {
        if (i % 2 == 1) { // i нечётное, perm[i-1] < perm[i]
            if (perm[i-1] >= perm[i]) return false;
        } else { // i чётное, perm[i-1] > perm[i]
            if (perm[i-1] <= perm[i]) return false;
        }
    }
    return true;
}

int count_valid_permutations(int n) {
    std::vector<int> perm(n);
    for (int i = 0; i < n; ++i) {
        perm[i] = i + 1;
    }

    int count = 0;
    do {
        if (is_valid_permutation(perm)) {
            count = (count + 1) % MOD;
        }
    } while (std::next_permutation(perm.begin(), perm.end()));

    return count;
}

int main() {
    int n;
    std::cin >> n;
    std::cout << count_valid_permutations(n) << std::endl;
    return 0;
}
