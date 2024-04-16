

### Java中的接口类.


### begin 接口类的简单介绍.


​ 如果一个抽象类中的所有方法都是抽象的，则可以把他定义为接口类。

接口类只能做两个事情：


+  在主函数调用接口类的静态方法或者静态常量. 
+  其他类实现该接口. 
### 1.接口类定义的规则:
 



在JDk8.0往后的版本中，接口类不止可以有抽象方法，还可以有静态方法和默认方法，即下面几种


+ 抽象方法（abstrat）.
+ 静态方法（static）.
+ 默认方法（default）.
+ 静态常量.
+ 不使用class关键词，而使用interface关键词.



甚至可以这么说，接口类不允许有普通方法、普通变量和静态变量.

**接口类不使用class关键词来定义 ，而是使用interface关键词**，下面来演示一下：

```java
import java.util.Arrays;
interface Animal{
   
    public static  String type="Animal";
    default String getType() {
   
        return type;
    }
    public static void noThing() {
   
        System.out.println("I'm nothing.");
    }
    void speak();//普通方法会被自动变成public abstract修饰
}
```


接口的静态方法可以直接用 **类名.方法名 **访问：

```java
public class Kit {
   
	public static void main(String[] arg) {
   
		Animal.noThing();//I'm nothing.
	}
```


#### 


