# -*- coding: utf-8 -*-

"""
info:
configurations file
edit variables before using JyutPing Bot
"""

import datetime #output purposes

# console window title
# set this to anything you like. Has no impact to script
window_title = "JyutPing Bot"

# session file name
# set this to anything you like. Has no impact to script
session_name = "bot"

# id/hashfrom https://my.telegram.org/apps
#set this to your own api id and hash
api_id = 0
api_hash = '0'

# bot_token from BotFather
#set this to your own bot token
bot_token = '0'

dt = datetime.datetime.now()
print(dt.strftime("%m/%d/%Y %H:%M:%S")+" : config imported...")
