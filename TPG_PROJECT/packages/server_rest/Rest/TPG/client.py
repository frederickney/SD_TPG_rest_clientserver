__author__ = 'Frederick NEY & Stephane Overlen'

from sources import *
import requests
import xml.etree.ElementTree as xmlparser
import itertools


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
        return requests.get(url, param).json()['disruptions']
    elif "xml" == datatype:
        content = requests.get(url, param).text
        xmlparse = xmlparser.fromstring(content)
        return xmlparser.parse(xmlparse)
    else:
        return requests.get(url, param).json()['disruptions']


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
# using line code
# http://prod.ivtr-od.tpg.ch/v1/GetStops?key=hZELIENF7EHRoHL2rY7i&?lineCode=12
def get_stops(request_code = None, request_data = None, datatype = None):
    url = "http://" + TPG_SERVER + "/" + SERVER_VERSION + "/GetStops"
    result = []
    if not None == datatype:
        url = url + "." + datatype
    if not None == request_code and not None == request_data:
        for data in request_data:
            param = {KEY: AUTH_KEY, request_code: data}
            if "json" == datatype:
                content = requests.get(url, param).json()["stops"]
                result .append(content)
            elif "xml" == datatype:
                content = requests.get(url, param).text
                xmlparse = xmlparser.fromstring(content)
                result.append(xmlparser.parse(xmlparse))
            else:
                content = requests.get(url, param).json()["stops"]
                result .append(content)
    else:
        param = {KEY: AUTH_KEY}
        if "json" == datatype:
                content = requests.get(url, param).json()["stops"]
                result .append(content)
        elif "xml" == datatype:
            content = requests.get(url, param).text
            xmlparse = xmlparser.fromstring(content)
            result.append(xmlparser.parse(xmlparse))
        else:
            content = requests.get(url, param).json()["stops"]
            result .append(content)
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
# http://prod.ivtr-od.tpg.ch/v1/GetStops?key=hZELIENF7EHRoHL2rY7i&latitude=46.218176&longitude=6.146445
def get_localisation(latitudes, longitudes, datatype = None):
    url = "http://" + TPG_SERVER + "/" + SERVER_VERSION + "/GetStops"
    result = []
    if not None == datatype:
        url = url + "." + datatype
    for latitude, longitude in itertools.product(latitudes, longitudes):
        param = {KEY: AUTH_KEY, "longitude": longitude, "latitude": latitude}
        if "json" == datatype:
            content = requests.get(url, param).json()["stops"]
            result.append(content)
        elif "xml" == datatype:
            content = requests.get(url, param).text
            xmlparse = xmlparser.fromstring(content)
            result.append(xmlparser.parse(xmlparse))
        else:
            content = requests.get(url, param).json()["stops"]
            result.append(content)
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
            content = requests.get(url, param).json()["stops"]
            result.append(content)
        elif "xml" == datatype:
            content = requests.get(url, param).text
            xmlparse = xmlparser.fromstring(content)
            result.append(xmlparser.parse(xmlparse))
        else:
            content = requests.get(url, param).json()["stops"]
            result.append(content)
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
            content = requests.get(url, param).json()
            del content['timestamp']
            result.append(content)
        elif "xml" == datatype:
            content = requests.get(url, param).text
            xmlparse = xmlparser.fromstring(content)
            result.append(xmlparser.parse(xmlparse))
        else:
            content = requests.get(url, param).json()
            del content['timestamp']
            content["departures"] = remove_timestamp(content["departures"])
            result.append(content)
    return result


"""
@:function  : remove_timestamp
@:brief     : removing timestamp from list
@:param     : list of data
@:return    : list of data
"""


def remove_timestamp(datalist):
    for data in datalist:
        if 'timestamp' in data:
            del data['timestamp']
    return datalist