


以下部分参考：https://blog.csdn.net/xiamoyanyulrq/article/details/83022632


### 使用安装包安装：


JDK官网下载地址:https://www.oracle.com/java/technologies/jdk8-downloads.html

##### 1）：官方下载对应的.gz包:


这里以jdk-8u181-linux-x64.tar.gz为例


我们可以在Ubantu自带的Firefox浏览器下载，然后保存文件，文件默认在home的下载文件夹中


查看下载后的tar.gz文件

```bash
$ cd ~/下载
```


这里 `~`指的是home目录,`cd ~/下载` 指进入home的下载目录 进入后我们可以使用`ls` 命令查看该目录下的文件

##### 2）：创建一个目录用于存放解压后的文件，并解压缩到该目录下


```bash
$ cd ~/下载
$ sudo mkdir /usr/lib/jvm
$ sudo tar -zxvf jdk-8u181-linux-x64.tar.gz -C /usr/lib/jvm
```


这里`cd ~/下载`是先进入下载文件的所在目录，`sudo mkdir /usr/lib/jvm`指在/usr/lib/下创建一个jvm文件夹,`sudo tar -zxvf jdk-8u181-linux-x64.tar.gz -C /usr/lib/jvm` 指将*.tar.gz文件解压到 /usr/lib/jvm下文件夹下

##### 3）：修改环境变量


```bash
$ sudo vim ~/.bashrc
```


`sudo vim ~/.bashrc`指用文本编辑器vim打开home下的隐藏文件./bashrc，该文件是用户的配置文件。


如果没有下载vim 可以使用 `sudo apt-get install vim`命令来安装vim


##### 4）：文件末尾追加如下内容


```bash
#set oracle jdk environment
export JAVA_HOME=/usr/lib/jvm/jdk1.8.0_181  ## 这里要注意目录要换成自己解压的jdk 目录
export JRE_HOME=${JAVA_HOME}/jre  
export CLASSPATH=.:${JAVA_HOME}/lib:${JRE_HOME}/lib  
PATH=${JAVA_HOME}/bin:$PATH  
```


##### 5）：使环境变量生效


```bash
$ source ~/.bashrc
```


#### 6）：设置默认jdk



注意，下面命令的jdk版本号可能与下载的不同，将下面jdk的版本号改为自己下载的即可。


```bash
$ sudo update-alternatives --install /usr/bin/java java /usr/lib/jvm/jdk1.8.0_181/bin/java 300  
$ sudo update-alternatives --install /usr/bin/javac javac /usr/lib/jvm/jdk1.8.0_181/bin/javac 300  
$ sudo update-alternatives --install /usr/bin/jar jar /usr/lib/jvm/jdk1.8.0_181/bin/jar 300   
$ sudo update-alternatives --install /usr/bin/javah javah /usr/lib/jvm/jdk1.8.0_181/bin/javah 300   
$ sudo update-alternatives --install /usr/bin/javap javap /usr/lib/jvm/jdk1.8.0_181/bin/javap 300 
```


##### 7）：执行


```bash
$ sudo update-alternatives --config java
```


##### 8）：测试是否安装成功


```bash
$ java -version
$ javac -version
```


如果出现bash:***: 没有那个文件或目录，如果环境变量没问题，那就是缺少编译环境。

```bash
$  sudo apt-get install libc6-i386
```


安装编译环境然后再键入`java`命令查看是否安装成功jdk即可。

