#!/usr/bin/env python
# -*- coding: utf-8 -*-

def is_anagram(s1, s2):
    return len(s1) == len(s2) and sorted(s1) == sorted(s2)


print("Enter two string and I'll tell you if they are anagrams:")
s1 = input("Enter the first string: ")
s2 = input("Enter the first string: ")

are_arent = "are" if is_anagram(s1, s2) else "are not"
print(f'"{s1}" and "{s2}" {are_arent} anagrams.')
