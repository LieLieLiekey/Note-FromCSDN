

## Linux定时器



本文为对CSDN博主「songly_」的原创文章整理后著作的，遵循 CC 4.0 BY-SA 版权协议， 原文链接：https://blog.csdn.net/qq_35733751/article/details/82763230


#### struct：timerval


```cpp
//itimerval结构体中的成员类型为timeval
struct timeval {
    time_t      tv_sec;         /* 秒 */
    suseconds_t tv_usec;        /* 微秒 */
};
```


该结构体表示一个计时时间类型，可以存储秒+微妙

#### struct：itimerval


```cpp
struct itimerval {
    struct timeval it_interval; 	/* 周期性的定时器 */
    struct timeval it_value;        	/* 一次性定时器 */
};
```


这个表示一个计时器类型，具体使用情况如下：

+ 用`setitimer`函数来在指定的模式下注册定时器+ `it_value`的值将随着指定模式下的时间的流逝而减少对应的值，当减少到0时，会发出对应的信号，并让`it_value`的值重置为`it_interavl`；+ 当`it_interval`和`it_value`的值同时为0是时，计时器停止（只有初始情况下`it_interval`的值为0的时候才有可能停止），否则返回第二步。 
  
+ 注：`timeval`类型的值为0当且仅当其两个成员的值都为0
 


所以计时器的在不同情况的值下有不同的功能

+ 当`it_interval`的值为0，`it_value`的值不为0时，该计时器表示为一次性计时器，定时时间为`it_value`。+ 当`it_interval`的不值为0，`it_value`的值为0时，该计时器表示为周期性计时器，周期为`it_interval`。+ 当`it_interval`的不值为0 且 `it_value`的值不为0时，该计时器首先等待`it_value`的时间后发出对应的信号，之后变为一个周期为`it_interval`的定时器。


#### function：setitimer


**函数原型**：

```cpp
#include <sys/time.h>
int setitimer(int which , const struct itimerval *new_value , struct itimerval *old_value);
```


**返回值说明**：成功返回0；失败则返回-1并设置`errno`

**参数1**：

在调用`setitimer`创建定时器时，可通过指定参数`which`创建以下几种不同的定时器：

`ITIMER_REAL`：表示以linux系统的真实时间来计时的定时器，每次超时将会产生`SIGALRM`信号并发送给进程。

`ITIMER_VIRTUAL`：以进程在用户模式下执行的cpu时间来计时的定时器，每次超时将会产生`SIGVTALRM`信号并发送给进程

`ITIMER_PROF`：以进程在用户和内核两种模式下执行的cpu时间总和来计时的定时器，每次超时将会产生`SIGPROF`信号并发送给进程

**参数2，3**：

参数`new_value`指定定时器超时时间，参数`old_value`返回上一次定时器的时间，另外`new_value`和`old_value`两个参数的类型都是struct `itimerval`类型，如果参数`old_value`不为NULL时，函数会将上次对应模式下的定时器的状态存入`old_value`

注：需要注意的是，计时器只会在`which`指定的模式下计时的。


相似的还有更简单的alrm函数


##### 程序示例1：设置一次性定时器


实验以linux系统下的真实时间为例

```cpp
#include <stdio.h>
#include <sys/time.h>
#include <unistd.h>

int main(void)
{	    
        //把time初始化，这一步操作不能少
        struct itimerval time = {0};

        //设置一次性定时器，超时时间为3秒
        time.it_value.tv_usec = 0;
        time.it_value.tv_sec = 3;
        
        //如果不关心上一次定时器的超时时间，old_value可以传NULL
        setitimer(ITIMER_REAL , &time , NULL);
        //每隔1秒打印一次
        while(1){
                puts("hello world");
                sleep(1);
        }

        return 0;
}

```


输出结果：三行`hello world`+一行`Alarm clock`

通过程序执行结果来看，setitimer程序每隔1秒打印一次hello world，当定时器超时后，发送了`SIGALRM`信号并终止了该进程。

##### 程序实例2：设置周期性定时器


```cpp
#include <stdio.h>
#include <sys/time.h>
#include <unistd.h>
#include <signal.h>

void sig_handler(int signum){
        if(signum == SIGALRM){
                puts("hello SIGALRM");
        }
}

int main(void)
{
        //一定要把time初始化
        struct itimerval time = {0};  

        //设置一次性定时器，超时时间为4秒
        time.it_value.tv_usec = 0;
        time.it_value.tv_sec = 4;

        //设置周期性定时器，超时时间为3秒
        //表示第一次超时为4秒，之后每次超时为3秒
        time.it_interval.tv_sec = 3;
        time.it_interval.tv_usec = 0;

        signal(SIGALRM , sig_handler);

        setitimer(ITIMER_REAL , &time , NULL);

        while(1){
                puts("hello world");
                sleep(1);
        }

        return 0;
}

```


输出：

程序首先输出了四行`hello world`和一行`hello SIGALRM`，之后周期性输出三行`hello world`和一行`hello SIGALRM`，直至`ctrl+c`结束进程。

##### 程序示例3：自定义alarm函数


```cpp
#include <stdio.h>
#include <unistd.h>
#include <sys/time.h>
#include <string.h>

unsigned int myalarm(unsigned int seconds)
{
    struct itimerval old_time, itime;

    //清空itime,这一步操作一定要做
    memset(&itime , 0 , sizeof(itime));

    itime.it_value.tv_sec = seconds;
    setitimer(ITIMER_REAL,&itime,&old_time);
    //printf("tv_sec=%ld\n",old_time.it_value.tv_sec);
    return old_time.it_value.tv_sec;
}

int main()
{
    unsigned int ret = 0;
    //设置定时器的超时时间为10秒
    ret = myalarm(10);
    printf("old_time = %d\n",ret);
    sleep(3);
    //第二次修改了定时器的超时时间为3秒
    ret = myalarm(3);

    //获取到的上一次定时器时间
    printf("old_time = %d\n",ret);

    while(1){
        printf("hello world\n");
        sleep(1);
    }
    return 0;
}
```


输出结果：`old_time=0\n`+`old_time=6\n`+3行`hello world`+1行`Alarm clock`

根据程序执行结果来看，第一设置定时器的超时时间为10秒，定时器开始倒计时（`tv_sec`的值开始递减），程序休眠3秒后，第二次把定时器的超时时间修改为3秒，按理来说，此时上一次定时器的超时时间应该递减为7秒了，参数`old_value`获取上一次的定时器超时时间也是7。但程序打印出来的却是6秒，这是因为程序执行需要消耗时间，所以在获取上一次定时器的超时时间是有损耗的，真实时间应该是6秒多。

最后定时器在3秒后超时，向进程发送了SIGALRM信号。

#### function：getitimer


函数原型：

作用：获取间隔定时器的值

```cpp
int getitimer(int which, struct itimerval *value);
```


