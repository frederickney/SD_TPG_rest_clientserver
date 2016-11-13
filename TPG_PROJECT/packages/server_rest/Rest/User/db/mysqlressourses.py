__author__ = 'Frederick NEY & Stephane Overlen'

import pymysql as mysql
from sources import *


"""
@:function  : mysql_connection
@:brief     : getting connection of the database
"""


def mysql_connection():
    return mysql.connect(MYSQL_USER, MYSQL_PASS, MYSQL_HOST, MYSQL_DB)


"""
@:function  : mysql_query
@:brief     : executing query into database
@:param     : mysql query
"""


def mysql_query(query, type = None):
    try:
        cnx = mysql_connection()
        cursor = cnx.cursor()
        try:
            result = cursor.execute(query)
            if "insert" == type:
                cnx.commit()
            else:
                result = cursor.fetchall()
            cursor.close()
            cnx.close()
        except mysql.Error:
            cnx.rollback()
            cursor.close()
            cnx.close()
            result = -2
    except mysql.Error:
        cnx.close()
        result = -1
    return result
