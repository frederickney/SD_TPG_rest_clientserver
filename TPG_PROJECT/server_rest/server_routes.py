__author__ = 'Frederick NEY & Stephane Overlen'

import re
import argparse

from flask import Flask, request, jsonify

import Rest.User.user as user
import Rest.TPG.client as client
import Rest.User.db.mysqlressourses as mysql

app = Flask(__name__)
main_directory = None


def parse_datatype(datatype):
    if not None == datatype:
        datatype = re.sub('\.+', '.', datatype)
    return datatype


"""------------------------------------------------------------------------------------------------------------------"""
"""+----------------------------------------------------------------------------------------------------------------+"""
"""|                                              GET METHOD                                                        |"""
"""+----------------------------------------------------------------------------------------------------------------+"""
"""------------------------------------------------------------------------------------------------------------------"""


"""
@api {get} /stop/available?id=&hash= list_available_stop()

@apiName list_available_stop
@apiGroup TPG

@apiParam   {id = integer} id of the user
@apiParam   {hash = string} hash code of the cookie

@apiSuccess {list of string} list of available stop
"""


@app.route('/list/stop/available', defaults={'datatype': None}, methods=['GET'])
@app.route('/list/stop/available<path:datatype>', methods=['GET'])
def list_available_stop(datatype):
    id = request.args.get('id')
    hash = request.args.get('hash')
    if None == hash and None == id:
        return jsonify(error="Bad request.")
    id = int(id)
    print(id)
    print(hash)
    if 1 == user.auth_cookie(id, hash):
        return jsonify(stop_available=client.get_stops())
    return jsonify(error="Bad request.")


"""
@api {get} /list/stop/subscribed?id=&hash= list_stop_subscribed()

@apiName list_stop_subscribed
@apiGroup TPG

@apiParam   {id = integer} id of the user
@apiParam   {hash = string} hash code of the cookie

@apiSuccess {list of string} list of stop
"""


@app.route('/list/stop/subscribed', methods=['GET'], defaults={'datatype': None})
@app.route('/list/stop/subscribed<path:datatype>', methods=['GET'])
def list_stop_subscribed(datatype):
    id = request.args.get('id')
    hash = request.args.get('hash')
    if None == hash and None == id:
        return jsonify(error="Bad request.")
    id = int(id)
    if 1 == user.auth_cookie(id, hash):
        query = "Select * from subscriptions where user_id = %i"
        results = mysql.mysql_query(query % id)
        stop_code = []
        for result in results:
            stop_code.append(result["stop_id"])
        return jsonify(stop_subscribed=client.get_stops("stopCode", stop_code))
    return jsonify(error="Bad request.")

"""
@api {get} /list/stop/subscribed/nextDeparture?id=&hash=&stopName&code= list_next_departure()

@apiName list_next_departure
@apiGroup TPG

@apiParam   {id = integer} id of the user
@apiParam   {hash = string} hash code of the cookie
@apiParam   {stopName = list of string}  list of stop
@apiParam   {code = string} optional should be stopName or stopCode

@apiSuccess {list of string} List of departure
"""


@app.route('/list/stop/subscribed/nextDeparture', methods=['GET'], defaults={'datatype': None})
@app.route('/list/stop/subscribed/nextDeparture<path:datatype>', methods=['GET'])
def list_next_departure(datatype):
    id = request.args.get('id')
    hash = request.args.get('hash')
    stop_name = request.args.getlist('stopName')
    request_code = request.args.get('code')
    if None == request_code:
        request_code = "stopName"
    if None == hash and None == id and None == stop_name:
        return jsonify(error="Bad request.")
    id = int(id)
    if 1 == user.auth_cookie(id, hash):
        return jsonify(next_departure=client.get_next_departure(request_code, stop_name))
    return jsonify(error="Bad request.")


"""
@api {get} /list/stop/subscribe?id=&hash=&stopName= subscribe()

@apiName subscribe
@apiGroup TPG

@apiParam   {id = integer} id of the user
@apiParam   {hash = string} hash code of the cookie
@apiParam   {stopName = list of string}  list of stop
@apiParam   {code = string} optional should be stopName or stopCode

@apiSuccess {string} error code
"""


@app.route('/list/stop/subscribe', methods=['GET'])
def subscribe():
    id = request.args.get('id')
    hash = request.args.get('hash')
    stop_name = request.args.getlist('stopCode')
    request_code = request.args.get('code')
    if None == request_code:
        request_code = "stopName"
    if None == hash and None == id:
        return jsonify(error="Bad request.")
    id = int(id)
    if 1 == user.auth_cookie(id, hash):
        query = "insert into subscriptions (stop_id, user_id) values ('%s', %i);"
        for stop in stop_name:
            mysql.mysql_query(query % (stop, id), "insert")
        return jsonify(error="Success.")
    return jsonify(error="Bad request.")


"""
@api {get} /list/stop/unsubscribe?stopName=&id=&hash= un_subscribe()

@apiName un_subscribe
@apiGroup TPG

@apiParam   {stopName = list of string}  list of stop name
@apiParam   {id = integer} id of the user
@apiParam   {hash = string} hash code of the cookie
@apiParam   {stopName = list of string}  list of stop
@apiParam   {code = string} optional should be stopName or stopCode

@apiSuccess {string} error code
"""


@app.route('/list/stop/unsubscribe', methods=['GET'])
def un_subscribe():
    id = request.args.get('id')
    hash = request.args.get('hash')
    request_code = request.args.get('code')
    stop_name = request.args.getlist('stopCode')
    if None == request_code:
        stop_name = request.args.getlist('stopCode')
    if None == hash and None == id:
        return jsonify(error="Bad request.")
    id = int(id)
    if 1 == user.auth_cookie(id, hash):
        query = "delete from subscriptions where stop_id = %s;"
        for stop in stop_name:
            mysql.mysql_query(query % stop, "delete")
        return jsonify(error="Success.")
    return jsonify(error="Bad request.")


"""
@api {get} /list/stop/around500Meter?id=&hash=&latitude=&longitude= get_stop_localisation()

@apiName get_stop_localisation
@apiGroup TPG

@apiParam   {id = integer} id of the user
@apiParam   {hash = string} hash code of the cookie
@apiParam   {latitude = list of float} list of latitude
@apiParam   {longitude = list of float} list of longitude

@apiSuccess {list of string} list of stops around 500 meters for a location
"""


@app.route('/list/stop/around500Meter', methods=['GET'], defaults={'datatype': None})
@app.route('/list/stop/around500Meter<path:datatype>', methods=['GET'])
def get_stop_localisation(datatype):
    id = request.args.get('id')
    hash = request.args.get('hash')
    longitude = request.args.getlist('longitude')
    latitude = request.args.getlist('latitude')
    if None == hash and None == id and None == latitude and None == longitude:
        return jsonify(error="Bad request.")
    id = int(id)
    if 1 == user.auth_cookie(id, hash):
        return jsonify(locations=client.get_localisation(latitude, longitude))
    return jsonify(error="Bad request.")


"""
@api {get} /list/stop/subscribed/nextDeparture/handicaped?id=&hash=&stopName= list_next_departure_for_handicaped()

@apiName list_next_departure_for_handicaped
@apiGroup TPG

@apiParam   {id = integer} id of the user
@apiParam   {hash = string} hash code of the cookie
@apiParam   {stopName = list of string}  list of stop
@apiParam   {code = string} optional should be stopName or stopCode

@apiSuccess {list of string} List of departure with handicapped capabilities
"""


@app.route('/list/stop/subscribed/nextDeparture/handicapped', methods=['GET'], defaults={'datatype': None})
@app.route('/list/stop/subscribed/nextDeparture/handicapped<path:datatype>', methods=['GET'])
def list_next_departure_for_handicaped(datatype):
    id = request.args.get('id')
    hash = request.args.get('hash')
    stop_name = request.args.getlist('stopName')
    request_code = request.args.get('code')
    if None == request_code:
        request_code = "stopName"
    if None == hash and None == id and None == stop_name:
        return jsonify(error="Bad request.")
    id = int(id)
    if 1 == user.auth_cookie(id, hash):
        return jsonify(next_departure_handicaped=client.get_next_departure(request_code, stop_name))
    return jsonify(error="Bad request.")


"""------------------------------------------------------------------------------------------------------------------"""
"""+----------------------------------------------------------------------------------------------------------------+"""
"""|                                             POST METHOD                                                        |"""
"""+----------------------------------------------------------------------------------------------------------------+"""
"""------------------------------------------------------------------------------------------------------------------"""


@app.route('/usr/signIn', methods=['POST'])
def __sign_in__():
    username = request.form.get('username')
    passwd = request.form.get('passwd')
    if not None == passwd and not None == username:
        cookie = user.sign_in(username, passwd)
        if 2 == len(cookie):
            return jsonify(cookie_hepia_tpg=cookie)
        return jsonify(error=cookie)
    return jsonify(error="Bad request.")


@app.route('/usr/del', methods=['POST'])
def __del_user__():
    id = request.form.get('id', type=int)
    hash = request.form.get('hash')
    if not None == id and not None == hash:
        return jsonify(error=user.del_user(id, hash))
    return jsonify(error="Bad request.")


@app.route('/usr/add', methods=['POST'])
def __add_user__():
    username = request.form.get('username')
    passwd = request.form.get('passwd')
    if not None == passwd and not None == username:
        return jsonify(error=user.add_user(username, passwd))
    return jsonify(error="Bad request.")


@app.route('/usr/signOut', methods=['POST'])
def __sign_out__():
    id = request.form.get('id', type=int)
    hash = request.form.get('hash')
    if not None == id and not None == hash:
        return jsonify(error=user.sign_out(id, hash))
    return jsonify(error="Bad request.")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Simple REST FTP server')
    parser.add_argument('-p', '--port', type=int, required=True, help='Listening port')
    parser.add_argument('-D', '--debug', action='store_true', help='Activate debug mode')
    args = parser.parse_args()
    app.run(host='0.0.0.0', port=args.port, debug=args.debug)
