#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 30 01:06:12 2017

@author: Robert
"""

class MyClass:
    """
    This is a class for testing single and double underscore
    """
    def __init__(self):
        # semi private instance
        self._a = 'Semi private'
        # super private instance, name mangling
        # _MyClass__a
        self.__a = 'Super private'
        
    def _sigle_underscore_method(self):
        print('_sigle_underscore_method')
        
    def __double_underscore_method(slef):
        # Name mangling
        print('_MyClass__double_underscore_method')
        
        
if __name__ == "__main__":
    obj = MyClass()
    print('obj._a=', obj._a)
    try:
        print('obj.__a =', obj.__a) # error
    except AttributeError:
        print('obj.__a induce AttributeError')
    print('(Name mangling) obj._MyClass__a =', obj._MyClass__a)
    
    obj._sigle_underscore_method()
    obj._MyClass__double_underscore_method()