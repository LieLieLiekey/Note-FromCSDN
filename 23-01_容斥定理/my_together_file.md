

容斥的几种写法


容斥公式本身就是 **枚举出状态的组合**，算其乘积，奇数个值为负，偶数个值为正

原理：

对于组合中每个状态有 **在**或**不在**两种，求其组合，可以用二进制枚举，也可以用递归

+ 二进制+ 两层for循环+ 递归



```cpp
#include<cstdio>
#include<algorithm>
#include<string>
#include<cstring>
#include<iostream>
#include<iomanip>
#include<map>
#include<vector>
#include<time.h>
#define mset(a,b)   memset(a,b,sizeof(a))
using namespace std;
typedef unsigned long long ull;
typedef long long ll;
const int maxn=1e5;
const int branch=26;
const int inf=0x3f3f3f3f;
const int MOD=1e6+7;
//假设有tot个数，存储在num数组中
int num[20];//存放数字种类
int rc[maxn];//存放容斥的组合
int tot;//数字种类数
int cnt;//容斥组合的个数
void rc_for()//求出num中 tot个数的所有组合
{
    cnt=0;
    rc[cnt++]=1;//初始状态
    for(int i=0; i<tot; ++i)
    {
        int k=cnt;//下标为i的数与前k个数的所有组合的组合
        for(int j=0; j<k; ++j)
        {
            rc[cnt++]=num[i]*rc[j]*-1;//奇数个为负
        }
    }
}
void rc_bit()//用二进制来写
{
    int top=1<<tot;//共tot个数字
    cnt=0;
    for(int i=0; i<top; ++i)
    {
        int val=1;
        for(int k=0; k<tot; ++k) //枚举每个位是否为1 为1的组合整上去
        {
            if((1<<k)&i)
            {
                val*=-1*num[k];
            }
        }
        rc[cnt++]=val;
    }
}
void dfs(int k,int val)//正在枚举下标为k的状态, 之前组合乘积为-1
{
    if(k==tot)
    {
        rc[cnt++]=val;
        return ;
    }
    dfs(k+1,val*-1*num[k]);//下标为k的状态在组合中
    dfs(k+1,val);
}
void rc_dfs()
{
    cnt=0;
    dfs(0,1);//
}
int main()
{
    //主要是枚举这些数的所有组合(不能重复)
    /*
    测试
    */
    scanf("%d",&tot);
    for(int i=0; i<tot; ++i)
        scanf("%d",num+i);
    rc_for();
    printf("\nrc_for.........\n");
    cout<<"cnt:"<<cnt<<endl;
    for(int i=0; i<cnt; ++i)
        printf("%d ",rc[i]);
    puts("");
    printf("rc_bit.........\n");
    rc_bit();
    cout<<"cnt:"<<cnt<<endl;
    for(int i=0; i<cnt; ++i)
        printf("%d ",rc[i]);
    puts("");
    rc_dfs();
    cout<<"cnt:"<<cnt<<endl;
    for(int i=0; i<cnt; ++i)
        printf("%d ",rc[i]);
    return 0;
}

```




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


