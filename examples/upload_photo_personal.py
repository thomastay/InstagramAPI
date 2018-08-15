#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Use text editor to edit the script and type in valid Instagram username/password

from InstagramAPI import InstagramAPI
import configparser

config = configparser.ConfigParser()
config.read("../login.ini")
username = config["LOGIN"]["username"]
passwd = config["LOGIN"]["password"]
InstagramAPI = InstagramAPI(username, passwd)
InstagramAPI.login()  # login

photo_path = '/home/thomas/Pictures/girl1.jpg'
caption = "This is too real #deep"
InstagramAPI.uploadPhoto(photo_path, caption=caption)
