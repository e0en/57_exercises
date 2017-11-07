#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re

def validate_first_name(first):
    return len(first) >= 2

def validate_last_name(last):
    return len(last) >= 2

employee_id_re = re.compile("^[a-zA-Z]{2}-\d{4}$")

def validate_employee_id(employee_id):
    return employee_id_re.match(employee_id)

def validate_zip_code(zip_code):
    return zip_code.isnumeric()

def validate_input(first, last, zip_code, employee_id):
    all_valid =\
        validate_first_name(first) and\
        validate_last_name(last) and\
        validate_zip_code(zip_code) and\
        validate_employee_id(employee_id)
    return all_valid

first_name = input("Enter the first name: ")
last_name = input("Enter the last name: ")
zip_code = input("Enter the ZIP code: ")
employee_id = input("Enter an employee ID: ")

message = ""

if first_name == '':
    message += "The first name must be filled in.\n"
elif not validate_first_name(first_name):
    message += f'"{first_name}" is not a valid first name. It is too short.\n'

if last_name == '':
    message += "The last name must be filled in.\n"
elif not validate_last_name(last_name):
    message += f'"{last_name}" is not a valid last name. It is too short.\n'

if employee_id == '':
    message += "The employee id must be filled in.\n"
elif not validate_employee_id(employee_id):
    message += f'{employee_id} is not a valid ID.\n'

if zip_code == '':
    message += "The ZIP code must be filled in.\n"
elif not validate_zip_code(zip_code): 
    message += "The ZIP code must be numeric.\n"

if validate_input(first_name, last_name, zip_code, employee_id):
    message = "There were no errors found.\n"

print(message, end="")
