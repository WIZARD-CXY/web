#!/usr/bin/env python

import cgi,os
form = cgi.FieldStorage()
name= form.getvalue("motiondata")
os.system("cd /home/bot5/cxy/ && ./motion_client "+name)
