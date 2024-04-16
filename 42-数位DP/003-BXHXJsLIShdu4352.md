

### B - XHXJ’s LIS


define xhxj (Xin Hang senior sister(学姐)) If you do not know xhxj, then carefully reading the entire description is very important. As the strongest fighting force in UESTC, xhxj grew up in Jintang, a border town of Chengdu. Like many god cattles, xhxj has a legendary life: 2010.04, had not yet begun to learn the algorithm, xhxj won the second prize in the university contest. And in this fall, xhxj got one gold medal and one silver medal of regional contest. In the next year’s summer, xhxj was invited to Beijing to attend the astar onsite. A few months later, xhxj got two gold medals and was also qualified for world’s final. However, xhxj was defeated by zhymaoiing in the competition that determined who would go to the world’s final(there is only one team for every university to send to the world’s final) .Now, xhxj is much more stronger than ever，and she will go to the dreaming country to compete in TCO final. As you see, xhxj always keeps a short hair(reasons unknown), so she looks like a boy( I will not tell you she is actually a lovely girl), wearing yellow T-shirt. When she is not talking, her round face feels very lovely, attracting others to touch her face gently。Unlike God Luo’s, another UESTC god cattle who has cool and noble charm, xhxj is quite approachable, lively, clever. On the other hand,xhxj is very sensitive to the beautiful properties, “this problem has a very good properties”，she always said that after ACing a very hard problem. She often helps in finding solutions, even though she is not good at the problems of that type. Xhxj loves many games such as，Dota, ocg, mahjong, Starcraft 2, Diablo 3.etc，if you can beat her in any game above, you will get her admire and become a god cattle. She is very concerned with her younger schoolfellows, if she saw someone on a DOTA platform, she would say: “Why do not you go to improve your programming skill”. When she receives sincere compliments from others, she would say modestly: "Please don’t flatter at me.(Please don’t black)."As she will graduate after no more than one year, xhxj also wants to fall in love. However, the man in her dreams has not yet appeared, so she now prefers girls. Another hobby of xhxj is yy(speculation) some magical problems to discover the special properties. For example, when she see a number, she would think whether the digits of a number are strictly increasing. If you consider the number as a string and can get a longest strictly increasing subsequence the length of which is equal to k, the power of this number is k… It is very simple to determine a single number’s power, but is it also easy to solve this problem with the numbers within an interval? xhxj has a little tired，she want a god cattle to help her solve this problem,the problem is: Determine how many numbers have the power value k in [L，R] in O(1)time. For the first one to solve this problem，xhxj will upgrade 20 favorability rate。

**Input**

First a integer T(T<=10000),then T lines follow, every line has three positive integer L,R,K.( 0<L<=R<2 63-1 and 1<=K<=10).

**Output**

For each query, print “Case #t: ans” in a line, in which t is the number of the test case starting from 1 and ans is the answer.

**Sample Input**


1 123 321 2


**Sample Output**


Case #1: 139


这题比较有意思，在把前面的状态压缩时用了一个非常巧妙的办法。

##### 参考博客：[https://www.cnblogs.com/dilthey/p/8525413.html](https://www.cnblogs.com/dilthey/p/8525413.html)


##### 题意：


在区间【a,b】找有多少个数满足下列。条件：这个数的十进制位的最长递增长度等于K.

##### 分析：


数位dp的时候把前缀的数的状态记录下即可，但是该怎么记录呢？

在nlogn的最长递增子序列的求法中每一个序列都确定一个数组d,d[top]就是长度为top的子序列的最大值是多少，

这里面top的范围是1~10,所有出现的最大值的范围是0~9,所以这里可以采用一个十个2进制位的形式进行压缩。肯定有点迷吧，让我慢慢解释…

对于一个上面的数组d[top]，其里面的值随着下标的增大是逐渐递增的，所以如果咱们知道数组d中的所有值，那么这个数组d就确定了，换句话就是说前缀的数的状态确定了。

这里咱们采用十个2进制位进行压缩，如果num位为1，就代表这个num数字在数组d中出现过，这样就用一个二进制数来表示前缀的数的状态了。

举个栗子：


我们化用一下这个数组d，用0~9十个位的0 or 1来表示，这个d数组里存了啥，比如说假设d[1]=1，d[2]=3，d[3]=5，d[4]=6，那么在本题下的形式就是sta = 0001101010


十个2进制位1有多少个 ，就代表这个状态最长递增子序列的长度为几。

**初始情况 ：**

​ sta

