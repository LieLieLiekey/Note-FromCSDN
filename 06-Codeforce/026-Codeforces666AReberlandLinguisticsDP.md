

#### 题目链接：[传送门](https://codeforces.com/problemset/problem/666/A)


##### 题意：


​ 给定串s，其由一个基本串后加任意多个长度为2或3的后缀串构成，要求基本串长度>4且相邻后缀串不相同。在基本串任意确定的情况下，求所有可能的后缀串。

##### 思路：


​ $dp[i][0]$表示第$a[i-1]$~$a[i]$组成的字符串是否可行，$dp[i][1]$表示第$a[i-2]$~$a[i]$组成的字符串是否可行。

​ 最后两个长度为2的后缀和长度为3的后缀如果可以取则可行。

​ $dp[i][0]=(dp[i+2][0]\&amp;\&amp;s1!=s2)~~||~~dp[i+3][1]$

​ $dp[i][1]=dp[i+2][0]~~||~~(dp[i+3][1]\&amp;\&amp;s1!=s2)$

```cpp
#include<bits/stdc++.h>
#define mset(a,b) memset(a,b,sizeof(a))
#define x  first
#define y  second
using  namespace std;
typedef long long ll;
typedef  pair<int,int> _p;
const int MAX=100000;
const int inf=0x3f3f3f3f;
const double EPS=1e-10;
const int MOD=1e9+7;
int dp[10005][2];/*0 :2 ,1:3*/
set<string> mmp;
int main()
{
    string s;
    cin>>s;
    if(s.length()<6)
    {
        puts("0");
        return 0;
    }
    int ls=s.length();
    if(ls>6)
    {
        dp[ls-1][0]=1;
        mmp.insert(s.substr(ls-2,2));
    }
    if(ls>7)
    {
        dp[ls-1][1]=1;
        mmp.insert(s.substr(ls-3,3));
    }
    dp[ls-2][0]=dp[ls-2][1]=0;
    for(int i=ls-3; i>=4; --i)
    {
        if(i-2>=4)
        {
            if((i+3<ls&&dp[i+3][1]) || (dp[i+2][0]&&s.substr(i-1,2)!=s.substr(i+1,2) )) //0
            {
                dp[i][0]=1;
                mmp.insert(s.substr(i-1,2));
            }
        }
        if(i-3>=4)
        {
            if(dp[i+2][0]>0||( i+3<ls &&dp[i+3][1]&&s.substr(i-2,3)!=s.substr(i+1,3))) // 1
            {
                dp[i][1]=1;
                mmp.insert(s.substr(i-2,3));
            }
        }

    }
    cout<<mmp.size()<<endl;
    for(auto i:mmp)
        cout<<i<<endl;
    return 0;
}

```


