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
import random

with sqlite3.connect('newnum.db') as connection:
    c = connection.cursor()
    c.execute("""
    DROP TABLE if exists randomnum
    """)
    c.execute("""
    CREATE TABLE randomnum
    (randomnum INT)
    """)
    #r =[random.randrange(0,101) for i in range(100)]
    for i in range(100):
        c.execute('INSERT INTO randomnum VALUES(?)', (random.randint(0,100),))

    sql = {'average': "SELECT avg(randomnum) FROM randomnum",
           'maximum': "SELECT max(randomnum) FROM randomnum",
           'minimum': "SELECT min(randomnum) FROM randomnum",
           'sum': "SELECT sum(randomnum) FROM randomnum",
           'count': "SELECT count(randomnum) FROM randomnum"}
    for k, v in sql.iteritems():
        c.execute(v)
        result = c.fetchone()
        print k, ":", result[0]
