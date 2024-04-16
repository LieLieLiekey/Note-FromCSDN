

### G - Visible Trees


There are many trees forming a m * n grid, the grid starts from (1,1). Farmer Sherlock is standing at (0,0) point. He wonders how many trees he can see.

If two trees and Sherlock are in one line, Farmer Sherlock can only see the tree nearest to him.

**Input**

The first line contains one integer t, represents the number of test cases. Then there are multiple test cases. For each test case there is one line containing two integers m and n(1 ≤ m, n ≤ 100000)

**Output**

For each test case output one line represents the number of trees Farmer Sherlock can see.

**Sample Input**

```bash
2
1 1
2 3
```


**Sample Output**

```bash
1
5
```


题意：


一个m*n的格子，每个格子里面都是一棵树，左上角坐标为（1，1），右上角坐标为（m，n）,假设你站在（0，0），你最多能看到多少棵树

m=2,n=3时

​ @@@

​ @@@

能看见(1,1),(1,2),(1,3)(2,1)(2,3)这五棵树，因为从（0,0）看（2，2）的过程中被树（1，1）挡住了


这道题其实就是对于每棵树(x,y),如果说x,y存在大于1的公因子，证明(x,y)这棵树肯定被挡住了，被挡住的这个线的斜率为y/x，因为k>1，所以在这一条线这棵树不能被看到，如果互为素数，证明(x，y)这颗树肯定没被挡住，故求矩阵中互素的坐标即可。

```cpp
#include<cstdio>
#include<algorithm>
#include<string>
#include<cstring>
#include<iostream>
#include<iomanip>
#include<map>
#include<vector>
#define mset(a,b)   memset(a,b,sizeof(a))
using namespace std;
typedef unsigned long long ull;
typedef long long ll;
const int maxn=1e5;
const int branch=26;
const int inf=0x3f3f3f3f;
const int MOD=1e6+7;
int book[maxn+10],prime[(int)5e4+10];
int ui[maxn+10];
int top;
//vector<int> fp;//用数组ui记录前k个数的各种组合
void init()
{
    top=0;
    book[0]=book[1]=1;
    for(int i=2;i*i<=maxn;++i)
        if(!book[i])
    {
        for(int j=i*i;j<=maxn;j+=i)
            book[j]=1;
    }
    for(int i=2;i<=maxn;++i)
        if(!book[i])
            prime[top++]=i;
}
void get_prime(int val,vector<int>& pf)//求出val的所有素因子 返回到vector内
{
    pf.clear();
    for(int i=0;prime[i]*prime[i]<=val;++i)
    {
        if(!(val%prime[i]))
        {
             pf.push_back(prime[i]);
//             printf("%d ",prime[i]);
        }

        while(!(val%prime[i]))
        {
            val/=prime[i];
        }
    }
    if(val>1)
    {
         pf.push_back(val);
//         printf("%d ",val);
    }
//    puts("");

}
int f(int a,int b)//求1~a中 互质的数目
{

    if(a==0)
        return 0;
    int sum=0;
    int cnt=0;
    vector<int>fp;
    get_prime(b,fp);
    ui[cnt++]=1;
    int t;//记下前几个组合的个数   前几个组合存在ui数字里面。
    for(int i=0;i<fp.size();++i)//第i+1个数与前i个数的各种组合搞
    {
        t=cnt;
        for(int j=0;j<t;++j)
        {
            ui[cnt++]=fp[i]*ui[j]*-1;
        }
    }
    for(int i=0;i<cnt;++i)
    {
        sum+=a/ui[i];
//        cout<<ui[i]<<" ";
    }
//    cout<<endl;
    return sum;
}
int main()
{
    int t,a,b;
    ll sum;
    init();
    scanf("%d",&t);
    while(t--)
    {
        scanf("%d %d",&a,&b);
        sum=0ll;
        for(int i=1;i<=a;++i)
        {
            sum+=f(b,i);
        }
        printf("%lld\n",sum);
    }
}
```


