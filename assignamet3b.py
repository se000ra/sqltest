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
import sqlite3

sql = {'average': "SELECT avg(randomnum) FROM randomnum",
       'maximum': "SELECT max(randomnum) FROM randomnum",
       'minimum': "SELECT min(randomnum) FROM randomnum",
       'sum': "SELECT sum(randomnum) FROM randomnum",
       'count': "SELECT count(randomnum) FROM randomnum"}
sql_list = sql.keys()
sql_list.sort()


def get_sql_funk(sql_funk='count'):
    with sqlite3.connect('newnum.db') as connection:
        c = connection.cursor()
        zapros = sql[sql_funk]
        print zapros
        c.execute(zapros)
        return c.fetchone()


class sql_funk_opt(npyscreen.Form):
    def create(self):
        self.sqlFunction = self.add(npyscreen.MultiLine, max_height=5,
                name='sql function',
                #values =['sum', 'maximum'],
                values = sql_list,
                scroll_exit = True
                )

def myFunction(*args):
    F = sql_funk_opt(name='selest sql funk', lines=10, columns=33)
    F.edit()
    user_sql = sql_list[F.sqlFunction.value]
    return get_sql_funk(user_sql)


if __name__ == '__main__':
    print npyscreen.wrapper_basic(myFunction)


