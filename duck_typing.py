#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  1 02:13:56 2017

Duck typing
If it walks like a duck and quacks like a duck, then it is a duck.

@author: Robert
"""

class Duck:
    
    def scream(self):
        print('quack')
    
    def walk(self):
        print('duck walk')
        
class Person:
    
    def scream(self):
        print('ohoh')
        
    def walk(self):
        print('human walk')
        
def action(duck):
    duck.scream()
    duck.walk()

if __name__=="__main__":
    a = Duck()
    b = Person()
    action(a)
    action(b)