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
    id = request.args.get['id']
    hash = request.args.get['hash']
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
    id = request.args.get['id']
    hash = request.args.get['hash']
    if 1 == user.auth_cookie(id, hash):
        query = "Select * from subscriptions where id = %i"
        mysql.mysql_query()
        return jsonify(stop_subscribed=client.get_stops())
    return jsonify(error="Bad request.")

"""
@api {get} /list/stop/subscribed/nextDeparture?id=&hash=&stopName list_next_departure()

@apiName list_next_departure
@apiGroup TPG

@apiParam   {id = integer} id of the user
@apiParam   {hash = string} hash code of the cookie
@apiParam   {list of string}  list of departure
"""


@app.route('/list/stop/subscribed/nextDeparture', methods=['GET'], defaults={'datatype': None})
@app.route('/list/stop/subscribed/nextDeparture<path:datatype>', methods=['GET'])
def list_next_departure(datatype):
    id = request.args.get['id']
    hash = request.args.get['hash']
    if 1 == user.auth_cookie(id, hash):
        return
    print (request.args.get('stops'))
    print (request.args.get('stopInfo'))
    return jsonify(error="Bad request.")


"""
@api {get} /list/stop/subscribe?id=&hash=&stopName= subscribe()

@apiName subscribe
@apiGroup TPG

@apiParam   {id = integer} id of the user
@apiParam   {hash = string} hash code of the cookie
@apiParam   {stopName = list of string}  list of stop name
"""


@app.route('/list/stop/subscribe', methods=['GET'])
def subscribe():
    id = request.args.get['id']
    hash = request.args.get['hash']
    if 1 == user.auth_cookie(id, hash):
        return
    print (request.args.getlist('stops'))
    return jsonify(error="Bad request.")


"""
@api {get} /list/stop/unsubscribe?stopName=&id=&hash= un_subscribe()

@apiName un_subscribe
@apiGroup TPG

@apiParam   {stopName = list of string}  list of stop name
@apiParam   {id = integer} id of the user
@apiParam   {hash = string} hash code of the cookie
"""


@app.route('/list/stop/unsubscribe', methods=['GET'])
def un_subscribe():
    id = request.args.get['id']
    hash = request.args.get['hash']
    if 1 == user.auth_cookie(id, hash):
        return
    print (request.args.get('stops'))
    return jsonify(error="Bad request.")


"""
@api {get} /list/stop/around500Meter?id=&hash=&latitude=&longitude= get_stop_localisation()

@apiName get_stop_localisation
@apiGroup TPG

@apiParam   {id = integer} id of the user
@apiParam   {hash = string} hash code of the cookie
@apiParam   {latitude = list of integer} list of latitude
@apiParam   {longitude = list of integer} list of longitude

@apiSuccess {list of string} list of stops around 500 meters for a location
"""


@app.route('/list/stop/around500Meter', methods=['GET'], defaults={'datatype': None})
@app.route('/list/stop/around500Meter<path:datatype>', methods=['GET'])
def get_stop_localisation(datatype):
    id = request.args.get['id']
    hash = request.args.get['hash']
    if 1 == user.auth_cookie(id, hash):
        return
    print (request.args.get('latitude'))
    print (request.args.get('longitude'))
    return jsonify(error="Bad request.")


"""
@api {get} /list/stop/subscribed/nextDeparture/handicaped?id=&hash=&stopName= list_next_departure_for_handicaped()

@apiName list_next_departure_for_handicaped
@apiGroup TPG

@apiParam   {id = integer} id of the user
@apiParam   {hash = string} hash code of the cookie
@apiParam   {stopName = list of string}  list of stop name

@apiSuccess {String = HandiBus} list of bus with handicapped capabilities
"""


@app.route('/list/stop/subscribed/nextDeparture/handicapped', methods=['GET'], defaults={'datatype': None})
@app.route('/list/stop/subscribed/nextDeparture/handicapped<path:datatype>', methods=['GET'])
def list_next_departure_for_handicaped(datatype):
    id = request.args.get['id']
    hash = request.args.get['hash']
    if 1 == user.auth_cookie(id, hash):
        return
    print (request.args.get('stops'))
    print (request.args.get('stopInfo'))
    return jsonify(error="Bad request.")


"""------------------------------------------------------------------------------------------------------------------"""
"""+----------------------------------------------------------------------------------------------------------------+"""
"""|                                             POST METHOD                                                        |"""
"""+----------------------------------------------------------------------------------------------------------------+"""
"""------------------------------------------------------------------------------------------------------------------"""


@app.route('/usr/signIn', methods=['POST'])
def __sign_in__():
    passwd = request.json['passwd']
    username = request.json['username']
    if not None == passwd and not None == username:
        cookie = user.sign_in(username, passwd)
        if 2 == len(cookie):
            return jsonify(cookie_hepia_tpg=cookie)
        return  jsonify(error=cookie)
    return jsonify(error="Bad request.")


@app.route('/usr/del', methods=['POST'])
def __del_user__():
    id = request.json['id']
    hash = request.json['hash']
    if not None == id and not None == hash:
        return jsonify(error=user.del_user(id, hash))
    return jsonify(error="Bad request.")


@app.route('/usr/add', methods=['POST'])
def __add_user__(passwd, user):
    passwd = request.json['passwd']
    username = request.json['username']
    if not None == passwd and not None == username:
        return jsonify(error=user.add_user(username, passwd))
    return jsonify(error="Bad request.")


@app.route('/usr/signOut', methods=['POST'])
def __sign_out__(uid, user):
    id = request.json['id']
    hash = request.json['hash']
    if not None == id and not None == hash:
        return jsonify(error=user.sign_out(id, hash))
    return jsonify(error="Bad request.")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Simple REST FTP server')
    parser.add_argument('-p', '--port', type=int, required=True, help='Listening port')
    parser.add_argument('-D', '--debug', action='store_true', help='Activate debug mode')
    args = parser.parse_args()
    app.run(host='0.0.0.0', port=args.port, debug=args.debug)