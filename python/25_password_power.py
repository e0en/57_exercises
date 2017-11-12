#!/usr/bin/env python
# -*- coding: utf-8 -*-
from enum import Enum

class PasswordStrength(Enum):
    VERY_WEAK = 1
    WEAK = 2
    STRONG = 3
    VERY_STRONG = 4


def calc_password_strength(pw):
    if len(pw) < 8:
        if pw.isnumeric():
            return PasswordStrength.VERY_WEAK
        elif pw.isalpha():
            return PasswordStrength.WEAK
    else:
        if not (pw.isnumeric() or pw.isalpha()) and pw.isalnum():
            return PasswordStrength.STRONG
        elif not pw.isalnum():
            return PasswordStrength.VERY_STRONG


STRENGTH_NAME = {
    PasswordStrength.VERY_WEAK: 'very weak',
    PasswordStrength.WEAK: 'weak',
    PasswordStrength.STRONG: 'strong',
    PasswordStrength.VERY_STRONG: 'very strong',
}



password = input("Enter your password: ")
strength = calc_password_strength(password)

print(f"The password '{password}' is a {STRENGTH_NAME[strength]} password.")
