"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
Dict = {}
for i in range(len(calls)):
    for j in range(2):
        key = calls[i][j]
        if key not in Dict:
            Dict[key] = int(calls[i][3])
        else:
            Dict[key] += int(calls[i][3])

maxTime = 0
phoneNumber = ""
for key in Dict:
    if Dict[key] > maxTime:
        phoneNumber = key
        maxTime = Dict[key]

print(f'{phoneNumber} spent the longest time, {maxTime} seconds, on the phone during September 2016.')