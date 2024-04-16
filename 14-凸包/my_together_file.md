

## Gragham扫描法求凸包对点的排序有两种方式


+ 极角排序+ x，y坐标的升序排序


求凸包核心思想就是利用向量的叉积判断点的转向，使得所有的点都是向左转，且包含在多边形内部里面。

 

第一种最容易理解，而第二种代码风格最简洁。

第一种的kuangbin代码

```cpp

/*
* 求凸包，Graham算法
* 点的编号0~n-1
* 返回凸包结果Stack[0~top-1]为凸包的编号
*/
class Point{
public:
    double x,y;
    Point(){}
    Point(double x,double y):x(x),y(y){
    }
    Point operator+ (Point p){
        return Point(add(x,p.x),add(y,p.y));
    }
    Point operator -(Point p){
        return Point(add(x,-p.x),add(y,-p.y));
    }
    Point operator *(double d){
        return Point(x*d,y*d);
    }
    double operator *(Point p){
        return add(x*p.x,y*p.y);//外积
    }
    double operator ^(Point p){//内积
        return add(x*p.y,-y*p.x);
    }
    double det(Point p){
     return add(x*p.y,-y*p.x);
    }
    double len(){
        return sqrt(add(x*x,y*y));
    }
};
const int MAXN = 1010;
Point list[MAXN];
int Stack[MAXN],top; //相对于list[0]的极角排序
bool _cmp(Point p1,Point p2)
{
    double tmp = (p1-list[0])^(p2-list[0]);
    if(sgn(tmp) > 0)return true;
    else if(sgn(tmp) == 0 && sgn(dist(p1,list[0]) - dist(p2,list[0])) <= 0)   return true;
    else return false;
}
void Graham(int n)
{
    Point p0;
    int k = 0;
    p0 = list[0];  //找最下边的一个点
    for(int i = 1; i < n; i++)
    {
        if( (p0.y > list[i].y) || (p0.y == list[i].y && p0.x > list[i].x) )
        {
            p0 = list[i];
            k = i;
        }
    }
    swap(list[k],list[0]);
    sort(list+1,list+n,_cmp);
    if(n == 1)
    {
        top = 1;
        Stack[0] = 0;
        return;
    }
    if(n == 2)
    {
        top = 2;
        Stack[0] = 0;
        Stack[1] = 1;
        return ;
    }
    Stack[0] = 0;
    Stack[1] = 1;
    top = 2;
    for(int i = 2; i < n; i++)
    {
        while(top > 1 && sgn((list[Stack[top-1]]-list[Stack[top-2]])^(list[i]-list[Stack[top-2]])) <= 0)

            top--;
        Stack[top++] = i;
    }
}
```


 

第二种在挑战书上的代码

```cpp
double add(double a,double b){//考虑误差的加法运算
    if(abs(a+b)<EPS*(abs(a)+abs(b))) return  0;
    return a+b;
}
class Point{
public:
    double x,y;
    Point(){}
    Point(double x,double y):x(x),y(y){
    }
    Point operator+ (Point p){
        return Point(add(x,p.x),add(y,p.y));
    }
    Point operator -(Point p){
        return Point(add(x,-p.x),add(y,-p.y));
    }
    Point operator *(double d){
        return Point(x*d,y*d);
    }
    double operator *(Point p){
        return add(x*p.x,y*p.y);//外积
    }
    double operator ^(Point p){//内积
        return add(x*p.y,-y*p.x);
    }
    double det(Point p){
     return add(x*p.y,-y*p.x);
    }
    double len(){
        return sqrt(add(x*x,y*y));
    }
};
//Gragham扫描法求凸包
//输入: 多边形和顶点个数
//得到的凸包的点最少，逆时针给出，第一个点是最靠左其次下的点。
bool cmp_x(const Point &p,const Point &q)
{
    if(p.x!=q.x) return p.x<q.x;
    return p.y<q.y;
}
vector<Point> convex_hull(Point *ps,int n)
{
    sort(ps,ps+n,cmp_x);
    int k=0; //凸包的顶点数
    vector<Point> qs(n*2); //构造中的凸包
    //构造凸包下侧
    for(int i=0; i<n;++i){
        while(k>1 && (qs[k-1]-qs[k-2]).det(ps[i]-qs[k-1]) <= 0) k--;
        qs[k++] = ps[i];
    }
    //构造凸包的上侧
    for(int i=n-2,t=k;i>=0;--i){
        while(k>t && (qs[k-1] - qs[k-2] ).det(ps[i]-qs[k-1]) <= 0 ) k--;
        qs[k++]=ps[i];
    }
    qs.resize(k-1);
    return qs;
}```


自己也实现了一下，基本跟书上差不多，但判断点的转向时有些差异，不过代码效果应该都一样。

```cpp
vector<Point> convex_hull(Point *ps,int n)
{
    sort(ps,ps+n,cmp_x);
    int k=0; //凸包的顶点数
    vector<Point> qs(n*2); //构造中的凸包
    //构造凸包下侧
    for(int i=0; i<n;++i){
        while(k>1 && (qs[k-1]-qs[k-2]).det(ps[i]-qs[k-2]) <= 0) k--;
        qs[k++] = ps[i];
    }
    //构造凸包的上侧
    for(int i=n-2,t=k;i>=0;--i){
        while(k>t && (qs[k-1] - qs[k-2] ).det(ps[i]-qs[k-2]) <= 0 ) k--;
        qs[k++]=ps[i];
    }
    qs.resize(k-1);
    return qs;
}```


 



上述中说的三种是方式分别是


+ kuangbin的-容易理解
+ 挑战书上的-容易实现
+ 我的-我的理解



第一种kuangbin板子

```cpp
class Point
{
public:
    double x,y;
    Point() {}
    Point(double x,double y):x(x),y(y)
    {
    }
    Point operator+ (Point p)
    {
        return Point(add(x,p.x),add(y,p.y));
    }
    Point operator -(Point p)
    {
        return Point(add(x,-p.x),add(y,-p.y));
    }
    Point operator *(double d)
    {
        return Point(x*d,y*d);
    }
    double operator *(Point p)
    {
        return add(x*p.x,y*p.y);//外积
    }
    double operator ^(Point p) //内积
    {
        return add(x*p.y,-y*p.x);
    }
    double det(Point p)
    {
        return add(x*p.y,-y*p.x);
    }
    double len()
    {
        return sqrt(add(x*x,y*y));
    }
};
}
//旋转卡壳，求两点间距离平方的最大值
int rotating_calipers(Point p[],int n)//要求p序列为凸包序列
{
    int ans = 0;
    Point v;
    int cur = 1;
    for(int i = 0; i < n; i++)
   ```


