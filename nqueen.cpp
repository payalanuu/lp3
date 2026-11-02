
#include <iostream>
using namespace std;

int board[20][20], n;

// Check whether queen can be placed safely
bool isSafe(int row, int col)
{
    for (int i = 0; i < row; i++)
        if (board[i][col] == 1)
            return false;

    // Check left diagonal
    for (int i = row-1, j = col-1; i >= 0 && j >= 0; i--, j--)
        if (board[i][j] == 1)
            return false;

    // Check right diagonal
    for (int i = row-1, j = col+1; i >= 0 && j < n; i--, j++)
        if (board[i][j] == 1)
            return false;

    return true;
}

// Solve using backtracking
bool solve(int row)
{
    if (row == n)
        return true;

    for (int col = 0; col < n; col++)
    {
        if (isSafe(row, col))
        {
            board[row][col] = 1;

            if (solve(row + 1))
                return true;

            // Backtrack
            board[row][col] = 0;
        }
    }

    return false;
}

int main()
{
    cout << "Enter size of chessboard: ";
    cin >> n;

    // Initialize board with 0
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            board[i][j] = 0;

    // Place first queen at (0,0)
    board[0][0] = 1;

    if (solve(1))
    {
        cout << "\nSolution:\n";

        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < n; j++)
                cout << board[i][j] << " ";

            cout << endl;
        }
    }
    else
    {
        cout << "No solution exists!";
    }

    return 0;
}

/*
Time Complexity: O(N!)
Space Complexity: O(N^2)
*/
