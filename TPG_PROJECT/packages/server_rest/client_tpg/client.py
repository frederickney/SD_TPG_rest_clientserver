__author__ = 'Frederick NEY & Stephane Overlen'

from sources import *
import pymysql as mysql
import requests

import xml.etree.ElementTree as xmlparser


def mysql_connection():
    return mysql.connect(MYSQL_USER, MYSQL_PASS, MYSQL_HOST, MYSQL_DB)


def mysql_query(query):
    cnx = mysql_connection()
    cursor = cnx.cursor()
    result = cursor.execute(query)
    cursor.close()
    cnx.commit()
    cnx.close()
    return result


"""
@:param datatype string
"""


# request example
# http://prod.ivtr-od.tpg.ch/v1/GetDisruptions?key=hZELIENF7EHRoHL2rY7i
def get_distribution(datatype):
    url = "http://" + TPG_SERVER + "/" + SERVER_VERSION + "/GetDisruptions"
    param = {'key': AUTH_KEY}
    if not None == datatype:
        url = url + "." + datatype
    return requests.get(url, param).content


# request example
# ALL
# http://prod.ivtr-od.tpg.ch/v1/GetStops?key=hZELIENF7EHRoHL2rY7i
# using stop code
# http://prod.ivtr-od.tpg.ch/v1/GetStops?key=hZELIENF7EHRoHL2rY7i&stopCode=ACCM
# using stop name
# http://prod.ivtr-od.tpg.ch/v1/GetStops?key=hZELIENF7EHRoHL2rY7i&stopName=gare cornavin
# using latitude and longitude
# http://prod.ivtr-od.tpg.ch/v1/GetStops?key=hZELIENF7EHRoHL2rY7i&GetStops?latitude=46.218176&longitude=6.146445
# using line code
# http://prod.ivtr-od.tpg.ch/v1/GetStops?key=hZELIENF7EHRoHL2rY7i&GetStops?lineCode=12
def get_stops(datatype, request_code, request_data):
    url = "http://" + TPG_SERVER + "/" + SERVER_VERSION + "/GetDisruptions"
    result = []
    if not None == datatype:
        url = url + "." + datatype
    for data in request_data:
        param = {'key': AUTH_KEY, request_code: data}
        result .append(requests.get(url, param).content)
    return result


# using stop code
# http://prod.ivtr-od.tpg.ch/v1/GetPhysicalStops?key=hZELIENF7EHRoHL2rY7i&stopCode=ACCM
# using stop name
# http://prod.ivtr-od.tpg.ch/v1/GetPhysicalStops?key=hZELIENF7EHRoHL2rY7i&stopName=gare cornavin
def get_physical_stops(datatype, request_code, request_data):
    url = "http://" + TPG_SERVER + "/" + SERVER_VERSION + "/GetDisruptions"
    result = []
    if not None == datatype:
        url = url + "." + datatype
    for data in request_data:
        param = {'key': AUTH_KEY, request_code: data}
        result .append(requests.get(url, param).content)
    return result


# request example
# using departure code
# http://prod.ivtr-od.tpg.ch/v1/GetNextDepartures?key=hZELIENF7EHRoHL2rY7i&departureCode=22936
# using line code
# http://prod.ivtr-od.tpg.ch/v1/GetNextDepartures?key=hZELIENF7EHRoHL2rY7i&lineCode=12
# using destination code
# http://prod.ivtr-od.tpg.ch/v1/GetNextDepartures?key=hZELIENF7EHRoHL2rY7i&destinationCode=BOURG D'EN HAUT
# using stop code
# http://prod.ivtr-od.tpg.ch/v1/GetNextDepartures?key=hZELIENF7EHRoHL2rY7i&stopCode=ACCM
def get_next_departure(datatype, request_code, request_data):
    url = "http://" + TPG_SERVER + "/" + SERVER_VERSION + "/GetDisruptions"
    result = []
    if not None == datatype:
        url = url + "." + datatype
    for data in request_data:
        param = {'key': AUTH_KEY, request_code: data}
        result .append(requests.get(url, param).content)
    return result
