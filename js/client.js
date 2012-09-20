var xmlHttp
function startMotion(value)
{
if (str.length==0)
  {
  document.getElementById("state").innerHTML=""
  }
xmlHttp=new XMLHttpRequest()
url="/cgi-bin/startMotion.py"
str=str*4+300
url=url+"?motiondata="+"500"+value
xmlHttp.onreadystatechange=stateChanged
xmlHttp.open("get",url,true)
xmlHttp.send()
}
function stateChanged()
{
if (xmlHttp.readyState==4 || xmlHttp.readyState=="complete")
 {
 document.getElementById("state").innerHTML=xmlHttp.responseText
 }
}
