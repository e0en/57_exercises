#!/usr/bin/env python
# -*- coding: utf-8 -*-


number_to_name = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December",
}

number = int(input("Please enter the number of the month: "))
print(f"The name of the month is {number_to_name[number]}.")
