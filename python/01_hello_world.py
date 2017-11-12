#!/usr/bin/env python
# -*- coding: utf-8 -*-


def prompt():
    return input("What is your name? ")


def msg_for(name):
    return f"Hello, {name}, nice to meet you!"


if __name__ == '__main__':
    print(msg_for(prompt()))
