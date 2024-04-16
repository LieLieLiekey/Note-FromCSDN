

### F - Co-prime


Given a number N, you are asked to count the number of integers between A and B inclusive which are relatively prime to N. Two integers are said to be co-prime or relatively prime if they have no common positive divisors other than 1 or, equivalently, if their greatest common divisor is 1. The number 1 is relatively prime to every integer.

Input

The first line on input contains T (0 < T <= 100) the number of test cases, each of the next T lines contains three integers A, B, N where (1 <= A <= B <= 1015) and (1 <=N <= 109).

Output

For each test case, print the number of integers between A and B inclusive which are relatively prime to N. Follow the output format below.

Sample Input

```bash
2
1 10 2
3 15 5
```


Sample Output

```bash
Case #1: 5
Case #2: 10


        
  
```


Hint

```bash
In the first test case, the five integers in range [1,10] which are relatively prime to 2 are {1,3,5,7,9}. 
        
 
```


题意：


t组输入

每组给出三个数 a,b,n(1 <= A <= B <= 1015) and (1 <=n <= 109).

让你求[a，b]区间中与n互质的个数


用f（b,n）代表[1,b]中与n互质的个数，那么答案就是f（b,n）-f（a-1,n），这一点应该都能想到，所以只要求出f（b,n)即可。

f函数的求法，因为一个数要么与n互质 要么与n不互质，所以**1到b与n互质**的可以转化成**b减去 1到b中与n不互质的个数**，如果一个数与n不互质，那么必存在一个>1的公因子，那么运用容斥原理，

假设求 1到100与6互质的个数 ,因为6的所有质因子为 2，3

​ $100/2+100/3-100/(2*3)$

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
vector<int> fp;//用数组ui记录前k个数的各种组合
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
ll f(ll a,int b)//求1~a中 互质的数目
{

    if(a==0)
        return 0;
    ll sum=0;
    int cnt=0;
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
    int t,n,cas;
    ll a,b;
    ios::sync_with_stdio(false);
    scanf("%d",&t);
    cas=0;
    init();
    while(t--)
    {
        cin>>a>>b>>n;
        get_prime(n,fp);
        printf("Case #%d: ",++cas);
        cout<<f(b,n)-f(a-1,n)<<endl;
    }
    return 0;
}

```


