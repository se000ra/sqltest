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
    
    c.execute("""
            SELECT population.city, population.population, regions.region
            FROM population, regions
            WHERE population.city = regions.city
            ORDER BY population.city ASC
            """)



    rows = c.fetchall()
    for r in rows:
        print r[0], r[1], r[2]
        
