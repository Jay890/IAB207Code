from datetime import date, datetime

# datetime(year, month, day)
a = datetime(2020, 8, 27, 23, 20, 59, 343433)
b = datetime(2020, 8, 27, 22, 55, 59, 343433)
print(a)

# We can also print seperate properties like
# print(a.year)

# timedelta is the difference between two datetime() values

delta = a - b
# print(delta)

# In python delta only provide days, seconds and microseconds
# If we wanted minutes we would have to do some calculations

minutes_between = delta.seconds / 60
print("Time difference is ", minutes_between, " minutes.")


# We can also format dates to be more human readable
# Using the strftime - which takes string with special characters
# Then it will find and replace the correct value of the time with the characters e.g. "%d, %m, &Y, %h, %M, %S"
print(a.strftime("%d, %m, %Y, %H:%M:%S"))
