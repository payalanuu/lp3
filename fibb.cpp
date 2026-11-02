
#include <iostream>
using namespace std;

// Recursive function
int fib(int n)
{
    if (n <= 1)
        return n;

    return fib(n - 1) + fib(n - 2);
}

int main()
{
    int n;

    cout << "Enter number: ";
    cin >> n;

    // Print Fibonacci series
    for (int i = 0; i < n; i++)
    {
        cout << fib(i) << " ";
    }

    return 0;
}

/*
Time Complexity: O(2^n)
Space Complexity: O(n)
*/



#include <iostream>
using namespace std;

int main()
{
    int n, a = 0, b = 1, c;

    cout << "Enter number: ";
    cin >> n;

    // Print Fibonacci series using loop
    for (int i = 0; i < n; i++)
    {
        cout << a << " ";

        c = a + b;
        a = b;
        b = c;
    }

    return 0;
}

/*
Time Complexity: O(n)
Space Complexity: O(1)
*/
