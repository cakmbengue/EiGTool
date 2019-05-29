#!/usr/bin/env python
# -*- coding:utf-8 -*- 
#
# EiG: Email Information Gathering
# @url: https://github.com/cakmbengue
# @author: Cheikh A. Khadre MBENGUE
)

from setuptools import setup 

setup(
    name='eig',

    version='0.1.5',
    description='Email OSINT',
    url='https://github.com/cakmbengue',
    
    author = 'Cheikh A. Khadre MBENGUE',
    author_email='mbengued@gmail.com',
    license='GPLv3',

    install_requires = ['colorama','requests','urllib3'],
    console =['eig.py'],
)
