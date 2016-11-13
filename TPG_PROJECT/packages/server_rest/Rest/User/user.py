import Rest.User.db.mysqlressourses as mysql
import hashlib


"""
@api {post} /usr/add/:userName/:password SetUser()

@apiName SetUser
@apiGroup User

@apiParam {String= Username, Password} user's credentials
"""


def set_user(username, passwd):
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


def sign_in(username, passwd):
    query = "Select * from user where username = '%s' and password = SHA2('%s', 512);"
    results = mysql.mysql_query(query % username % passwd)
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
@api {post} /usr/del/:userId DelUser()

@apiName DelUser
@apiGroup User

@apiParam {Integer= UserId} UserId user's id
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
@api {post} /usr/signout/:userId SignOut()

@apiName SignOut
@apiGroup User

@apiParam {Integer= UserId} UserId user's id
"""


def sign_out(id, hash):
    if 1 == auth_cookie(id, hashlib):
        query = "update user set logged = 0 where id = %i;"
        mysql.mysql_query(query % id)
        return "logged out."
    else:
        return "unable to log out."


def auth_cookie(id, hash):
    query = "Select * from user where id = %i;"
    results = mysql.mysql_query(query % id)
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
