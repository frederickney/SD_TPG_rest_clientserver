"""
@api {list} /stop/available

@apiName GetAvailableStops
@apiGroup Tpg
 
@apiSuccess {String}
"""
 
"""
@api {get} /stop/subscribe/:userId

@apiName Subscribe
@apiGroup Tpg

@apiParam {Integer} userId User's identifier
"""
 
"""
@api {get} /stop/unsubscribe/:stopName/:userId

@apiName Unsubscribe
@apiGoup Tpg

@apiParam {String} StopName Stop's name
@apiParam {Integer} userId User's Identifier
"""
 
"""
@api {list} /stop/bus/handicappedEquiped/:stopName

@apiName GetHandicappedEquiped
@apiGroup Tpg

@apiParam {String} StopName

@apiSuccess {String} HandiBus
"""
 
"""
@api {list} /stop/bus/subscribed/:userId/:stopName

@apiName NextBusList
@apiGroup Tpg

@apiParam {Integer} UserId
@apiParam {String} StopName

@apiSuccess {String}
"""
 
"""
@api {list} /stop/:position

@apiName ListStopByPosition
@apiGroup Tpg

@apiParam {Point} StopPosition

@apiSuccess {String}
"""
