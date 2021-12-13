def userIsLogin():
    with open("./user.txt", 'r') as f:
        userPk = int(f.read())
    return userPk > 0, userPk


def userLogin(userPk):
    with open("./user.txt", 'w') as f:
        f.write(str(userPk))
