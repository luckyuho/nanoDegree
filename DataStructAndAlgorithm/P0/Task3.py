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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore. In other words, the calls were initiated by "(080)" area code
to the following area codes and mobile prefixes:
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""
FixedLine = 1
Mobile = 2
TeleMarketer = 3

def DistinguishCodes(phone): # type, prefix
  phone = phone.replace(" ", "")
  # type 1
  if phone[0:2] == "(0":
    end = phone.find(')')
    return FixedLine, phone[1:end]
  # type 2
  mobilePrefix = {7, 8, 9}
  if int(phone[0]) in mobilePrefix:
    return Mobile, phone[0:4]
  # type 3
  if phone[0:3] == '140':
    return TeleMarketer, '140'

# PartA
PhoneList = set()
for i in range(len(calls)):
  own = calls[i][0]
  
  if own[0:5] == '(080)':
    call = calls[i][1]
    _, prefix = DistinguishCodes(call)
    
    if prefix not in PhoneList:
      PhoneList.add(prefix)

PhoneList = sorted(PhoneList)
print(f'The numbers called by people in Bangalore have codes:' )
for i in PhoneList:
  print(f'{i}' )

# PartB
counter = 0
total = 0
for i in range(len(calls)):
  own = calls[i][0]
  
  if own[0:5] == '(080)':
    total += 1
    call = calls[i][1]
    _, prefix = DistinguishCodes(call)
    
    if prefix == '080':
      counter += 1

percent = "{:.2f}".format(counter / total * 100)
print(f'{percent} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.')

