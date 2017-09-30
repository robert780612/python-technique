#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  1 00:04:33 2017

A simple example to implement stack by inheritance

@author: Robert
"""

class Stack(list):
    """
    Inheritance list
    """

    def push(self, x):
        self.insert(0, x)
    
    def popout(self):
        return self.pop(0)
    
if __name__=="__main__":
    a = Stack()
    a.push(3)
    a.push(99)
    print('a:', a)
    x = a.popout()
    print('After pop')
    print('Pop out', x)
    print('a:', a)
    