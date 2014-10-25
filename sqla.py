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
cursor.execute("""CREATE TABLE population
(city TEXT, state TEXT, population INT)
""")
conn.close()
