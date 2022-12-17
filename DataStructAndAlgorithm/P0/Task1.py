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
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
def getDictNumber(Dict, Input):
    length = len(Input)
    for i in range(length):
        for j in range(2):
            key = Input[i][j]
            if key not in Dict:
                Dict[key] = 1
            else:
                Dict[key] += 1
    return Dict

Dict = {}
Dict = getDictNumber(Dict, texts)
Dict = getDictNumber(Dict, calls)

print(f'There are {len(Dict)} different telephone numbers in the records.')

