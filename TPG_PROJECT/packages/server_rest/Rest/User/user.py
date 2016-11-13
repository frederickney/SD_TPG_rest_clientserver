import

"""
@api {post} /usr/add/:userName/:password SetUser()

@apiName SetUser
@apiGroup User

@apiParam {String= Username, Password} user's credentials
"""


def SetUser(self, Username, Password):
	return


"""
@api {post} /usr/signin/:userName/password SignIn()

@apiName SignIn
@apiGroup User

@apiParam {String= Username, Password} user's credentials
"""


def SignIn(self, Username, Password):
	return


"""
@api {post} /usr/del/:userId DelUser()

@apiName DelUser
@apiGroup User

@apiParam {Integer= UserId} UserId user's id
"""


def DelUser(self, UserId):
	return


"""
@api {post} /usr/signout/:userId SignOut()

@apiName SignOut
@apiGroup User

@apiParam {Integer= UserId} UserId user's id
"""


def SignIn(self, UserId):
	return

