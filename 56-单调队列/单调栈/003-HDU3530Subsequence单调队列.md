

题目：

题意：

给你一个长度为n的数组，要求一段**连续的子序列**满足子序列中最大值减去最小值在$[m,k]$范围内。求该子序列的最大长度。

思路：我们假设区间右边界为$i$，然后求下标$[1,i]$中满足最大值减去最小值在[m,k]范围内的最小左边界。我们可以用单调队列维护一个当前前缀最大值序列和最小值序列。可以用下列步骤描述：

+ 将下标为$i$的值加入单调队列。+ 查看**最大值单调队列队首**减去**最小值单调队列队首**<=k是否满足， 
  
+ 如果不满足，我们让其下标最靠左边的出队，再次判断，直至队列为空或满足<=k停止。+ 满足则进行令i=i+1继续进行第3步。
 + 在前面出队的时候记录下出队的最大下标即为now，那么now就是区间不能取的最大位置。+ 查看**最大值单调队列队首**减去**最小值单调队列队首**>=m是否满足，如果满足用此时最长满足的区间下标为$[now+1,i]$,更新答案。否则对于$i$不可能有满足条件的区间左端点，不更新答案，并判断i+1


代码：

```cpp
#include<bits/stdc++.h>
#define mset(a,b) memset(a,b,sizeof(a))
using namespace std;
typedef long long ll;
typedef pair<int,int> P;
const int inf=0x3f3f3f3f;
deque<int> q1,q2;
int A[100000+10];
int main()
{
    int n,m,k;
    while(~scanf("%d%d%d",&n,&m,&k))
    {
        q1.clear();q2.clear();
        for(int i=1;i<=n;++i) scanf("%d",A+i);
        int ans=0,no=0;//no为对于当前左边界
        for(int i=1;i<=n;++i){
            while(!q1.empty()&&A[i]>=A[q1.back()]) q1.pop_back();
            q1.push_back(i);
            while(!q2.empty()&&A[i]<=A[q2.back()]) q2.pop_back();
            q2.push_back(i);
            //去掉无效的值
            while(!q1.empty()&&!q2.empty()&&A[q1.front()]-A[q2.front()]>k)
            {
                if(q1.front()<q2.front()){
                    no=q1.front();
                    q1.pop_front();
                }
                else{
                    no=q2.front();
                    q2.pop_front();
                }
            }
            if(!q1.empty()&&!q2.empty()&&A[q1.front()]-A[q2.front()]>=m)
                ans=max(ans,i-no);
        }
        cout<<ans<<endl;
    }
}
```


