#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

html_template = '''<!DOCTYPE html>
<html lang="en">
  <head>
    <title>{title}</title>
    <meta author="{author}"></meta>
  </head>
  <body>
  </body>
</html>'''

site_name = input("Site name: ")
author = input("Author: ")
make_js_dir = input("Do you want a folder for Javascript? ") == "y"
make_css_dir = input("Do you want a folder for CSS? ") == "y"

os.mkdir(site_name)

with open(os.path.join(site_name, "index.html"), "w") as fp:
    fp.write(html_template.format(title=site_name, author=author))

if make_js_dir:
    os.mkdir(os.path.join(site_name, "js"))
if make_css_dir:
    os.mkdir(os.path.join(site_name, "css"))
