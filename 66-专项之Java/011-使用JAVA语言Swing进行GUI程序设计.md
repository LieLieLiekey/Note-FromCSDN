

## 使用JAVA语言Swing进行GUI程序设计


在扫雷S项目的GUI设计中主要遇到了一下问题并且解决。


+ 怎么在JDIalog对象中添加组件
+ 怎么自定义容器中组件的位置和大小
+ 在设定了布局管理器的容器中怎么控制某一块的高度或者宽度
+ 怎么返回一个指定大小的ImageIcon对象
+ 怎么给按钮设置三种（四种状态的Icon）
+ 怎么给窗口设置半透明




注：大多数查找API文档和从网络论坛中查找较为方便


#### 1.怎么在JDIalog对象中添加组件


向对话框JDialog对象中组件只能通过添加一个JPanel，在JPanel中添加组件即可。


参考博客：[https://blog.csdn.net/xietansheng/article/details/75948933](https://blog.csdn.net/xietansheng/article/details/75948933)


```java
JFrame jf=new JFrame();
jf.setSize(1200,960);		
jf.setDefaultCloseOperation(JFrame.HIDE_ON_CLOSE);
JDialog dialog=new JDialog(jf);
dialog.setContentPane(contentPanel);
dialog.setVisible(true)
```



#### 2.怎么自定义容器中组件的位置和大小


如果一个容器使用的布局管理器为null，那么可以使用组件的setBounds(x,y,width,height)函数可以设置组件在容器中的位置

```java
JFrame jf=new JFrame();```


