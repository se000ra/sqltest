#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2014 van <van@vanleno>
#
# Distributed under terms of the MIT license.

"""

"""
import npyscreen

class myEmployeeForm(npyscreen.Form):
    def create(self):
        self.myName     = self.add(npyscreen.TitleText, name='Name')
        #self.myDepartment= self.add(npyscreen.TitleText, name='myDepartment')
        self.myDepartment= self.add(npyscreen.TitleSelectOne, max_height=3,
                name='myDepartment',
                values =['dep1', 'dep2', 'dep3','dep4'],
                scroll_exit = True
                )
        self.myDate= self.add(npyscreen.TitleText, name='myDate')

def myFunction(*args):
    #F = npyscreen.Form(name='my test app')
    F = myEmployeeForm(name='new employee')
    F.edit()
    return 'created record for ' + F.myName.value

if __name__ == '__main__':
    print npyscreen.wrapper_basic(myFunction)


