__author__ = 'Frederick NEY & Stephane Overlen'
import requests


def get(url, params):
    return requests.get(url, params=params).json()