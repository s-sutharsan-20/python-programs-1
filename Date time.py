from datetime import datetime

today=datetime.today()
date=today.date()
hour=today.hour
minute=today.minute
second=today.second

print("Date :",date,"(YYYY-MM-DD)")
print("Time :",hour,":",minute,":",second)


