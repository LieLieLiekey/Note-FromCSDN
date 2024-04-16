

## Codeforces Global Round 5(赛后补题)



这场的体验挺好的，总体感觉题目给自己一些了good idea，不过就是比赛过程中不争气，只做出来了仅仅三道题目（赛后补题+两道


##### 比赛链接：[传送门](https://codeforces.com/contest/1237)


##### A - Balanced Rating Changes



水


```cpp
#include<bits/stdc++.h>
#define mset(a,b) memset(a,b,sizeof(a))
using namespace std;
typedef long long ll;
const int N=2e4+5;
int a[N],b[N];
int main()
{
   
    ios::sync_with_stdio(false);
    cin.tie(0);
    int n,t;
    cin>>n;
    t=0;
    for(int i=1; i<=n; ++i)
    {
   
        cin>>a[i];
        if(abs(a[i])&1) t++;
        else b[i]=a[i]/2;
    }
    t/=2;
    for(int i=1; i<=n; ++i)
    {
   
        if((abs(a[i])&1))
        {
   
            if(t>0)
            {
   
                b[i]=(a[i]+1)/2;
                t--;
            }
            else
            {
   
                b[i]=(a[i]-1)/2;
            }
 
        }
    }
    for(int i=1; i<=n; ++i)
        cout<<b[i]<<endl;
}
```


##### B - Balanced Tunnel



水


思路：按照进入的顺序如果比车 $a a$ 与比该车之前进去的车 $b b$ 出来的早，那么车a就超车了

```cpp
#include<bits/stdc++.h>
#define mset(a,b) memset(a,b,sizeof(a))
using namespace std;
typedef long long ll;
const int inf=0x3f3f3f3f;
const int N=2e5+5;
int in[N],to[N],out[N],num[N];
int main()
{
   
    int n;
    scanf("%d",&n);
    for(int i=1;i<=n;++i){
   
        scanf("%d",in+i);
        to[in[i]]=i;
    }
    for(int i=1;i<=n;++i){
   
        scanf("%d",out+i);
        int ps=to[out[i]];
        num[ps```


