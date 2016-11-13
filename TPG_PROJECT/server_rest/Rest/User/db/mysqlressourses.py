__author__ = 'Frederick NEY & Stephane Overlen'

import pymysql as mysql
import sources


"""
@:function  : mysql_connection
@:brief     : getting connection of the database
"""


def mysql_connection():
    return mysql.connect(sources.MYSQL_USER, sources.MYSQL_PASS, sources.MYSQL_HOST, sources.MYSQL_DB)


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
            if "insert" == type or "delete" == type:
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
