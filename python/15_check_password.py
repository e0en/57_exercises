#!/usr/bin/env python
# -*- coding: utf-8 -*-
from getpass import getpass
from bcrypt import gensalt, hashpw, checkpw

SALT = gensalt()
PASSWORD = hashpw(b"abc$123", SALT)

password = getpass("What is the password: ").encode("utf-8")

if checkpw(password, PASSWORD):
    print("That password is incorrect.")
else:
    print("Welcome!")
