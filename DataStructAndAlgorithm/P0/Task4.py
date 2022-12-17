"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""
outgoing = set()
non_tele = set()

for call in calls:
    outgoing.add(call[0])
    non_tele.add(call[1])

def getCallsNumber(Set):
    for phone in non_tele:
        Set.add(phone)
    return Set

def getTextNumber(Set):
    length = len(texts)
    for i in range(length):
        for j in range(2):
            phone = texts[i][j]
            Set.add(phone)
    return Set

nonTele = set()
nonTele = getCallsNumber(nonTele)
nonTele = getTextNumber(nonTele)

def possibleTelemarketers(Set):
    PosTelMar = set()
    for phone in outgoing:
        if phone not in Set:
            PosTelMar.add(phone)
    return PosTelMar

posTelMar = possibleTelemarketers(nonTele)
posTelMar = sorted(posTelMar)

print(f'These numbers could be telemarketers:')
for i in posTelMar:
    print(f'{i}')


