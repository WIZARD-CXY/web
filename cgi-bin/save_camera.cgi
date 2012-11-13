#!/usr/bin/env python

import cgi

form = cgi.FieldStorage()


text = "saturation: "                  
text = text+form.getvalue('saturation')     
text = text+"\n"

text = text+"contrast: "                  
text = text+form.getvalue('contrast')     
text = text+"\n" 

text = text+"brightness: "                  
text = text+form.getvalue('brightness')     
text = text+"\n" 

text = text+"hue: "                  
text = text+form.getvalue('hue')     
text = text+"\n" 

text = text+"gamma: "                  
text = text+form.getvalue('gamma')     
text = text+"\n"                   
                                       
text = text+"gain: "                   
text = text+form.getvalue('gain')      
text = text+"\n"
                                       
text = text+"sharpness: "              
text = text+form.getvalue('sharpness') 
text = text+"\n"                     
                                       
text = text+"whitebalance: "           
text = text+form.getvalue('whiteauto') 
text = text+"\n"

text = text+"exposureauto: "                  
text = text+form.getvalue('exposureauto')     
text = text+"\n" 

text = text+"exposure: "                  
text = text+form.getvalue('exposure')     
text = text+"\n" 

text = text+"white_balance_temperature: "                  
text = text+form.getvalue('white')     
text = text+"\n" 

f=open('a.txt','w')
f.write(text)
f.close()

print "The file has been saved"