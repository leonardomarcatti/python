import datetime as dt

agora = dt.datetime.now()
minute = agora.minute
hour = agora.hour
second = agora.second

print(agora)
print(hour)
print(minute)
print(second)

print(dt.date.today())