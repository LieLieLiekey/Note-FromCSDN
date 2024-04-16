

　　Haoren is very good at solving mathematic problems. Today he is working a problem like this:  　　Find three positive integers X, Y and Z (X < Y, Z > 1) that holds  　　 X^Z + Y^Z + XYZ = K  　　where K is another given integer.  　　Here the operator “^” means power, e.g., 2^3 = 2 * 2 * 2.  　　Finding a solution is quite easy to Haoren. Now he wants to challenge more: What’s the total number of different solutions?  　　Surprisingly, he is unable to solve this one. It seems that it’s really a very hard mathematic problem.  　　Now, it’s your turn. 

Input　　There are multiple test cases.  　　For each case, there is only one integer K (0 < K < 2^31) in a line.  　　K = 0 implies the end of input.  　　  Output　　Output the total number of solutions in a line for each test case.  Sample Input

```
9
53
6
0```


Sample Output

```
1
1
0
　　

        
  ```


Hint                                                                                                                                                                      

```
9 = 1^2 + 2^2 + 1 * 2 * 2
53 = 2^3 + 3^3 + 2 * 3 * 3

        
 ```


 

题意 给你一个k

解方程 X^Z + Y^Z + XYZ = K   其中x>=1 y>x,z>1 让你解出有多少种解

 

枚举所有x的可能情况 ，在每个x上z的可能情况枚举，然后用二分求出y，并且判断y是否符合方程。

代码：

```cpp
/*
1.x 范围为1~sqrt(k/2)  time:1~3w
2.z 范围为2~log2(k);//times:1~30
3.二分求 y  y的范围为(x+1)~pow(k,1/z);times:log(3w);
*/
#include<stdio.h>
#include<cstring>
#include<string>
#include<algorithm>
#include<math.h>
#define INF 0x3f3f3f3f
#define N 10010
using namespace std;
typedef long long ll;
//int k,x,z;
ll k;
ll qucikpow(ll a,ll b)
{
    ll ans=1;
    while(b)
    {
        if(b&1)
            ans*=a;
        a=a*a;
        b/=2;
    }
    return ans;
}
ll compute(ll x,ll y,ll z)
{
    ll ans=qucikpow(x,z)+qucikpow(y,z)+x*y*z;
    return ans;
}
int Slove(ll x,ll z)//根据此时的x z和y的范围找y 并且判断答案是否存在
{
    ll l=x+1;
    ll r,mid,ans;
    r=(ll)pow(k*1.0,1.0/z);
    while(l<r)
    {
        mid=(l+r)/2;
        ans=compute(x,mid,z);
        if(ans<k)
            l=mid+1;
        else
            r=mid;
    }
    if(l!=r)//防止r比l小
        return 0;
    ans=compute(x,r,z);
    if(ans==k)
        return 1;
    else
        return 0;
}
int main()
{
    int ans;
    ll lz;
    ll mid;
    while(~scanf("%lld",&k)&&k)//优化数据范围
    {
        ans=0;
        lz=log(k*1.0)/log(2.0);
        for(ll x=1;2*x*x<=k;x++)
        {
            mid=x*x;   
            for(ll z=2;mid<k&&z<=lz;z++)//
            {
                if(Slove(x,z))
                    ans++;
                mid*=x;
            }
        }
        printf("%d\n",ans);
    }
    return 0;
}```


