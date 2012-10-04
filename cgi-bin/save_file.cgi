#!/usr/bin/env python
import cgi, os
import cgitb;
cgitb.enable()

try: 
    import msvcrt
    msvcrt.setmode (0, os.O_BINARY) # stdin  = 0
    msvcrt.setmode (1, os.O_BINARY) # stdout = 1
except ImportError:
    pass

form = cgi.FieldStorage()

fileitem = form['file']

if fileitem.filename:
   dir = form.getvalue('dir','Unkown')
   if not dir:
	   dir = '/tmp/'
   fn = os.path.basename(fileitem.filename)
   open( dir + fn, 'wb').write(fileitem.file.read())
   message = 'The file ' + fn + ' was uploaded successfully'
   
else:
   message = 'No file was uploaded'
   
print """\
Content-Type: text/html\n
<html><body>
<p>%s  under %s</p>
</body></html>
""" % (message,dir)
