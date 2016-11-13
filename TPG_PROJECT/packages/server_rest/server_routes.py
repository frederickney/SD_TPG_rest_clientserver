__author__ = 'admin_master'

import re
import argparse
from flask import Flask, request, jsonify
from Rest.User.user import *
from Rest.tpg import *

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


@app.route('/list/stop/available', defaults={'datatype': None}, methods=['GET'])
@app.route('/list/stop/available<path:datatype>', methods=['GET'])
def list_available_stop(datatype):
    print request.args.get('id')
    print request.args.get('username')
    return jsonify(id=1)


@app.route('/list/stop/subscribed', defaults={'datatype': None}, methods=['GET'])
@app.route('/list/stop/subscribed?<path:datatype>', methods=['GET'])
def get_subscribed(datatype):
    print request.args.get('id')
    print request.args.get('username')
    print request.args.get('stops')
    print request.args.get('stopInfo')
    return jsonify(id=1)


@app.route('/list/stop/subscribed', methods=['GET'], defaults={'datatype': None})
@app.route('/list/stop/subscribed<path:datatype>', methods=['GET'])
def list_stop(datatype):
    print request.args.get('id')
    print request.args.get('username')
    return jsonify(id=1)


@app.route('/list/stop/subscribed/nextDeparture', methods=['GET'], defaults={'datatype': None})
@app.route('/list/stop/subscribed/nextDeparture<path:datatype>', methods=['GET'])
def list_next_departure(datatype):
    print request.args.get('id')
    print request.args.get('username')
    print request.args.get('stops')
    print request.args.get('stopInfo')
    return jsonify(id=1)


@app.route('/list/stop/subscribe', methods=['GET'])
def subscribe():
    print request.args.get('id')
    print request.args.get('username')
    print request.args.get('stops')
    return jsonify(id=1)


@app.route('/list/stop/unsubscribe', methods=['GET'])
def un_subscribe():
    print request.args.get('id')
    print request.args.get('username')
    print request.args.get('stops')
    return jsonify(id=1)


@app.route('/list/stop/around500Meter', methods=['GET'], defaults={'datatype': None})
@app.route('/list/stop/around500Meter<path:datatype>', methods=['GET'])
def get_stop_localisation(datatype):
    print request.args.get('id')
    print request.args.get('username')
    print request.args.get('latitude')
    print request.args.get('longitude')
    return jsonify(id=1)


@app.route('/list/stop/subscribed/nextDeparture/handicaped', methods=['GET'], defaults={'datatype': None})
@app.route('/list/stop/subscribed/nextDeparture/handicaped<path:datatype>', methods=['GET'])
def list_next_departure_for_handicaped(datatype):
    print request.args.get('id')
    print request.args.get('username')
    print request.args.get('stops')
    print request.args.get('stopInfo')
    return jsonify(id=1)


"""------------------------------------------------------------------------------------------------------------------"""
"""+----------------------------------------------------------------------------------------------------------------+"""
"""|                                             POST METHOD                                                        |"""
"""+----------------------------------------------------------------------------------------------------------------+"""
"""------------------------------------------------------------------------------------------------------------------"""


@app.route('/usr/signIn', methods=['POST'])
def login():
    print request.json['passwd']
    print request.json['username']
    return jsonify(id=1)


@app.route('/usr/del', methods=['POST'])
def del_user():
    print request.json['id']
    print request.json['username']
    return jsonify(id=1)


@app.route('/usr/add', methods=['POST'])
def add_user(passwd, user):
    print request.json['passwd']
    print request.json['username']
    return jsonify(id=1)


@app.route('/usr/signOut', methods=['POST'])
def sign_out(uid, user):
    print request.json['id']
    print request.json['username']
    return jsonify(id=1)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Simple REST FTP server')
    parser.add_argument('-p', '--port', type=int, required=True, help='Listening port')
    parser.add_argument('-D', '--debug', action='store_true', help='Activate debug mode')
    args = parser.parse_args()
    app.run(host='0.0.0.0', port=args.port, debug=args.debug)