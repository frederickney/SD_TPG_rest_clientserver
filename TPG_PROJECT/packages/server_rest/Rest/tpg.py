"""
@api {get} /stop/available/ GetAvailableStops()

@apiName GetAvailableStops
@apiGroup Tpg

@apiSuccess {String= StopList} StopList list of available stop
"""

""" 
@api {get} /stop/subscribe/:userId Subscribe()

@apiName Subscribe 
@apiGroup Tpg 

@apiParam {Integer= UserId} UserId User's identifier
"""

"""
@api {get} /stop/unsubscribe/:stopName/:userId Unsubscribe()

@apiName Unsubscribe 
@apiGroup Tpg 

@apiParam {String= StopName} StopName Stop's name 
@apiParam {Integer= UserId} UserId User's Identifier 
""" 
 
""" 
@api {get} /stop/bus/handicappedEquiped/:stopName GetHandicappedEquiped()

@apiName GetHandicappedEquiped 
@apiGroup Tpg 

@apiParam {String= StopName} StopName 

@apiSuccess {String= HandiBus} HandiBus Handicaped bus list
""" 
 
""" 
@api {get} /stop/bus/subscribed/:userId/:stopName NextBusList()

@apiName NextBusList 
@apiGroup Tpg 

@apiParam {Integer= UserId} UserId 
@apiParam {String= StopName} StopName 

@apiSuccess {String= NextBusList} NextBusList list of next bus
"""
  
""" 
@api {get} /stop/:positionx/:positiony ListStopByPosition()

@apiName ListStopByPosition 
@apiGroup Tpg 

@apiParam {Integer= Positionx, Positiony} Specific location

@apiSuccess {String= ListStopByPosition} ListStopByPosition Stop bus list by specific location
"""
