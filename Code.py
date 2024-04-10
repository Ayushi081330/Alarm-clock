import datetime

current_time = datetime.datetime.now()
hour = current_time.hour

if 0 <= hour < 12:
     print("Suprabhat")
elif 12 <= hour < 18:
     print("Din")
elif 18 <= hour < 24:
     print("Shaam ya Ratri")
else:
     print("Kripiya sahi samay daale")
