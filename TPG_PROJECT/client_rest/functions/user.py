__author__ = 'Frederick NEY & Stephane Overlen'


import functions.http_request.post_request as http_post
import functions.client.urlbuilder as urlbuilder

SIGN_IN = "/usr/signIn"
SIGN_OUT = "/usr/signOut"
ADD_USER = "/usr/add"
DEL_USER = "/usr/del"


def sign_in(username, passwd, fqdn, port):
    params = urlbuilder.login_datas(username, passwd)
    url = urlbuilder.set_url(fqdn, SIGN_IN, port)
    request = http_post.post(url, params)
    return request


def sign_out(id, hash, fqdn, port):
    params = urlbuilder.params(id, hash)
    url = urlbuilder.set_url(fqdn, SIGN_OUT, port)
    request = http_post.post(url, params)
    return request


def add_user(username, passwd, fqdn, port):
    params = urlbuilder.login_datas(username, passwd)
    url = urlbuilder.set_url(fqdn, ADD_USER, port)
    request = http_post.post(url, params)
    return request


def del_user(id, hash, fqdn, port):
    params = urlbuilder.params(id, hash)
    url = urlbuilder.set_url(fqdn, DEL_USER, port)
    request = http_post.post(url, params)
    return request