#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

This is borrow from https://advancedpythonprogramming.github.io/Book_Chapters/Chapter_1_OOP.pdf

Created on Sat Sep 30 01:27:36 2017

@author: Robert
"""

#%% First way: use the property()
class Email:
    """
    User property(getter, setter, deleter) to set a property
    Email.email calls the getter
    Email.email = 'Something' calls the setter
    del Email.email calls the deleter
    """
    
    def __init__(self, address):
        self._email = address
    
    def _set_email(self, value):
        if '@' not in value:
            print('This is not an email address')
        else:
            self._email = value
    
    def _get_email(self):
        return self._email
    
    def _del_email(self):
        print('Erase this email address')
        del self._email
        
    # a public property "email"
    # getter, setter, deleter
    email = property(_get_email, _set_email, _del_email,
                     'Email operation')
    
#%% Second way: use the decorator
class Email2:
    """
    Use @property to set a property
    Note: getter & setter & deleter's names equal to property's name
    """
    
    def __init__(self, address):
        self._email = address
    
    # a property "email"
    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, value):
        if '@' not in value:
            print('This is not an email address')
        else:
            self._email = value
    
    @email.getter
    def email(self):
        return self._email
    
    @email.deleter
    def email(self):
        print('Erase this email address')
        del self._email
    

if __name__=="__main__":
    #%% Test the first class
    m = Email('m1@gmail.com')
    print(m.email)
    

    print('')
    print('Warning by the setter!!')
    # Call the setter
    m.email = 'Use setter'
    
    print('')
    m.email = 'normal@email'
    print('Normal email address: ', m.email)

    print('')
    del m.email
    try:
        print(m.email) # error no attribute _email
    except AttributeError:
        print('No attribute _email')
    
    #%% Test the second class
    print('\n\n\nClass2')
    m2 = Email2('m1@gmail.com')
    print(m2.email)
    

    print('')
    print('Warning by the setter!!')
    # Call the setter
    m2.email = 'Use setter'
    
    print('')
    m2.email = 'normal@email'
    print('Normal email address: ', m2.email)

    print('')
    del m2.email
    try:
        print(m2.email) # error no attribute _email
    except AttributeError:
        print('No attribute _email')
    
    
    
    
    
    
    
    