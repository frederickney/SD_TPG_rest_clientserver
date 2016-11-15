__author__ = 'Frederick NEY & Stephane Overlen'

import functions.http_request.get_request as http_get
import functions.client.urlbuilder as urlbuilder

AVAILABLE = "/list/stop/available"
SUBSCRIBED = "/list/stop/subscribed"
SUBSCRIBE = "/list/stop/subscribe"
UN_SUBSCRIBE = "/list/stop/unsubscribe"
NEXT_DEPARTURE = "/list/stop/subscribed/nextDeparture"
NEXT_HANDICAPPED_DEPARTURE = "/list/stop/subscribed/nextDeparture/handicapped"
POSITION = "/list/stop/around500Meter"


def list_available_stop(id, hash, fqdn, port):
    params = urlbuilder.params(id, hash)
    url = urlbuilder.set_url(fqdn, AVAILABLE, port)
    request = http_get.get(url, params)
    return request


def list_stop_subscribed(id, hash, fqdn, port):
    params = urlbuilder.params(id, hash)
    url = urlbuilder.set_url(fqdn, SUBSCRIBED, port)
    request = http_get.get(url, params)
    return request


def get_next_departure(id, hash, fqdn, port, stop, code = None):
    params = urlbuilder.params(id, hash, stop, code)
    url = urlbuilder.set_url(fqdn, NEXT_DEPARTURE, port)
    request = http_get.get(url, params)
    return request


def get_handicapped_next_dearture(id, hash, fqdn, port, stop, code = None):
    params = urlbuilder.params(id, hash, stop, code)
    url = urlbuilder.set_url(fqdn, NEXT_HANDICAPPED_DEPARTURE, port)
    request = http_get.get(url, params)
    return request


def subscribe(id, hash, fqdn, port, stop_code):
    params = urlbuilder.params(id, hash, stop_code)
    url = urlbuilder.set_url(fqdn, SUBSCRIBE, port)
    request = http_get.get(url, params)
    return request


def un_subscribe(id, hash, fqdn, port, stop_code):
    params = urlbuilder.params(id, hash, stop_code)
    url = urlbuilder.set_url(fqdn, UN_SUBSCRIBE, port)
    request = http_get.get(url, params)
    return request


def get_stop_for_position(id, hash, fqdn, port, latitude, longitude):
    params = urlbuilder.params_2_list(id, hash, latitude, longitude)
    url = urlbuilder.set_url(fqdn, POSITION, port)
    request = http_get.get(url, params)
    return request