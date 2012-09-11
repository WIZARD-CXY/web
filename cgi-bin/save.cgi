#!/usr/bin/env python

print "Content-type: text/html\n"

import cgi ,sha,sys

form = cgi.FieldStorage()

text = form.getvalue('text')
filename = form.getvalue('filename')
password = form.getvalue('password')

if not ( filename and text and password):
	print "You are missing something!"
	sys.exit()

if sha.sha(password).hexdigest() != '637d1f5c6e6d1be22ed907eb3d223d858ca396d8':
	print "Invalid Password"
	sys.exit()
f=open('/home/bot5/yuling/configure/'+filename,'w')
f.write(text)
f.close()
print "The file has been saved"
