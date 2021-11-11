#include <iostream>
using namespace std;
int main()
{
    int i, mi = 0, mx = 0;
    while (true)
    {
        cout << "Enter no";
        cin >> i;

        if (i > mi)
        {
            mi = i;
        }
        else if (mi < i)
        {
            mx = i;
        }
        else if (i == 0)
        {
            break;
        }
    }
    cout << "Larg" << mi << "samll" << mx;
}