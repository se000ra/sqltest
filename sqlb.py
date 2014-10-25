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
conn = sqlite3.connect('new.db')
cursor = conn.cursor()
try:
    cursor.execute("INSERT INTO population VALUES('New York City', 'NY', 8200000)")
    cursor.execute("INSERT INTO pppppopulation VALUES('San Francisco', 'CA', 800000)")
    conn.commit()
except sqlite3.OperationalError:
    print "Oops!"
conn.close()
