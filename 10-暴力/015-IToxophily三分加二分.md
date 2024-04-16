

### I - Toxophily


 

The recreation center of WHU ACM Team has indoor billiards, Ping Pang, chess and bridge, toxophily, deluxe ballrooms KTV rooms, fishing, climbing, and so on.  We all like toxophily.  Bob is hooked on toxophily recently. Assume that Bob is at point (0,0) and he wants to shoot the fruits on a nearby tree. He can adjust the angle to fix the trajectory. Unfortunately, he always fails at that. Can you help him?  Now given the object's coordinates, please calculate the angle between the arrow and x-axis at Bob's point. Assume that g=9.8N/m. 

**Input**

The input consists of several test cases. The first line of input consists of an integer T, indicating the number of test cases. Each test case is on a separated line, and it consists three floating point numbers: x, y, v. x and y indicate the coordinate of the fruit. v is the arrow's exit speed.  Technical Specification  1. T ≤ 100.  2. 0 ≤ x, y, v ≤ 10000. 

**Output**

For each test case, output the smallest answer rounded to six fractional digits on a separated line.  Output "-1", if there's no possible answer.  Please use radian as unit. 

**Sample Input**

```
3
0.222018 23.901887 121.909183
39.096669 110.210922 20.270030
138.355025 2028.716904 25.079551```


**Sample Output**

```
1.561582
-1
-1
```


#### 题意：


在一个平面坐标系中，你要射苹果，苹果在坐标（x,y），且你射箭的速度是v，重力加速度是9.8N/m，求射中苹果的时弓箭与x轴的弧度.

#### 思路：


枚举弓箭与x轴的弧度angle，每一个angle对应一个y，y为当箭与苹果在一条垂直线上时，箭的高度(可以为负)。

易证明随着angle的增大，其y是一个形似开口向上的抛物线，若其中的极大值大于苹果的高度Y，此时一定有界，可以三分求出此位置设为pos，那么二分枚举anlge在[0,pos]就可以求出来y==苹果的高度时的弓箭与x轴的弧度

如果对三分不了解，传送门：[https://www.cnblogs.com/whywhy/p/4886641.html](https://www.cnblogs.com/whywhy/p/4886641.html)

代码：

```cpp
#include<cstdio>
#include<algorithm>
#include<cmath>
using namespace std;
const double pi=acos(-1);
const double wc=1e-8;
double X,Y,V;
double f(double x)/*先求极大值 然后二分找答案*/
{
    double ans=0;
    double t=X/(V*cos(x));
    ans=V*sin(x)*t-0.5*9.8*t*t;
    return ans;
}
int main()
{
    double l,r,maxx;
    int t;
    scanf("%d",&t);
    while(t--)
    {
        scanf("%lf%lf%lf",&X,&Y,&V);
        l=0.0,r=pi/2.0;
        while(r-l>wc)
        {
            double M1=l+(r-l)/3;
            double M2=r-(r-l)/3;
            if(f(M1)<f(M2))
                l=M1;
            else
                r=M2;
        }
        maxx=(r+l)/2.0;
        if(f(maxx)<Y)
        {
             printf("-1\n");
             continue;
        }
        /*二分求答案*/
        l=0.0,r=maxx;
        while(r-l>wc)
        {
            double mid=(l+r)/2.0;
            if(f(mid)<Y)
                l=mid;
            else
                r=mid;
        }
        printf("%.6f\n",(l+r)/2);
    }
    return 0;
}```


 

 

二分/三分

