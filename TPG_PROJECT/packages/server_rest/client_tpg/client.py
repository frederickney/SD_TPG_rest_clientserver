__author__ = 'Frederick NEY & Stephane Overlen'

from sources import *
import pymysql as mysql
import requests
import xml.etree.ElementTree as xmlparser
import itertools


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


def mysql_query(query):
    cnx = mysql_connection()
    cursor = cnx.cursor()
    result = cursor.execute(query)
    cursor.close()
    cnx.commit()
    cnx.close()
    return result


"""
@:function  : get_disruptions
@:brief     : getting disruptions of lines from tpg server
@:param     : xml or json data type (optional)
"""


# request example
# http://prod.ivtr-od.tpg.ch/v1/GetDisruptions?key=hZELIENF7EHRoHL2rY7i
def get_disruptions(datatype = None):
    url = "http://" + TPG_SERVER + "/" + SERVER_VERSION + "/GetDisruptions"
    param = {KEY: AUTH_KEY}
    if not None == datatype:
        url = url + "." + datatype
    if "json" == datatype:
        return requests.get(url, param).json()
    elif "xml" == datatype:
        root = xmlparser.fromstring(requests.get(url, param).content)
        return xmlparser.tostring(root, encoding='utf8', method='xml')
    else:
        return requests.get(url, param).json()


"""
@:function  : get_stops
@:brief     : getting list of stops or list of specifics stop or only one stop
@:param     : request_code = stopCode or stopName or lineCode (optional)
@:param     : request_data = list of data corresponding to request_code type (optional)
@:param     : datatype = xml or json data type (optional)
"""


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
def get_stops(request_code = None, request_data = None, datatype = None):
    url = "http://" + TPG_SERVER + "/" + SERVER_VERSION + "/GetStops"
    result = []
    if not None == datatype:
        url = url + "." + datatype
    if not None == request_code and not None == request_data:
        for data in request_data:
            param = {KEY: AUTH_KEY, request_code: data}
            if "json" == datatype:
                result .append(requests.get(url, param).json())
            elif "xml" == datatype:
                root = xmlparser.fromstring(requests.get(url, param).content)
                result.append(xmlparser.tostring(root, encoding='utf8', method='xml'))
            else:
                result .append(requests.get(url, param).json())
    else:
        param = {KEY: AUTH_KEY}
        if "json" == datatype:
                result .append(requests.get(url, param).json())
        elif "xml" == datatype:
            root = xmlparser.fromstring(requests.get(url, param).content)
            result.append(xmlparser.tostring(root, encoding='utf8', method='xml'))
        else:
            result .append(requests.get(url, param).json())
    return result


"""
@:function  : get_localisation
@:brief     : getting stops into a range of 500 meters
@:param     : latitudes = list of latitude (required)
@:param     : longitudes = list of longitude (required)
@:param     : datatype = xml or json data type (optional)
"""


# request example
# using latitude and longitude
# http://prod.ivtr-od.tpg.ch/v1/GetStops?key=hZELIENF7EHRoHL2rY7i&GetStops?latitude=46.218176&longitude=6.146445
def get_localisation(latitudes, longitudes, datatype = None):
    url = "http://" + TPG_SERVER + "/" + SERVER_VERSION + "/GetStops"
    result = []
    if not None == datatype:
        url = url + "." + datatype
    for latitude, longitude in itertools.product(latitudes, longitudes):
        param = {KEY: AUTH_KEY, "longitude": longitude, "latitude": latitude}
        if "json" == datatype:
            result .append(requests.get(url, param).json())
        elif "xml" == datatype:
            root = xmlparser.fromstring(requests.get(url, param).content)
            result.append(xmlparser.tostring(root, encoding='utf8', method='xml'))
        else:
            result .append(requests.get(url, param).json())
    return result


"""
@:function  : get_physical_stops
@:brief     : getting all data for specifics stop or list of stop
@:param     : request_code = stopCode or stopName (required)
@:param     : request_data = list of data corresponding to request_code type (required)
@:param     : datatype = xml or json data type (optional)
"""


# using stop code
# http://prod.ivtr-od.tpg.ch/v1/GetPhysicalStops?key=hZELIENF7EHRoHL2rY7i&stopCode=ACCM
# using stop name
# http://prod.ivtr-od.tpg.ch/v1/GetPhysicalStops?key=hZELIENF7EHRoHL2rY7i&stopName=gare cornavin
def get_physical_stops(request_code, request_data, datatype = None,):
    url = "http://" + TPG_SERVER + "/" + SERVER_VERSION + "/GetPhysicalStops"
    result = []
    if not None == datatype:
        url = url + "." + datatype
    for data in request_data:
        param = {KEY: AUTH_KEY, request_code: data}
        if "json" == datatype:
            result .append(requests.get(url, param).json())
        elif "xml" == datatype:
            root = xmlparser.fromstring(requests.get(url, param).content)
            result.append(xmlparser.tostring(root, encoding='utf8', method='xml'))
        else:
            result .append(requests.get(url, param).json())
    return result


"""
@:function  : get_next_departure
@:brief     : getting next departure(s) for a single or list of stop, bus or destination
@:param     : request_code = stopCode or destinationCode or lineCode or departureCode (required)
@:param     : request_data = list of data corresponding to request_code type (required)
@:param     : datatype = xml or json data type (optional)
"""


# request example
# using departure code
# http://prod.ivtr-od.tpg.ch/v1/GetNextDepartures?key=hZELIENF7EHRoHL2rY7i&departureCode=22936
# using line code
# http://prod.ivtr-od.tpg.ch/v1/GetNextDepartures?key=hZELIENF7EHRoHL2rY7i&lineCode=12
# using destination code
# http://prod.ivtr-od.tpg.ch/v1/GetNextDepartures?key=hZELIENF7EHRoHL2rY7i&destinationCode=BOURG D'EN HAUT
# using stop code
# http://prod.ivtr-od.tpg.ch/v1/GetNextDepartures?key=hZELIENF7EHRoHL2rY7i&stopCode=ACCM
def get_next_departure(request_code, request_data, datatype = None):
    url = "http://" + TPG_SERVER + "/" + SERVER_VERSION + "/GetNextDepartures"
    result = []
    if not None == datatype:
        url = url + "." + datatype
    for data in request_data:
        param = {KEY: AUTH_KEY, request_code: data}
        if "json" == datatype:
            result .append(requests.get(url, param).json())
        elif "xml" == datatype:
            root = xmlparser.fromstring(requests.get(url, param).content)
            result.append(xmlparser.tostring(root, encoding='utf8', method='xml'))
        else:
            result .append(requests.get(url, param).json())
    return result
