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

cities = [
    ('New York City', 'Northeast'),
    ('San Francisco', 'West'),
    ('Chicago', 'Midwest'),
    ('Houston', 'South'),
    ('Phoenix', 'West'),
    ('Boston', 'Northeast'),
    ('Los Angeles', 'West'),
    ('Houston', 'South'),
    ('Philadelphia', 'Northeast'),
    ('San Antonio', 'South'),
    ('San Diego', 'West'),
    ('Dallas', 'South'),
    ('San Jose', 'West'),
    ('Jacksonville', 'South'),
    ('Indianapolis', 'Midwest'),
    ('Austin', 'South'),
    ('Detroit', 'Midwest')
    ]

with sqlite3.connect('new.db') as connection:
    c = connection.cursor()
    c.execute("""
            CREATE TABLE regions
            (city TEXT, region TEXT)
            """)



    c.executemany("INSERT INTO regions VALUES(?,?)", cities)

    c.execute("SELECT * FROM regions ORDER BY region ASC")
    rows = c.fetchall()
    for r in rows:
        print r[0], r[1]
        
