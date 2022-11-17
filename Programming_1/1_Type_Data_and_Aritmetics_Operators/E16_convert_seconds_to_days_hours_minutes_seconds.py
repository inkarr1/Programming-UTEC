seconds = int(input("Segundos: "))

seconds_day = 86400
seconds_hour = 3600
seconds_minute = 60

dd = seconds // seconds_day
seconds = seconds % seconds_day
hh = seconds // seconds_hour
seconds = seconds % seconds_hour
mm = seconds // seconds_minute
ss = seconds % seconds_minute

print("Equivale a: %d:%02d:%02d:%02d" % (dd, hh, mm, ss))