# Telegram JyutPing Bot

current version: 1.0.0

Telegram JyutPing Bot is a telegram bot script written in Python. 
It is a dictionary, searching for entries based on Chinese input. 
This is a work in progress.

https://github.com/yuenedmond/JyutPing-Bot

This program is developed on:

Python 3.8.2

Telethon 1.13.0

CC-CEDICT (2020-05-27)

CC-Canto (170202)

CC-CEDICT Cantonese readings (150923)

Ekho (jyutping-wong-16000-v6)

Pydub 0.24.0

Honorable Mention: PyCantonese

I initially built a prototype of this using the PyCantonese library.
It is written very well, 
but unfortunately the corpus was not big enough.

## To Do List
add text to speech

## Installation

In Telegram, find BotFather and create a bot.

etc.

Use pip to install necessary prerequisites.

pip install -r requirements.txt

Bot


## Usage

## Files/Directories

corpus/

Includes 3 modified corpus files. Original versions located in corpus/original/.

cantoreading.py

Corpus parser for CC-CEDICT Cantonese readings.

cccanto.py

Corpus parser for CC-Canto.

cedict.py

Corpus parser for CC-CEDICT.

config.py

Configurations file. Edit this before first use.

info.txt

Information as given to BotFather.

jyutpingbot.py

Main script. Run this script to use the bot.

runbot.bat

Batch file to run the script. No difference to running jyutpingbot.py.

## Version History

This section lists all version history.
Dates in parentheses indicate the date this version was pushed onto github.
No date means it was committed locally only.

1.0.1

Updated start, help text

1.0.0 (5/29/20)

Implemented text-to-speech for Jyutping

0.2.1

Added start, help text

Set up base for text-to speech

0.2.0

Implemented JyutPing phrase search

Added Pinyin to JyutPing search results

Added info.txt

Added icon.png

various bugfixes

0.1.0 (5/28/20)

Initial release

Chinese word search, Chinese phrase search, JyutPing word search

Traditional and Simplified Chinese input

Minor bugs/limitations, but working

## License
[GNU GENERAL PUBLIC LICENSE V3](https://choosealicense.com/licenses/gpl-3.0/)

## Third Party Licenses
[Telethon](https://docs.telethon.dev/en/latest/#)

Copyright (c) 2016-2019 LonamiWebs

Telethon is licensed under a MIT License

This program uses the Telethon library.

[CC-CEDICT](https://cc-cedict.org/editor/editor.php?handler=Main)

Copyright (c) 1997, 1998 Paul Andrew Denisowski.

CC-CEDICT is licensed under a Creative Commons Attribution-Share Alike 4.0 License

This program includes files modified from CC-CEDICT.

[CC-CANTO](https://cantonese.org/)

Copyright (c) 2015-16 Pleco Software Incorporated

CC-Canto is licensed under a Creative Commons Attribution-Share Alike 3.0 License

This program includes files modified from CC-Canto.

[CC-CEDICT Cantonese readings](https://cantonese.org/)

Copyright (c) 2015-16 Pleco Software Incorporated

CC-CEDICT Cantonese readings is licensed under a Creative Commons Attribution-Share Alike 3.0 License

This program includes files modified from CC-CEDICT Cantonese readings.

[Ekho](https://www.eguidedog.net/ekho.php)

Copyright (c) 2006 - 2020, eGuideDog team

Ekho is licensed under a GNU GPL v2 License.

This program uses Sound files from Ekho for text to speech.

[Pydub](https://github.com/jiaaro/pydub)

Copyright (c) 2011 James Robert, http://jiaaro.com

Pydub is licensed under a MIT License.

This program uses the Pydub module to parse wav files from Ekho.