__author__ = 'Frederick NEY & Stephane Overlen'

import requests


def post(url, params):
    return requests.post(url, data=params).json()