# 使用JAVA语言Swing进行GUI程序设计

在扫雷S项目的GUI设计中主要遇到了一下问题并且解决。

1. 怎么在JDIalog对象中添加组件
2. 怎么自定义容器中组件的位置和大小
3. 在设定了布局管理器的容器中怎么控制某一块的高度或者宽度
4. 怎么返回一个指定大小的ImageIcon对象
5. 怎么给按钮设置三种（四种状态的Icon）
6. 怎么给窗口设置半透明

> 注：大多数查找API文档和从网络论坛中查找较为方便

### 1.怎么在JDIalog对象中添加组件

向对话框JDialog对象中组件只能通过添加一个JPanel，在JPanel中添加组件即可。

> 参考博客：<https://blog.csdn.net/xietansheng/article/details/75948933>

```java
JFrame jf=new JFrame();
jf.setSize(1200,960);		
jf.setDefaultCloseOperation(JFrame.HIDE_ON_CLOSE);
JDialog dialog=new JDialog(jf);
dialog.setContentPane(contentPanel);
dialog.setVisible(true)
```



-------

### 2.怎么自定义容器中组件的位置和大小

如果一个容器使用的布局管理器为null，那么可以使用组件的setBounds(x,y,width,height)函数可以设置组件在容器中的位置

```java
JFrame jf=new JFrame();//
jf.setLayout(null);
jf.setSize(1200,960);		jf.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
jf.setResizable(false);
jf.setLocation(343, 36); 
		//设置没有装饰
jf.setUndecorated(true);
//		jf.setBackground(new Color(0,255,0));
//设置透明度
jf.setOpacity(0.95f);
jf.add(component);//向之中添加组件。要求组件使用setBounds来指定位置
jf.setVisible(true);
```



-----

### 3.在设定了布局管理器的容器中怎么控制某一块的高度或者宽度

如果在一个容器中使用了布局管理器，但是还想要控制组件的某一个属性，比如使用BorderLayout布局管理器，却想要控制north或者center的组件的高度等等，那么可以使用组件的setPreferredSize(preferredSize)函数，参数是一个宽度和高度的对象，该函数的作用是如果某一值为0则表示该方向适应布局管理器，否则按照自己的大小进行设置

> 参考博客：<https://codeday.me/bug/20170621/28652.html>

```java
JPanel panel=new JPanel();
panel.setPreferredSize(new Dimension(0,250));//panel在JFrame中的BorderLayout布局管理器中的NORTH位置，这样设置会使得该面板的高度为250像素，宽度自适应Layout(这个例子中是宽度为整个Panel的宽度)
```



-----

### 4.返回一个指定大小的ImageIcon对象

我们可以先创建一个‘’指定图片路径‘’的ImageIcon对象，然后获取其中的image对象后使用image对象的img.getScaledInstance(width, height, hints)，获取一个指定大小的相同图像的对象(这两个对象不为同一个对象)，然后用ImageIcon的setImage函数设定图像图像即可。

```java
 public ImageIcon getSpcImageIcon(String filename,int d)
{
		ImageIcon icon=new ImageIcon(filename);
		Image img=icon.getImage();
		img=img.getScaledInstance(d, d, Image.SCALE_DEFAULT);
		icon.setImage(img);
		return icon;
}
```



---

### 5.怎么给按钮设置三种（四种状态的Icon）

按钮主要的状态由三种：正常状态（general），点击中状态(press) ，鼠标放在上面的状态(roll over)。分别可以用setIcon(defaultIcon)，setPressedIcon(pressedIcon)，setRolloverIcon(rolloverIcon)实现。

```java
public ImageIcon getSpcImageIcon(String filename,int d)
{//返回一个d*d大小，图片路径在filename的ImageIcon对象
		ImageIcon icon=new ImageIcon(filename);
		Image img=icon.getImage();
		img=img.getScaledInstance(d, d, Image.SCALE_DEFAULT);
		icon.setImage(img);
		return icon;
}
public JButton setButtonImage(JButton button,int d,String s1,String s2,String s3) {
		//指定button一个默认图片，Press图片，onMouse图片，
		button.setIcon(getSpcImageIcon(s1,d));
		button.setPressedIcon(getSpcImageIcon(s2,d));
		button.setRolloverIcon(getSpcImageIcon(s3,d));
//		button.setOpaque(false);
		return button;
	}
```



但是有时候给button使用setEnable函数设置失效，此时按钮就会变灰色，我们只要使用button的setDisabledIcon(ImageIcon)函数设置失效后的Icon即可.



---

### 6.怎么给窗口设置半透明

jdk1.7提供了，setOpacity(float f);方法 。 即可将frame设置呈透明。但是默认情况下容器中的所有组件也都变为半透明

> 参考博客:<https://blog.csdn.net/JavaBuilt/article/details/79897042>

```java
JFrame jf=new JFrame();
jf.setOpacity(0.95f);
```
