#To run from Terminal: python3 good.py
name = str(input("Please enter your name: "))

import datetime
now = datetime.datetime.now()
hour = now.hour

if 3 <= hour < 9:
    tod = 'morning'
elif 9 <= hour < 15:
    tod = 'day'
elif 15 <= hour < 21:
    tod = 'evening'
else:
    tod = 'night'

message = f"Hello {name}! Good {tod}!"
# message_raw = r"Hello {name}! Good {tod}!\n"
# message = "Hello {}! Good {}!".format(name, tod)
# message = "Hello %s! Good %s!" % (name, tod)
print(message)
# print(message_raw)