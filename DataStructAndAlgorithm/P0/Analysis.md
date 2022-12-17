# Runtime Analysis

### Task 0: print list first and last messages
- Worst-case time complexity is O(1).
- The time complexity for this program is O(1) because we only access the first and last values from the lists by an index.
  
```
First record of texts, 97424 22395 texts 90365 06212 at time 01-09-2016 06:03:22
Last record of calls, 98447 62998 calls (080)46304537 at time 30-09-2016 23:57:15, lasting 2151 seconds
```

### Task 1: show different phone number among the lists
- Worst-case time complexity is O(n).
- The time complexity for this program is O(n), the actual time complexity is O(2n*2), because we have to access sender and receiver from both lists (calls and texts).

```
There are 570 different telephone numbers in the records.
```

### Task 2: find out who spend the longest time during the period and how much time

- Worst-case time complexity is O(n).
- The time complexity for this program is O(n), because we have to access sender and receiver from calls.
- We use dict to record the time is taken by each phone and use another for loop to find out our winner.

```
(080)33251027 spent the longest time, 90456 seconds, on the phone during September 2016.
```

### Task 3: 
#### PartA: find out whom called by people in Bangalore

- Worst-case time complexity is O(nlogn).
- The time complexity for this program is O(nlogn), the actual time complexity is O(n) + O(nlogn) + O(n), because we have to access caller: O(n) and sorted the data: O(nlogn) and print data: O(n).

```
The numbers called by people in Bangalore have codes:
022
040
04344
044
04546
0471
080
0821
7406
7795
7813
7829
8151
8152
8301
8431
8714
9008
9019
9035
9036
9241
9242
9341
9342
9343
9400
9448
9449
9526
9656
9738
9740
9741
9742
9844
9845
9900
9961
```

#### PartB: show the percentage of receiver in Bangalore when caller is in Bangalore

- Worst-case time complexity is O(n).
- The time complexity for this program is O(n), because we have to access caller and get receiver when caller is in Bangalore from calls.

```
24.81 percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.
```

### Task 4: find out who is possible telemarketer

- Worst-case time complexity is O(nlogn).
- The time complexity for this program is O(nlogn), because we have to access sender and receiver from both lists (calls and texts).
- We use dict to record the receivers and text relative phone number, because possible telemarketers are callers and probably not the receivers and text relative phone number. We can save those caller phone number not in these situations as possible telemarketers.

```
These numbers could be telemarketers:
(022)37572285
(022)65548497
(022)68535788
(022)69042431
(040)30429041
(044)22020822
(0471)2171438
(0471)6579079
(080)20383942
(080)25820765
(080)31606520
(080)40362016
(080)60463379
(080)60998034
(080)62963633
(080)64015211
(080)69887826
(0821)3257740
1400481538
1401747654
1402316533
1403072432
1403579926
1404073047
1404368883
1404787681
1407539117
1408371942
1408409918
1408672243
1409421631
1409668775
1409994233
74064 66270
78291 94593
87144 55014
90351 90193
92414 69419
94495 03761
97404 30456
97407 84573
97442 45192
99617 25274
```
