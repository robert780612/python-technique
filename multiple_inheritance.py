#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  1 00:50:06 2017

Important concept!!
MRO (method resolution order)
super() -> find the "next" class in the MRO


Ref:
https://advancedpythonprogramming.github.io/Book_Chapters/Chapter_1_OOP.pdf
https://mozillazg.github.io/2016/12/python-super-is-not-as-simple-as-you-thought.html
https://www.zhihu.com/question/20040039

@author: Robert
"""

#%%
print('Example 1')
class Researcher:

    def __init__(self, field, **kwargs):
        # not necessary, next class in the MRO is "object"
        # but suggest uncomment following line to execute object.__init__
        # avoid potential mistake
#        super().__init__(**kwargs) 
        self.field = field

    def __str__(self):
        return "Research field: " + self.field + "\n"


class Teacher:

    def __init__(self, courses_list, **kwargs):
        # super() find the next class in the "MRO"
        # important!! next class in the MRO is "Researcher"!!!!!!!!
        # if we comment this line, it will raise AttributeError "no attribute field"
        # because python didn't execute Researcher.__init__ method
        super().__init__(**kwargs) 
        self.courses_list = courses_list

    def __str__(self):
        out = "Courses: "
        for c in self.courses_list:
            out += c + ", "
        # the [:-2] selects all the elements
        # but the last two
        return out[:-2] + "\n"


class Professor(Teacher, Researcher):

    def __init__(self, name, **kwargs):
        super().__init__(**kwargs)
        self.name = name

    def __str__(self):
        out = Researcher.__str__(self)
        out += Teacher.__str__(self)
#        out = super().__str__() # do not work, it won't call Researcher.__str__
        out += "Name: " + self.name + "\n"
        return out


p = Professor(name="Steve Iams",
              field="Meachine Learning",
              courses_list=[
                "Python Programming",
                "Probabilistic Graphical Models",
                "Bayesian Inference"
              ])

print(p)
for x in Professor.mro(): # method resolution order
    print(x)
    
    
    
#%% Example 2
print('')
print('Example 2')
class A:
    def __init__(self):
        self.n = 2

    def add(self, m):
        # 第四步
        # 来自 D.add 中的 super
        # self == d, self.n == d.n == 5
        print('self is {0} @A.add'.format(self))
        print('in A', self.n)
        self.n += m
        print('in A', self.n)
        # d.n == 7


class B(A):
    def __init__(self):
        self.n = 3

    def add(self, m):
        # 第二步
        # 来自 D.add 中的 super
        # self == d, self.n == d.n == 5
        print('self is {0} @B.add'.format(self))
        print('in B', self.n)
        # 等价于 suepr(B, self).add(m)
        # self 的 MRO 是 [D, B, C, A, object]
        # 从 B 之后的 [C, A, object] 中查找 add 方法
        super().add(m)
        # 第六步
        # d.n = 11
        self.n += 3
        print('in B', self.n)
        # d.n = 14

class C(A):
    def __init__(self):
        self.n = 4

    def add(self, m):
        # 第三步
        # 来自 B.add 中的 super
        # self == d, self.n == d.n == 5
        print('self is {0} @C.add'.format(self))
        print('in C', self.n)
        # 等价于 suepr(C, self).add(m)
        # self 的 MRO 是 [D, B, C, A, object]
        # 从 C 之后的 [A, object] 中查找 add 方法
        super().add(m)

        # 第五步
        # d.n = 7
        self.n += 4
        print('in C', self.n)
        # d.n = 11


class D(B, C):
    def __init__(self):
        self.n = 5

    def add(self, m):
        # 第一步
        print('self is {0} @D.add'.format(self))
        print('in D', self.n)
        # 等价于 super(D, self).add(m)
        # self 的 MRO 是 [D, B, C, A, object]
        # 从 D 之后的 [B, C, A, object] 中查找 add 方法
        super().add(m)

        # 第七步
        # d.n = 14
        self.n += 5
        print('in D', self.n)
        # self.n = 19

d = D()
d.add(2)
print(d.n)
    