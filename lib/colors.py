#!/usr/bin/env python
# -*- coding:utf-8 -*- 
#
# EiG: Email Information Gathering
# @url: https://github.com/cakmbengue
# @author: Cheikh A. Khadre MBENGUE

import sys
import colorama


if sys.platform == 'win32':
    colorama.init()
    
R = "\033[%s;31m"
B = "\033[%s;34m"
G = "\033[%s;32m"
W = "\033[%s;38m"
Y = "\033[%s;33m"
E = "\033[0m"
