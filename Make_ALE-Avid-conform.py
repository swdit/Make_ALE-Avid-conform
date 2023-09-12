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


import pandas
