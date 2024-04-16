

Mr. West bought a new car! So he is travelling around the city.  One day he comes to a vertical corner. The street he is currently in has a width x, the street he wants to turn to has a width y. The car has a length l and a width d.  Can Mr. West go across the corner? 
![./figures/605e6d7e3698d2abbe292059d5224f9c](./figures/605e6d7e3698d2abbe292059d5224f9c)


**Input**

Every line has four real numbers, x, y, l and w.  Proceed to the end of file. 

**Output**

If he can go across the corner, print "yes". Print "no" otherwise. 

**Sample Input**

```
10 6 13.5 4
10 6 14.5 4```


**Sample Output**

```
yes
no```


#### 思路：


用下[https://blog.csdn.net/u013761036/article/details/24588987](https://blog.csdn.net/u013761036/article/details/24588987)博主的图


![./figures/20190116205558929.png](./figures/20190116205558929.png)


意思当车的右侧按不同的角度angle靠着右侧的墙走的时候，看是否能碰着拐角。即此时车身左侧的直线当y=X时，此时的横坐标在-Y的左边还是右边，如果满足情况下，-x<Y,证明车子可以过去，否则则不能。

因为随着angle角的增大，-x的值是一个形似开头向下的抛物线，故可以利用三分来求此抛物线的极点的值

 

```cpp
#include<cstdio>
#include<algorithm>
#include<cmath>
using namespace std;
const double wc=1e-6;
const double pi=acos(-1);
double X,Y,l,w;
double f(double x)//传弧度，返回Y=X时的-x的值
{
    return (l*sin(x)+w/cos(x)-X)/tan(x);
}
int main()
{
    while(~scanf("%lf%lf%lf%lf",&X,&Y,&l,&w))
    {
        double ll=0,rr=pi/2.0;
        while(rr-ll>wc)
        {
            double M1=ll+(rr-ll)/3;
            double M2=rr-(rr-ll)/3;
            if(f(M1)<f(M2))
                ll=M1;
            else
                rr=M2;
        }
        if(f(ll)<Y)
            printf("yes\n");
        else
            printf("no\n");
    }
    return 0;
}```


 

