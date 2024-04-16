

## xpath语法


#### 前言：


处理规则数据例如json类数据就就需json模块提取

处理不规则数据例如html代码的数据一般使用正则表达式或者lxml提取。

而lxml模块需要了解xpath语法，故xpath语法及其重要

#### Xpath的节点和语法以及基本使用请参考W3school：[http://www.w3school.com.cn/xpath/xpath_syntax.asp](http://www.w3school.com.cn/xpath/xpath_syntax.asp)


#### 1.什么是xpath


XPath (XML Path Language) 是一门在 HTML\XML 文档中查找信息的**语言**，可用来在 HTML\XML 文档中对**元素和属性进行遍历**。

#### ​2.认识xmL


```
<bookstore>
<book category="COOKING">
  <title lang="en">Everyday Italian</title> 
  <author>Giada De Laurentiis</author> 
  <year>2005</year> 
  <price>30.00</price> 
</book>
<book category="CHILDREN">
  <title lang="en">Harry Potter</title> 
  <author>J K. Rowling</author> 
  <year>2005</year> 
  <price>29.99</price> 
</book>
<book category="WEB">
  <title lang="en">Learning XML</title> 
  <author>Erik T. Ray</author> 
  <year>2003</year> 
  <price>39.95</price> 
</book>
</bookstore>
```


### 3.下面引用W3school中对于xpath的语法，已经是非常常用的！


#### 下面列出了最有用的路径表达式：

表达式描述nodename选取此节点的所有子节点。/从根节点选取。//从匹配选择的当前节点选择文档中的节点，而不考虑它们的位置。.选取当前节点。…选取当前节点的父节点。@选取属性。

#### 实例


在下面的表格中，我们已列出了一些路径表达式以及表达式的结果：
路径表达式结果bookstore选取 bookstore 元素的所有子节点。/bookstore选取根元素 bookstore。注释：假如路径起始于正斜杠( / )，则此路径始终代表到某元素的绝对路径！bookstore/book选取属于 bookstore 的子元素的所有 book 元素。//book选取所有 book 子元素，而不管它们在文档中的位置。bookstore//book选择属于 bookstore 元素的后代的所有 book 元素，而不管它们位于 bookstore 之下的什么位置。//@lang选取名为 lang 的所有属性。

### 谓语（Predicates）


谓语用来查找某个特定的节点或者包含某个指定的值的节点。

谓语被嵌在方括号中。

#### 实例


在下面的表格中，我们列出了带有谓语的一些路径表达式，以及表达式的结果：
路径表达式结果/bookstore/book[1]选取属于 bookstore 子元素的第一个 book 元素。/bookstore/book[last()]选取属于 bookstore 子元素的最后一个 book 元素。/bookstore/book[last()-1]选取属于 bookstore 子元素的倒数第二个 book 元素。/bookstore/book[position()❤️]选取最前面的两个属于 bookstore 元素的子元素的 book 元素。//title[@lang]选取所有拥有名为 lang 的属性的 title 元素。//title[@lang=‘eng’]选取所有 title 元素，且这些元素拥有值为 eng 的 lang 属性。/bookstore/book[price>35.00]选取 bookstore 元素的所有 book 元素，且其中的 price 元素的值须大于 35.00。/bookstore/book[price>35.00]/title选取 bookstore 元素中的 book 元素的所有 title 元素，且其中的 price 元素的值须大于 35.00。

### 选取未知节点


XPath 通配符可用来选取未知的 XML 元素。
通配符描述*匹配任何元素节点。@*匹配任何属性节点。node()匹配任何类型的节点。

#### 实例


在下面的表格中，我们列出了一些路径表达式，以及这些表达式的结果：
路径表达式结果/bookstore/*选取 bookstore 元素的所有子元素。//*选取文档中的所有元素。//title[@*]选取所有带有属性的 title 元素。

### 选取若干路径


通过在路径表达式中使用“|”运算符，您可以选取若干个路径。

#### 实例


在下面的表格中，我们列出了一些路径表达式，以及这些表达式的结果：
路径表达式结果//book/title | //book/price选取 book 元素的所有 title 和 price 元素。//title | //price选取文档中的所有 title 和 price 元素。/bookstore/book/title | //price选取属于 bookstore 元素的 book 元素的所有 title 元素，以及文档中所有的 price 元素。

##### 


##### 对于Python中xpath的使用请看下一章：


