time=int(input("enter your time in seconds:"))
hour=int(time/3600)
minute=int((time/3600-hour)*60)
second=round(((time/3600-hour)*60-minute)*60)
print(hour,":",minute,":",second)