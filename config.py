# -*- coding: utf-8 -*-

"""
info:
configurations file
NOTE: The three variables below must be filled in before running the script, or else it will not load.
api_id, api_hash, bot_token
You can also edit other variables, or leave it at default settings.
For what each variable is, refer to the comments.
"""

import datetime #output purposes

# id/hashfrom https://my.telegram.org/apps
# set this to your own api id and hash
api_id = 0
api_hash = '0'

# bot_token from BotFather
# set this to your own bot token
bot_token = '0'

# console window title
window_title = "JyutPing Bot"

# session file name
session_name = "bot"

# message bot sends upon receiving the /start command
start_text = """Hi! Thanks for using Jyutping Bot!\n
You can start using right now,
or refer to the /help command for instructions."""

# message bot sends upon receiving the /start command
help_text = """To use JyutPing Bot, input something from the supported input types.
If you input Chinese, entries with Traditional Chinese, Simplified Chinese, JyutPing, Pinyin, word meaning, words with similar pronunciation, and used in will be shown. (given that they exist)\n
Supported input types:
- single Chinese word *1
- Chinese word phrase *1
- single JyutPing word *2
- Jyutping word phrase *3\n
Notes:
*1 Do not include spaces in the input.
*2 Follow the JyutPing format, e.g. jyut6
*3 Seperate each JyutPing eord with a space. e.g. jyut6 jyu5\n
Have fun!"""

# maximum outputs for word used in
maxusedinoutput=8

dt = datetime.datetime.now()
print(dt.strftime("%m/%d/%Y %H:%M:%S")+" : config imported...")