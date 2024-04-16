

### Java中所有类的父类——非常重要的Object类。

​ 在Java中，所有的基类都有一个默认的父类，那就是Object类。Object类有下面几种方法

```java
boolean equals(Object obj);//判断某个对象与此对象是否相等
final Class<?> getClass()；//返回此Object的运行时类
int hashCode();//返回该对象的哈希码值
String toString();//返回该对象的字符串表示
void finalize();//垃圾回收器调用此方法来清理没有被任何引用变量所引用的资源
Object clone();//返回该对象的克隆
```


​ 在Object类中，这些函数需要我们重写才能达到相应的功能。下面以重载toString函数为例：


我们发现可以直接用System.out.println()输出自己的字符串表示。


```java
package test;
class A {
	int a;
	A(){};
	public String toString() {
		return "This class A of toString function";
	}
}

public class Kit {
	public static void main(String[] arg) {
		A aa = new A();
		System.out.println(aa);//输出 This class A of toString function
	}
}
```


另外Object的equals函数是判断两个对象是否引用的同一个对象，**更确切的说是变量引用的对象内存地址是否为相等，而不是比较他们的内容是否一样** 。
但是我们可以对equals函数进行重载，来达到我们的目的(判断对象的内容是否一样)。


这里需要注意的是’=='也是判断两个对象变量引用的对象是否相同，而不是比较他们的内容（或者你可以理解为对象变量里面存的都是引用对应的地址）


