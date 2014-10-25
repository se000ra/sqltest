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
    sql = {'average': "SELECT avg(population) FROM population",
           'maximum': "SELECT max(population) FROM population",
           'minimum': "SELECT min(population) FROM population",
           'sum': "SELECT sum(population) FROM population",
           'count': "SELECT count(population) FROM population"}
    for k, v in sql.iteritems():
        c.execute(v)
        result = c.fetchone()
        print k, ":", result[0]
