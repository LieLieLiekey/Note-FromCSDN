

### nth_element() O(n)复杂度求第k+1小元素


##### 函数原型


```cpp
void nth_element(_RAIter, _RAIter, _RAIter);
void nth_element(_RAIter, _RAIter, _RAIter, _Compare);
void nth_element(_RandomAccessIterator __first, _RandomAccessIterator __nth,
		_RandomAccessIterator __last)
void nth_element(_RandomAccessIterator __first, _RandomAccessIterator __nth,
		_RandomAccessIterator __last, _Compare __comp)
```


##### 先看官方的声明



```cpp
void nth_element(_RAIter, _RAIter, _RAIter);
```


/*

@brief Sort a sequence just enough to find a particular position

using a predicate for comparison.

@ingroup sorting_algorithms

@param __first An iterator.

@param __nth Another iterator.

@param __last Another iterator.

@param __comp A comparison functor.

@return Nothing.

Rearranges the elements in the range @p [__first,__last) so that @p *__nth is the same element that would have been in that position had the whole sequence been sorted. The elements either side of @p *__nth are not completely sorted, but for any iterator @e i in the range @p [__first,__nth)


