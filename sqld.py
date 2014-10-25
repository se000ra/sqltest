#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2014 van <van@vanleno>
#
# Distributed under terms of the MIT license.

"""

"""
import sqlite3
import csv

with sqlite3.connect('new.db') as connection:
    c = connection.cursor()
    employees = csv.reader(open("employees.csv", "rU"))
    c.execute("CREATE TABLE employees(firsname TEXT, lastname TEXT)")
    c.executemany('INSERT INTO employees(firsname, lastname) VALUES(?,?)', employees)

