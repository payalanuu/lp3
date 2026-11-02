
#include <iostream>
using namespace std;

int main()
{
    int n, W;

    cout << "Enter number of items: ";
    cin >> n;

    int wt[100], profit[100];

    cout << "Enter weights of items:\n";
    for (int i = 0; i < n; i++)
        cin >> wt[i];

    cout << "Enter profits of items:\n";
    for (int i = 0; i < n; i++)
        cin >> profit[i];

    cout << "Enter knapsack capacity: ";
    cin >> W;

    int dp[101][101] = {0};

    // Dynamic Programming
    for (int i = 1; i <= n; i++)
    {
        for (int w = 1; w <= W; w++)
        {
            if (wt[i-1] <= w)
            {
                dp[i][w] = max(
                    profit[i-1] + dp[i-1][w-wt[i-1]],
                    dp[i-1][w]
                );
            }
            else
            {
                dp[i][w] = dp[i-1][w];
            }
        }
    }

    cout << "Maximum Profit = " << dp[n][W];

    return 0;
}

/*
Time Complexity: O(n * W)
Space Complexity: O(n * W)
*/
