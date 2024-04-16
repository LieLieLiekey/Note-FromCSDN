

## codeforces 1253 E. Antenna Coverage（DP）


##### 题意：


现有一个一维的OX轴，给出n个antenna，每个antenna的属性有$( x i , r i ) (x_i,r_i)$,代表该antenna 可以覆盖区间$[ x i − r i , x i + r i ] [x_i-r_i,x_i+r_i]$，我们可以花费一个硬币使得某个antenna的 $r r$ 增大1，问使区间$[ 1 , m ] [1,m]$都被某个antenna覆盖所需最小花费。$n ∈ [ 1 , 80 ] , m ∈ [ 1 , 2 e 5 ] , x i ∈ [ 1 , m ] n\in[1,80],m\in[1,2e5],x_i\in [1,m]$,

##### 思路：


因为所有antenna的中心都在$[ 1 , m ] [1,m]$，所以我们在位置0处放一个半径为0的antenna答案不收影响，（因为位置0处的antenna覆盖到位置x，那么x+1位置必定被覆盖了，所以x+1位置必定能花费同样的硬币进行扩展到左边的位置1，我们覆盖位置$[ 1 , x ] [1,x]$所需要的花费不会比之前坏）。我们用$d p [ p o s ] dp[pos]$代表假设位置$p o$

