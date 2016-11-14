__author__ = 'Frederick NEY & Stephane Overlen'
import Rest.User.db.mysqlressourses as mysql
import hashlib


"""
@api {post} /usr/add?userName=&password= SetUser()

@apiName SetUser
@apiGroup User

@apiParam {Username = string} user's credentials
@apiParam {Password = string} user's credentials

@apiSuccess {string} message
"""


def add_user(username, passwd):
    query = "Insert into users (id, username, password) values ( NULL, '%s', SHA2('%s', 512));"
    result = mysql.mysql_query(query % username % passwd, "insert")
    if 0 == result:
        return "Unable to register your user."
    else:
        return "User registered"


"""
@api {post} /usr/signIn?username=&passwd= SignIn()

@apiName SignIn
@apiGroup User

@apiParam {Username = string} user's credentials
@apiParam {Password = string} user's credentials

@apiSuccess {string or cookie} message or session
"""


def sign_in(username, passwd):
    query = "Select * from user where username = '%s' and password = SHA2('%s', 512);"
    results = mysql.mysql_query(query % username % passwd)
    if 0 > results:
        result = "Unable to sign in, please register before login or verify your username and password"
    if 1 == len(results):
        """ /* setting up cookie for user registered */ """
        for row in results:
            result = {"id", "hash"}
            result["id"] = row["id"]
            result["hash"] = hashlib.sha512(row["id"] + row["user"] + row["password"]).hexdigest()
            query = "update user set logged = 1 where id = %i;"
            mysql.mysql_query(query % id)
            return result
    elif 0 == len(results):
        result = "Unable to sign in, please register before login or verify your username and password"
        return result


"""
@api {post} /usr/del?id=&hash= DelUser()

@apiName DelUser
@apiGroup User

@apiParam {id = integer} user id
@apiParam {hash = string} session hash

@apiSuccess {string} message
"""


def del_user(id, hash):
    if 1 == auth_cookie(id, hash):
        query = "delete from subscriptions where id = %i"
        if 0 <= mysql.mysql_query(query % id, "delete"):
            query = "delete from subbscriptions where id = %i"
            if 0 < mysql.mysql_query(query % id, "delete"):
                return "User successfully deleted"
            else:
                return "unable to delete user"
        else:
            return "unable to delete subscriptions"
    else:
        result = "sorry wrong session id."
        return result


"""
@api {post} /usr/signOut?id=&hash= SignOut()

@apiName SignOut
@apiGroup User

@apiParam {Integer= id} user id
@apiParam {hash = string} session hash

@apiSuccess {string} message
"""


def sign_out(id, hash):
    if 1 == auth_cookie(id, hash):
        query = "update user set logged = 0 where id = %i;"
        result = mysql.mysql_query(query % id)
        if 0 < result:
            return "logged out."
    else:
        return "unable to log out."


def auth_cookie(id, hash):
    query = "Select * from user where id = %i;"
    results = mysql.mysql_query(query % id)
    if 0 > results:
        return 0
    if 1 == len(results):
        """ /* authentify user */ """
        for row in results:
            hash_verify = hashlib.sha512(row["id"] + row["user"] + row["password"]).hexdigest()
            if hash == hash_verify and row["logged"] == 1:
                return 1
            else:
                return 0
    elif 0 == len(results):
        return 0
    return
