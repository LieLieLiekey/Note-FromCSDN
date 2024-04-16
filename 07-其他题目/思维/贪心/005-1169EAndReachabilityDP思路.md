

## 1169E. And Reachability(DP+思路)


题目链接：[传送门](https://codeforces.com/contest/1169/problem/E)

思路：

涉及到位运算，很容易想到按位考虑。

我们用$g o [ i ] [ j ] go[i][j]$表示第 $i i$ 个数可以到达第 $j j$ 位为1的最小下标是多少，如果没有则等于$n + 1 n+1$。

对于这个状态方程，我们倒过来递推，我们让 $i i$ 从 $n n$ 开始遍历到 $1 1$ ,并用$l a s t [ k ] last[k]$ 表示满足 $j > i j>i$ 且 $a j a_j$ 的第 $k k$

