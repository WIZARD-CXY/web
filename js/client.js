var xmlHttp
function startMotion(value)
{
xmlHttp=new XMLHttpRequest()
url="/cgi-bin/startMotion.cgi"
value=value*4+300
url=url+"?motiondata="+"500"+value
xmlHttp.open("get",url,true)
xmlHttp.send()
}
