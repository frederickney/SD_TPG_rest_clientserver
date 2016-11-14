__author__ = 'Frederick NEY & Stephane Overlen'
import Rest.User.db.mysqlressourses as mysql
import hashlib


"""
@api {post} /usr/add?userName=&password= add_user()

@apiName add_user
@apiGroup User

@apiParam {string = USERNAMe} user's credentials
@apiParam {string = PASSWD} user's credentials

@apiSuccess {string = return} message
"""


def add_user(username, passwd):
    print (type(username))
    query = "Insert into users (id, username, password, logged) values ( NULL, '%s', SHA2('%s', 512), 0);"
    result = mysql.mysql_query(query % (username, passwd), "insert")
    if 0 == result:
        return "Unable to register your user."
    else:
        return "User registered"


"""
@api {post} /usr/signIn?username=USERNAME&passwd=PASSWD sign_in()

@apiName sign_in
@apiGroup User

@apiParam {string = USERNAME} user's credentials
@apiParam {string = PASSWD} user's credentials

@apiSuccess {string or cookie = return} message or session
"""


def sign_in(username, passwd):
    query = "Select * from users where username = '%s' and password = SHA2('%s', 512);"
    results = mysql.mysql_query(query % (username, passwd))
    if 1 == len(results):
        """ /* setting up cookie for user registered */ """
        for row in results:
            result = {"id": row[0], "hash": hashlib.sha512(str(row[0]).encode('utf-8') + row[1].encode('utf-8') + row[2].encode('utf-8')).hexdigest()}
            query = "update users set logged = 1 where id = %i;"
            mysql.mysql_query(query % row[0], "update")
            return result
    elif 0 == len(results):
        result = "Unable to sign in, please register before login or verify your username and password"
        return result


"""
@api {post} /usr/del?id=ID&hash=HASH del_user()

@apiName del_user
@apiGroup User

@apiParam {integer = ID} user id
@apiParam {string = HASH} session hash

@apiSuccess {string = result} message
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
@api {post} /usr/signOut?id=ID&hash=HASH sign_out()

@apiName sign_out
@apiGroup User

@apiParam {Integer = ID} user id
@apiParam {string = HASH} session hash

@apiSuccess {result = string} message
"""


def sign_out(id, hash):
    if 1 == auth_cookie(id, hash):
        query = "update users set logged = 0 where id = %i;"
        result = mysql.mysql_query(query % id, "update")
        if 0 < result:
            return "logged out."
    else:
        return "unable to log out."


def auth_cookie(id, hash):
    query = "Select * from users where id = %i;"
    results = mysql.mysql_query(query % id)
    if 1 == len(results):
        """ /* authentify user */ """
        for row in results:
            hash_verify = hashlib.sha512(str(row[0]).encode('utf-8') + row[1].encode('utf-8') + row[2].encode('utf-8')).hexdigest()
            if hash == hash_verify and row[3] == 1:
                return 1
            else:
                return 0
    elif 0 == len(results):
        return 0
    return
