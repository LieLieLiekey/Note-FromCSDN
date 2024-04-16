

## 2019CCPC哈尔滨Artful Paintings（二分+差分约束）


题目链接：[传送门](https://codeforces.com/gym/102394/problem/A)

思路：


这题现场赛的时候TLE了，赛后才发现spfa可以剪枝，而且还缺少一约束。


我们假设答案是k，那么k+1也可行，所以可行性具有单调性。设函数S( i )为前 i 个cube画的个数。

那么有约束


+ $1 ≥ S ( i ) − S ( i − 1 ) ≥ 0 1\ge S(i)-S(i-1)\ge0$
+ 对于第一种条件，$S ( r ) − S ( l − 1 ) ≥ k S(r)-S(l-1)\ge k$
+ 对于第二种条件，$S ( n ) − S ( r ) + S ( l − 1 ) ≥ k S(n)-S(r)+S(l-1)\ge k$



因为对于第二种条件， $S ($

