# traps-in-Python3
collection of encountered traps in Python3  
[**c1**](https://github.com/xiandongli/traps-in-Python3/tree/master/c1)  
函数内部引用外部list/dict/set变量可不用global关键字声明(要小心)  
函数内部引用外部int/str变量必须用global关键字声明  
[**c2**](https://github.com/xiandongli/traps-in-Python3/tree/master/c2)  
Default argument value is evaluated only once.  
This makes a difference when the default is a mutable object such as a list, dictionary, or instances of most classes.

