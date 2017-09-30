#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  1 00:17:46 2017


*In class method overriding
__repr__ goal is to be unambiguous -> for developers
__str__ goal is to be readable -> for customers

if the __str__ is defined, print use the __str__ first.
otherwise print function use __repr__.


*Another good example
>>> repr(1.0 - 0.8)
'0.19999999999999996'
>>> str(1.0 - 0.8)
'0.2'
>>>

Ref:
https://stackoverflow.com/questions/1436703/difference-between-str-and-repr-in-python
http://www.codedata.com.tw/python/python-tutorial-the-2nd-class-1-numeric-types-and-string/

@author: Robert
"""

class Foo1:
    pass

class Foo2:
    """
    Override __repr__
    """
    def __repr__(self):
        return 'Override __repr__'
        
class Foo3:
    """
    Override __str__
    """
    def __str__(self):
        return 'Override __str__'
    
class Foo4:
    """
    Override __repr__ & __str__ at the same time
    """
    def __repr__(self):
        return 'Override __repr__'
    
    def __str__(self):
        return 'Override __str__'
    
    

if __name__=="__main__":
    # No differenct in the Foo1
    a = Foo1()
    print('Foo1')
    print(str(a))
    print(repr(a))
    print(a)
    print('')
    
    # Override __repr__ -> both impacts on str & repr
    b = Foo2()
    print('Foo2')
    print(str(b))
    print(repr(b))
    print(b)
    print('')
    
    # Override __str__ -> only impacts on the str method
    c = Foo3()
    print('Foo3')
    print(str(c))
    print(repr(c))
    print(c)
    print('')
    
    d = Foo4()
    print('Foo4')
    print(str(d))
    print(repr(d))
    print(d)
    
    
    
    
    
    