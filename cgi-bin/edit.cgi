#!/usr/bin/env python

import cgi, sys,cgitb
cgitb.enable()

print "Content-type: text/html\n"

form = cgi.FieldStorage()
filename=form.getvalue('filename')
if not filename:
	print "Please Enter a valid filename"
	sys.exit()

text=open('/home/bot5/yuling/configure/'+filename).read()

print """
<html>
<head>
<title>Editing robot parameters</title>
</head>
<body>
<form action='save.cgi' method='POST'>
<b>File: </b>%s<br />
<input type='hidden' value='%s' name='filename'/>
<b>Password:</b><br />
<input name='password' type='password' /><br />
<b>Text : </b><br />
<textarea name='text' cols ='60' rows='30'>%s</textarea><br />
<input type='submit' value='Save' />
</form>
</body>
</html>
""" % (filename,filename,text)
