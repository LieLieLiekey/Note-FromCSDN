


+  
## H 幻方变换(puzzle)（NYIST 2019年校赛）
 



如果一个 3 × 3 的矩阵中，整数 1-9 中的每个都恰好出现一次，我们称这个矩阵为一个幻 方。

我们可以对一个幻方进行一些操作。具体来说，我们可以

• 选择幻方的一行，整体向右移动一格，并将最右侧的数字移到最左边；或者

• 选择幻方的一列，整体向下移动一格，并将最下侧的数字移到最上面。

例如，下面两个操作分别是一种合法的行操作和列操作：


![./figures/9b9944d4e8b854f3bd0fddb13ef3d196.png](./figures/9b9944d4e8b854f3bd0fddb13ef3d196.png)


显然，一个合法的幻方经过一次操作后一定还是合法的幻方。

给定幻方的初始状态，请问，最少要经过多少次变换，才能变成最终状态？

### 输入描述:


```bash
第一行一个整数 T (1 ≤ T ≤ 200000)，表示测试用例的数量。

接下来有 T 组测试用例，每组测试用例前有一个空行。每组样例的前 3 行为幻方的初始状态，后 3 行为幻方的最终状态。每行的数字之间没有空格。

保证初始状态和最终状态都是合法的幻方。
```


### 输出描述:


```bash
对于每组测试用例在一行内输出一个整数，表示答案。如果不可能从起始状态转变为最终状态，输出 impossible。
```


### 样例输入:


```bash
4

1```


