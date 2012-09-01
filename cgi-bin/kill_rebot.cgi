#!/bin/sh

echo  "Content-type: text/html"
echo  ""
killall rebot

echo "<html><head></head>"  
echo "<body>"
echo "<h1>The rebot has been killed !</h1>"
echo "</body></html>"
