#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Use text editor to edit the script and type in valid Instagram username/password

from InstagramAPI import InstagramAPI
import configparser

config = configparser.ConfigParser()
config.read("login.ini")

username = config["LOGIN"]["username"]
passwd = config["LOGIN"]["password"]
InstagramAPI = InstagramAPI(username, passwd)
if (InstagramAPI.login()):
    InstagramAPI.getSelfUserFeed()  # get self user feed
    print(InstagramAPI.LastJson)  # print last response JSON
    print("Login success!")
else:
    print("Can't login!")
