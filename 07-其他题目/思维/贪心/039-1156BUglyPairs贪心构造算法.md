

## [1156B - Ugly Pairs](https://codeforces.com/contest/1156/problem/B) (贪心，构造算法)


### 解法：


​ 偶数位置的串在一起为a，奇数位置的串在一起为b，其中a和b串的内部是一定合法的。故只需检查a+b串合法，或者b+a是否合法即可。

```cpp
#include<bits/stdc++.h>
#define mset(a,b) memset(a,b,sizeof(a))
#define x first
#define y second
using namespace std;
typedef long long ll;
const double EPS=1e-10;
const int maxn=1e6+10;
bool check(string s)
{
    for(int i=1;i<s.length();++i){
        if(abs(s[i]-s[i-1])==1) return false;
    }
    return true;
}
int main()
{
    int t;
    cin>>t;
    while(t--)
    {
        string s,odd,even;
        cin>>s;
        for(auto i:s){
            if(i%2) odd+=i;
            else even+=i;
        }
        sort(odd.begin(),odd.end());
        sort(even.begin(),even.end());
        if(check(odd+even)){
            cout<<odd+even<<endl;
        }
        else if(check(even+odd)){
            cout<<even+odd<<endl;
        }
        else
            cout<<"No answer"<<endl;
    }
    return 0;
}
```


