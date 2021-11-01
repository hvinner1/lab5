#!/usr/bin/python37all
import cgi
import json

data = cgi.FieldStorage()

#json code
ang = data.getvalue('angle')
submit = data.getvalue('Change Angle')
zero = data.getvalue('Zero')
#do we need to getvalue from each button
data = {"angle":ang, "sumbit":submit, "zero":zero}
with open('lab5.txt', 'w') as f:
  json.dump(data,f)

print('Content-type: text/html\n\n')
print('''
<html>
<form action="/cgi-bin/stepper.py" method="POST">
  <input type="range" id="angle" name="angle" min="0" max="1000">
  <label for="angle">Volume</angle><br>
  <br>
  <input type="submit" value="Change Angle">
  <input type="submit" value="Zero">
</form>
<iframe width="450" height="260" style="border: 1px solid #cccccc;" src="https://thingspeak.com/channels/1550818/charts/1?bgcolor=%23ffffff&color=%23d62020&dynamic=true&results=60&type=line&xaxis=time&yaxis=motor+angle"></iframe><br>
<iframe width="450" height="260" style="border: 1px solid #cccccc;" src="https://thingspeak.com/channels/1550818/widgets/372978"></iframe>
</html>
''')
