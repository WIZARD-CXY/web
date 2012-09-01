#!/bin/sh

echo  "Content-type: text/html"
echo  ""
killall mjpg_streamer 

echo "<html><head></head>"  
echo "<body>"
echo "<h1>The monitor has been killed !</h1>"
echo "</body></html>"
