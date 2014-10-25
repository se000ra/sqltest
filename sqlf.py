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

with sqlite3.connect('new.db') as connection:
    c = connection.cursor()
    c.execute("SELECT firstname, lastname from employees")
    rows = c.fetchall()
    for r in rows:
        print r[0], r[1]
        
