

### HDU-4122 Alice’s mooncake shop 单调队列


**题目：** [HDU - 4122 ](https://cn.vjudge.net/problem/25789/origin)

**题意：**

**输入：**

第一行两个数n,m. 代表n份订单 m小时制作月饼.

接下来有n行，每一行有订单的时间 （月 日 年 小时） 和 需要月饼的数量cnt .

接下来一行两个数T,timecost. 代表每个月饼的保质期为T 放冰箱每小时需要timecost的代价.

接下来有 $m$ 行，第$i$行代表第 $i-1$ 小时制作月饼的代价求完成所有月饼所需的代价.

**输出：**

求将所有订单完成的最小花费。

注：2000年1月1日0小时代表第0小时。

**思路：**

比较暴力的方法是

+ 处理出每个订单的时间和数量+ 对于每个订单期望找出时间(nowt-T,nowt)的最小花费。+ 每个订单用最小花费 $*$ 订单内月饼的个数来得到该订单的总最小花费。


显然这种方法时间复杂度为$T*m$,过大，不过看到这里都应该理解题意了。

我们使用单调队列，优先队列存储{时间,该时间的成本}。那么对于时间t，如果队尾处没有比此时更优，就删除队尾一个元素。如果此时有订单，就使用队首部处理该订单。

**代码：**

```cpp
/*
思路：
1.处理出每个订单的时间和数量
2.对于每个订单期望找出时间(T-nowt,nowt)的最小单位花费
3.处理出最小单位花费
或：代码是使用此种类方法
1.处理出每个订单的时间和数量,保证时间递增
2.遍历每个时间，处理出当当前时间的最小花费。然后查看该时间是否为下一个订单，如果是就从最小花费单调队列中出队至符合条件的一个。
*/#include<bits/stdc++.h>
#define mset(a,b) memset(a,b,sizeof(a))
using namespace std;
typedef long long ll;
typedef pair<ll,ll> P;
P order[2500+10];
deque<P> q;
map<string,ll> mmp;
ll getDay(ll y,ll m,ll d)//第y年m月d天
{
    ll sum=0;
    ll yy=y-1;
    sum=yy*365+(yy/4-yy/100+yy/400);
    for(ll i=1;i<m;++i){
        if(i==2) sum+=28+(((y%4==0&&y%100!=0)||y%400==0)?1:0);
        else if(i==1||i==3||i==5||i==7 ||i==8 ||i==10 ||i==12) sum+=31;
        else sum+=30;
    }
    sum+=d;
    return sum;
}
ll gethours(string mouth,ll day,ll year,ll hour)//2000-1-1 0是第0小时
{
    ll m=mmp[mouth],t=0;
    ll sum=getDay(year,m,day)-getDay(2000,1,0)-1;//从2000年开始到现在纯共有sum天
    sum*=24;
    sum+=hour;
    return sum;
}
void init()
{
    mmp["Jan"]=1,mmp["Feb"]=2,mmp["Mar"]=3,mmp["Apr"]=4,mmp["May"]=5,mmp["Jun"]=6,mmp["Jul"]=7,mmp["Aug"]=8;
    mmp["Sep"]=9,mmp["Oct"]=10,mmp["Nov"]=11,mmp["Dec"]=12;
}
int main()
{
    ll T,sum,timecost,n,m;
    ios::sync_with_stdio(false);cin.tie(0);
    init();
    while(cin>>n>>m,n)
    {
        q.clear();
        sum=0ll;
        string mouth;
        ll day,year,hour,cnt;
        for(ll i=1;i<=n;++i){
            cin>>mouth>>day>>year>>hour>>cnt;
            order[i].first=gethours(mouth,day,year,hour);
            order[i].second=cnt;
        }
        cin>>T>>timecost;
        ll p=1;
        for(ll i=0;i<m;++i){
            ll x;
            cin>>x;//第i次的花费
            while(!q.empty()&&((q.back().second+(i-q.back().first)*timecost)>=x)) q.pop_back();
                q.push_back({i,x});
            while(order[p].first==i){
                while(!q.empty()&&(q.front().first+T<i)) q.pop_front();
                ll cnt=order[p].second;
                sum+=cnt*(q.front().second+(i-q.front().first)*timecost);
                ++p;
            }
        }
        cout<<sum<<endl;
    }
    return 0;
}
```


