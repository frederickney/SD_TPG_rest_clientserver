define({ "api": [
  {
    "type": "get",
    "url": "/stop/available/",
    "title": "GetAvailableStops()",
    "name": "GetAvailableStops",
    "group": "Tpg",
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "String",
            "allowedValues": [
              "StopList"
            ],
            "optional": false,
            "field": "StopList",
            "description": "<p>list of available stop</p>"
          }
        ]
      }
    },
    "version": "0.0.0",
    "filename": "TPG_PROJECT/packages/server_rest/tpg/tpg.py",
    "groupTitle": "Tpg"
  },
  {
    "type": "get",
    "url": "/stop/bus/handicappedEquiped/:stopName",
    "title": "GetHandicappedEquiped()",
    "name": "GetHandicappedEquiped",
    "group": "Tpg",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "String",
            "allowedValues": [
              "StopName"
            ],
            "optional": false,
            "field": "StopName",
            "description": ""
          }
        ]
      }
    },
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "String",
            "allowedValues": [
              "HandiBus"
            ],
            "optional": false,
            "field": "HandiBus",
            "description": "<p>Handicaped bus list</p>"
          }
        ]
      }
    },
    "version": "0.0.0",
    "filename": "TPG_PROJECT/packages/server_rest/tpg/tpg.py",
    "groupTitle": "Tpg"
  },
  {
    "type": "get",
    "url": "/stop/:positionx/:positiony",
    "title": "ListStopByPosition()",
    "name": "ListStopByPosition",
    "group": "Tpg",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "Integer",
            "allowedValues": [
              "Positionx",
              "Positiony"
            ],
            "optional": false,
            "field": "Specific",
            "description": "<p>location</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "String",
            "allowedValues": [
              "ListStopByPosition"
            ],
            "optional": false,
            "field": "ListStopByPosition",
            "description": "<p>Stop bus list by specific location</p>"
          }
        ]
      }
    },
    "version": "0.0.0",
    "filename": "TPG_PROJECT/packages/server_rest/tpg/tpg.py",
    "groupTitle": "Tpg"
  },
  {
    "type": "get",
    "url": "/stop/bus/subscribed/:userId/:stopName",
    "title": "NextBusList()",
    "name": "NextBusList",
    "group": "Tpg",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "Integer",
            "allowedValues": [
              "UserId"
            ],
            "optional": false,
            "field": "UserId",
            "description": ""
          },
          {
            "group": "Parameter",
            "type": "String",
            "allowedValues": [
              "StopName"
            ],
            "optional": false,
            "field": "StopName",
            "description": ""
          }
        ]
      }
    },
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "String",
            "allowedValues": [
              "NextBusList"
            ],
            "optional": false,
            "field": "NextBusList",
            "description": "<p>list of next bus</p>"
          }
        ]
      }
    },
    "version": "0.0.0",
    "filename": "TPG_PROJECT/packages/server_rest/tpg/tpg.py",
    "groupTitle": "Tpg"
  },
  {
    "type": "get",
    "url": "/stop/subscribe/:userId",
    "title": "Subscribe()",
    "name": "Subscribe",
    "group": "Tpg",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "Integer",
            "allowedValues": [
              "UserId"
            ],
            "optional": false,
            "field": "UserId",
            "description": "<p>User's identifier</p>"
          }
        ]
      }
    },
    "version": "0.0.0",
    "filename": "TPG_PROJECT/packages/server_rest/tpg/tpg.py",
    "groupTitle": "Tpg"
  },
  {
    "type": "get",
    "url": "/stop/unsubscribe/:stopName/:userId",
    "title": "Unsubscribe()",
    "name": "Unsubscribe",
    "group": "Tpg",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "String",
            "allowedValues": [
              "StopName"
            ],
            "optional": false,
            "field": "StopName",
            "description": "<p>Stop's name</p>"
          },
          {
            "group": "Parameter",
            "type": "Integer",
            "allowedValues": [
              "UserId"
            ],
            "optional": false,
            "field": "UserId",
            "description": "<p>User's Identifier</p>"
          }
        ]
      }
    },
    "version": "0.0.0",
    "filename": "TPG_PROJECT/packages/server_rest/tpg/tpg.py",
    "groupTitle": "Tpg"
  },
  {
    "type": "post",
    "url": "/usr/del/:userId",
    "title": "DelUser()",
    "name": "DelUser",
    "group": "User",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "Integer",
            "allowedValues": [
              "UserId"
            ],
            "optional": false,
            "field": "UserId",
            "description": "<p>user's id</p>"
          }
        ]
      }
    },
    "version": "0.0.0",
    "filename": "TPG_PROJECT/packages/server_rest/user/user.py",
    "groupTitle": "User"
  },
  {
    "type": "post",
    "url": "/usr/add/:userName/:password",
    "title": "SetUser()",
    "name": "SetUser",
    "group": "User",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "String",
            "allowedValues": [
              "Username",
              "Password"
            ],
            "optional": false,
            "field": "user",
            "description": "<p>'s credentials</p>"
          }
        ]
      }
    },
    "version": "0.0.0",
    "filename": "TPG_PROJECT/packages/server_rest/user/user.py",
    "groupTitle": "User"
  },
  {
    "type": "post",
    "url": "/usr/signin/:userName/password",
    "title": "SignIn()",
    "name": "SignIn",
    "group": "User",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "String",
            "allowedValues": [
              "Username",
              "Password"
            ],
            "optional": false,
            "field": "user",
            "description": "<p>'s credentials</p>"
          }
        ]
      }
    },
    "version": "0.0.0",
    "filename": "TPG_PROJECT/packages/server_rest/user/user.py",
    "groupTitle": "User"
  },
  {
    "type": "post",
    "url": "/usr/signout/:userId",
    "title": "SignOut()",
    "name": "SignOut",
    "group": "User",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "Integer",
            "allowedValues": [
              "UserId"
            ],
            "optional": false,
            "field": "UserId",
            "description": "<p>user's id</p>"
          }
        ]
      }
    },
    "version": "0.0.0",
    "filename": "TPG_PROJECT/packages/server_rest/user/user.py",
    "groupTitle": "User"
  }
] });