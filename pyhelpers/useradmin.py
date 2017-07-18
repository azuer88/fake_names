#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# author: Blue Cuenca <blue.cuenca@gmail.com>

import libuser
import os
import string
import random

from passlib.hash import sha512_crypt
from libuser import GECOS, USERPASSWORD, SHADOWPASSWORD


class AdminSingleton(object):

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(AdminSingleton, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        super(AdminSingleton, self).__init__(self)
        self.admin = libuser.admin()

    def get_admin(self):
        return self.admin


def encrypt_password(password):
    saltsrc = string.digits + string.letters
    salt = "".join(random.sample(saltsrc, 8))
    return sha512_crypt.encrypt(password, salt=salt, rounds=5000)


def mkuser(username, fullname, password):
    sa = AdminSingleton()
    admin = sa.get_admin()

    user = admin.initUser(username)
    user.set(GECOS, fullname)

    user.set(USERPASSWORD, "x")
    user.set(SHADOWPASSWORD, encrypt_password(password))

    return admin.addUser(user)


def rmuser(username):
    sa = AdminSingleton()
    admin = sa.get_admin()

    user = admin.lookupUserByName(username)
    admin.deleteUser(user)
    admin.removeHome(user)
    admin.removeMail(user)


def check_permissions():
    if os.geteuid != 0:
        raise Exception("administrative privileges required.")


def main():

    # check_permissions()

    print encrypt_password("password")

    # u = mkuser("deleteme", "Delete Me User", "password")
    # print "u = ", u

    rmuser("deleteme")
    # for k in u.keys():
    #     print "{}: '{}'\n".format(k, u.get(k))


if __name__ == "__main__":
    import sys
    sys.exit(main())
