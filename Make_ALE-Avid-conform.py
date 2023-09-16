#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Check ALE file (AvidLogExchange) for known issues that might cause problems when imported into Avid-Media-Composer (=> AMC) and fix them:
This is primarily targeted to ALE's that have been generated in third party tools (Silverstack, DaVinci-Resolve...) and not by Avid-Software.

Issues:
1. Character limit:
Plenty Version of AMC crash if an ALE with more than 250 characters in one Metadata field is imported.
This script will find those fields cut them down to 247 characters and attach the suffix "..." to give a hint that data had to be cut off.

2. German-Umlaut
Plenty Version of AMC struggle with special german characters like "ö, ä, ü, ß".
This script will fix those.

Issue missing?
Feel free to get in touch via github to request further ALE-conforming
=> https://github.com/swdit/Make_ALE-Avid-conform/issues
"""


import ALE_Parser as alp # custom modul can be found here https://github.com/swdit/ALE-Parser.git

# Path to ALE file <- Change this to your ALE file
ale_path = "your/path/testfile.ale"
dst_pathname = "your/path/newfile.ale"

# Read your ale file into a pandas dataframe and a headerdict
headerdict, df = alp.ale_read_parser(ale_path)


# Replace German Umlauts in all fields
df = df.replace({'Ä': 'Ae'})
df = df.replace({'ä': 'ae'})
df = df.replace({'Ö': 'Oe'})
df = df.replace({'ö': 'oe'})
df = df.replace({'Ü': 'Ue'})
df = df.replace({'ü': 'ue'})
df = df.replace({'ß': 'ss'})


# Limit Number of characters per field to 250
def limit_characters(value):
    if isinstance(value, str):
        if len(value) > 250:
            return value[:247] + "..."
        else:
            return value
    else:
        return value

df = df.applymap(limit_characters)


# Write your pandas dataframe to an ALE file
alp.ale_write_parser(df, headerdict, dst_pathname)

