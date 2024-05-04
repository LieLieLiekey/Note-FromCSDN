

### [ KiKi’s K-Number](https://vjudge.net/problem/HDU-2852)  (树状数组)


[HDU - 2852 ](https://vjudge.net/problem/17358/origin)

**题意：**
```
题意：题目给定三种操作:
 0 x 表示把x插入容器 ; 
 1 x 表示删除一个x, 如果没有x则输出 No Element! ;
2 a k 表示比a大的数中的第k大的数 如果没有输出No Find!
```
**思路：**

​ 树状数组维护元素出现次数前缀和即可。
操作0即修改；
操作1先查询x是否存在，如果存在删除一个即可。
操作2可以用二分逐渐逼近答案。

```cpp
#include<bits/stdc++.h>
#define mset(a,b) memset(a,b,sizeof(a))
using namespace std;
typedef long long ll;
const ll MAXN=1e5+20;
const int MAX=100000;
int bt[MAXN];
int lowbit(int k)
{
    return k&-k;
}
void modify(int k,int val)
{
    while(k<=MAX)
    {
        bt[k]+=val;
        k+=lowbit(k);
    }
}
int getsum(int k)
{
    int ans=0;
    while(k>0)
    {
        ans+=bt[k];
        k-=lowbit(k);
    }
    return ans;
}
int clac(int a,int b)
{
    return getsum(b)-getsum(a-1);
}
int m,tot;
int main()
{
    while(~scanf("%d",&m))
    {
        mset(bt,0);
        tot=0;
        while(m--)
        {
            int sign;
            scanf("%d",&sign);
            if(sign==0)
            {
                int val;
                scanf("%d",&val);
                modify(val,1);
                tot++;
            }
            if(sign==1){
                int val;
                scanf("%d",&val);

                if(clac(val,val)==0){
                    puts("No Elment!");
                }
                else{
                    modify(val,-1);
                    tot--;
                }
            }
            if(sign==2){
                int a,k;
                scanf("%d%d",&a,&k);
                int ans=-1,l=a+1,r=MAX;
                while(l<=r){
                    int mid=(l+r)/2;
                    if(clac(a+1,mid)>=k){
                        ans=mid;
                        r=mid-1;
                    }
                    else
                        l=mid+1;
                }
                if(ans==-1){
                    puts("Not Find!");
                }
                else
                    printf("%d\n",ans);
            }
        }
    }

}

```
