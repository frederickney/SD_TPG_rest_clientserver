from db import mysqlressourses as mysql


"""
@api {post} /usr/add/:userName/:password SetUser()

@apiName SetUser
@apiGroup User

@apiParam {String= Username, Password} user's credentials
"""


def SetUser(username, passwd):
    query = "Insert into users (id, username, password) values ( NULL, '%s', SHA2('%s', 512));"
    result = mysql.mysql_query(query % username % passwd, "insert")
    if 0 == result:
        return "To register your user."
    elif 1 == result:
        return "User registered"


"""
@api {post} /usr/signin/:userName/password SignIn()

@apiName SignIn
@apiGroup User

@apiParam {String= Username, Password} user's credentials
"""


def SignIn(username, passwd):
    query = "Select id form user where user = '%s' and password = SHA2('%s', 512);"
    results = mysql.mysql_query(query % username % passwd)
    if 1 == len(results):
        for row in results:
            result = row["id"]
    elif 0 == len(results):
        result = "Unable to sign in, please register before login or verify your username and password"
    return result


"""
@api {post} /usr/del/:userId DelUser()

@apiName DelUser
@apiGroup User

@apiParam {Integer= UserId} UserId user's id
"""


def DelUser(UserId):
    return


"""
@api {post} /usr/signout/:userId SignOut()

@apiName SignOut
@apiGroup User

@apiParam {Integer= UserId} UserId user's id
"""


def SignIn(UserId):
    return

