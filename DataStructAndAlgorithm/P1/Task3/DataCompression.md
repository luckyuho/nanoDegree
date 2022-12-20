# Task 3: Data Compression

### Explanation of code
We use huffman to build a tree according to the frequency of occurrence. Encoding and decoding the data by the huffman tree. We use map in both encoding and decoding methods. First, traverse all elements to get the corresponding symbols and record in the map. After that, we can use the map to encode and decode tha data.
  
### Time and Space Complexity Analysis
The time and space complexity for this program is O(n*log(n)) because it builds a binary tree.

### Result
```python
# # Example
# a_great_sentence = "The bird is the word"
# whole_package(a_great_sentence, "Example")
The size of the data is: 69

The content of the data is: The bird is the word

The size of the encoded data is: 36

The content of the encoded data is: 1000010111011000010011111011110001100111010110101110110101000001111011

The size of the decoded data is: 69

The content of the encoded data is: The bird is the word

# # Test Case 1
# a_great_sentence = "AAAAAAABBBCCCCCCCDDEEEEEE"
# whole_package(a_great_sentence, "Case1")
Case1
===============================
The size of the data is: 74

The content of the data is: AAAAAAABBBCCCCCCCDDEEEEEE

The size of the encoded data is: 32

The content of the encoded data is: 1010101010101000100100111111111111111000000010101010101

The size of the decoded data is: 74

The content of the encoded data is: AAAAAAABBBCCCCCCCDDEEEEEE

# # Test Case 2
# a_great_sentence = 123
# whole_package(a_great_sentence, "Case2")
Case2
===============================
The size of the data is: 28

The content of the data is: 123

The size of the encoded data is: 28

The content of the encoded data is: 10110

The size of the decoded data is: 28

The content of the encoded data is: 123

# # Test Case 3
# a_great_sentence = " "
# whole_package(a_great_sentence, "Case3")
Case3
===============================
The size of the data is: 50

The content of the data is:  

The size of the encoded data is: 24

The content of the encoded data is: 0

The size of the decoded data is: 50

The content of the encoded data is:  

```

### Question
- I have to say, if there is no library "heapq", I really have no idea how to do huffman tree nodes. Is there any instruction?
- Besides, there is a problem in chapt2 Arrays and Linked Lists: 21. swap nodes

```python
Assume linkList: Node(4) → Node(2) → Node(1) → Node(3)

head located at Node(4)

node = head

one_current = node # Node(4)

two_current = node.next # Node(2)

temp = one_current.next # Node(2) → Node(1) → Node(3)
one_current.next = two_current.next # Node(4) → Node(1) → Node(3)
two_current.next = temp # ??? Node(2) → Node(2) ??? what does that mean ?
```