#!/bin/python
import os

#Set your bot token here
token = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'

#Set the user or group chat id here
chat_id = 111111111

#cd to the script's directory
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)
