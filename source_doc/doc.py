__author__ = 'admin_master'


"""
@api {post} /usr/add add_user()

@apiName add_user
@apiGroup User

@apiParam {USERNAME = string} user's credentials
@apiParam {PASSWD = string} user's credentials

@apiSuccess {return = string[]} message
"""

"""
@api {post} /usr/signIn sign_in()

@apiName sign_in
@apiGroup User

@apiParam {USERNAME = string} user's credentials
@apiParam {PASSWD = string} user's credentials

@apiSuccess {return = string[]} message or session
"""

"""
@api {post} /usr/del del_user()

@apiName del_user
@apiGroup User

@apiParam {ID = Integer} user id
@apiParam {HASH = string} session hash

@apiSuccess {return = string[]} message
"""

"""
@api {post} /usr/signOut sign_out()

@apiName sign_out
@apiGroup User

@apiParam {ID = Integer} user id
@apiParam {HASH = string} session hash

@apiSuccess {return = string[]} message
"""

"""
@api {get} /stop/available?id=ID&hash=HASH list_available_stop()

@apiName list_available_stop
@apiGroup TPG

@apiParam {ID = Integer} user id
@apiParam {HASH = string} session hash

@apiSuccess {return = string[]} list of available stop
"""

"""
@api {get} /list/stop/subscribed?id=ID&hash=HASH list_stop_subscribed()

@apiName list_stop_subscribed
@apiGroup TPG

@apiParam {ID = Integer} user id
@apiParam {HASH = string} session hash


@apiSuccess {string[]  = return} list of stop
"""

"""
@api {get} /list/stop/subscribed/nextDeparture?id=ID&hash=HASH&stopName=STOPNAME&code=CODE list_next_departure()

@apiName list_next_departure
@apiGroup TPG

@apiParam {ID = Integer} user id
@apiParam {HASH = string} session hash
@apiParam   {STOPNAME = string[]}  list of stop
@apiParam   {CODE = string} optional should be 'stopName' or 'stopCode'

@apiSuccess {return = string[]} List of departure
"""


"""
@api {get} /list/stop/subscribe?id=ID&hash=HASH&stopName=STOPCODE subscribe()

@apiName subscribe
@apiGroup TPG

@apiParam {ID = Integer} user id
@apiParam {HASH = string} session hash
@apiParam   {STOPCODE = string[]}  list of stop

@apiSuccess {return = string} error code
"""


"""
@api {get} /list/stop/unsubscribe?stopName=STOPCODE&id=ID&hash=HASH un_subscribe()

@apiName un_subscribe
@apiGroup TPG

@apiParam {ID = Integer} user id
@apiParam {HASH = string} session hash
@apiParam   {STOPCODE = string[]}  list of stop


@apiSuccess {return = string} error code
"""

"""
@api {get} /list/stop/around500Meter?id=ID&hash=HASH&latitude=LAT&longitude=LONG get_stop_localisation()

@apiName get_stop_localisation
@apiGroup TPG

@apiParam {ID = Integer} user id
@apiParam {HASH = string} session hash
@apiParam   {LAT = float[]} list of latitude
@apiParam   {LONG = float[]} list of longitude

@apiSuccess {return = string[]} list of stops around 500 meters for a location
"""

"""
@api {get} /list/stop/subscribed/nextDeparture/handicaped?id=ID&hash=HASH&stopName=STOPCODE&code=CODE list_next_departure_for_handicaped()

@apiName list_next_departure_for_handicaped
@apiGroup TPG

@apiParam {ID = Integer} user id
@apiParam {HASH = string} session hash
@apiParam   {STOPCODE = string[]}  list of stop
@apiParam   {CODE = string} optional should be 'stopName' or 'stopCode'


@apiSuccess {return = string[]} List of departure with handicapped capabilities
"""