__author__ = 'Frederick NEY & Stephane Overlen'


def set_url(fqdn, request_link, port = 80):
    url = "http://%s:%i%s"
    return url % (fqdn, port, request_link)


def login_datas(username, passwd):
    return {"username": username, "passwd": passwd}


def params(id, hash, list = None, code = None):
    if None == list and None == code:
        params = {"id": id, "hash": hash}
    elif None == code and not None == list:
        params = {"id": id, "hash": hash, "stopCode": list}
    elif not None == list and not None == code:
        params = {"id": id, "hash": hash, "stopCode": list, "code": code}
    return params


def params_2_list(id, hash, list, list2):
    return {"id": id, "hash": hash, "longitude": list2, "latitude": list}