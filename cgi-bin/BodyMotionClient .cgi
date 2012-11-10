#!/usr/bin/env python

import cgi,os
form = cgi.FieldStorage()
command = form.getvalue("command")
os.system("cd /var/www/motion && ./Body_Motion_Client "+command)
