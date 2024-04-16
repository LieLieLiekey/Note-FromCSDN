

## Java的Set、Map和数组的自定义排序


该文章讲述下面三点并给出相应实例


+ Set的三种自定义排序和遍历
+ Map的三种自定义排序和遍历
+ 数组的三种自定义排序



#### 1.Set的三种自定义排序和遍历


这里的三种自定义排序分别是


+  实现Comparator接口的compare方法并传入构造函数 
+  传入Lambda表达式作为函数接口的参数 
+  以类名::静态方法名作为函数接口的参数 



当然还有常用的第四种方法，让存储元素的类实现Comparabel接口的comparaTo(Object)函数，不过这里不再阐述。

这里的三种遍历集合的方式是

​ 1. 使用**迭代器**遍历set集合

​ 2. 使用forEach函数**用Lambda表达式**实现遍历集合

​ 3. 使用forEach函数用**类名::静态方法名**实现遍历集合

下面以重载String的排序为例，将默认的字典序改为按字符串长度排序。

使用第一种方法自定义排序

```java
package learn;
import java.util.*;
class EachInterface{
   
	static void fuc(String key) {
   
		System.out.println(key);
	}
}
class compare implements Comparator{
    //第一种方式所需的接口实现类
	public int compare(Object _a,Object _b) {
   
		String a=(String)_a;
		String b=(String)_b;
		return a.length()-b.length();
	}
}
public class Learn {
   

	public static void main(String[] args) {
   
		TreeSet<String> mmp=new TreeSet<String>(new compare());//自定义排序的第一种方式
		mmp.add("abccc");
		mmp.add("dch2");
		mmp.add("qwe");
		/*遍历的第一种方式*/
		Iterator it=mmp.iterator();
		while(it.hasNext()) {
   
			System.out.println(it.next());
		}
		System.out.println("===================");
		
		/*遍历的第二种方式*/
		mmp.forEach( (a)->{
   System.out.println(a);}	);
		System.out.println("===================");
		
		/*遍历的第三种方式*/
		mmp.forEach(EachInterface::fuc);
		
	}
	
}

/*
输出：
qwe
dch2
abccc
===================
qwe
dch2
abccc
===================
qwe
dch2
abccc
*/
```



使用第二种方法自定义排序

```java
package learn;
import java.util.*;
public class ```


