

### [D - Farm Tour](https://vjudge.net/problem/POJ-2135)（最小费用流）


[POJ - 2135](https://vjudge.net/problem/16586/origin)

#### 思路：


​ 问题可以转化为求两条$1 1$到$n n$的路径，使得这两条路径没有重边且费用和最小。而这个问题我们又可以转化为最小费用流问题。对于$u u$到$v v$的费用为$w w$双向边，在图中转化为$u u$到$v v$容量$1 1$费用为$w w$的边和$v v$到$u u$容量为$1 1$，费用为$w w$的边； 求$1 1$到$n n$流量为$2 ​ 2​$

