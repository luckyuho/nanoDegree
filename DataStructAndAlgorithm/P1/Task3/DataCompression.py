

# D	2	000
# B	3	001
# E	6	01
# A	7	10
# C	7	11

# A  A  A  A  A  A  A  B   B   B   C  C  C  C  C  C  C  D   D   E  E  E  E  E  E
# 10 10 10 10 10 10 10 001 001 001 11 11 11 11 11 11 11 000 000 01 01 01 01 01 01

import sys
'''
The building huffman tree node code below is a reference to this website:
https://www.geeksforgeeks.org/huffman-coding-greedy-algo-3/
'''
# A Huffman Tree Node
import heapq
 
class node:
    def __init__(self, freq, symbol, left=None, right=None):
        # frequency of symbol
        self.freq = freq
 
        # symbol name (character)
        self.symbol = symbol
 
        # node left of current node
        self.left = left
 
        # node right of current node
        self.right = right
 
        # tree direction (0/1)
        self.huff = ''
         
    def __lt__(self, nxt):
        return self.freq < nxt.freq
         
 
# utility function to print huffman
# codes for all symbols in the newly
# created Huffman tree
def EncodeNodes(node, encode_dict, val=''):
    if node is None:
        return
     
    # huffman code for current node
    newVal = val + str(node.huff)
 
    # if node is not an edge node
    # then traverse inside it
    # if(node.left):
    EncodeNodes(node.left, encode_dict, newVal)
# if(node.right):
    EncodeNodes(node.right, encode_dict, newVal)
 
    # if node is edge node then
    # save it as dict
    if(not node.left and not node.right):
        if newVal == '':
            newVal = '0'
        encode_dict[node.symbol] = newVal
 
def build_huffman_tree(data):
    record = dict()
    for d in data:
        if d in record:
            record[d] += 1
        else:
            record[d] = 1
    
    record_sorted = dict(sorted(record.items(), key=lambda item: item[1]))
    
    chars = []
    freq = []
    for k in record_sorted:
        chars.append(k)
        freq.append(record_sorted[k])
    
    # list containing unused nodes
    nodes = []
    
    # converting characters and frequencies
    # into huffman tree nodes
    for x in range(len(chars)):
        heapq.heappush(nodes, node(freq[x], chars[x]))
    
    while len(nodes) > 1:
        
        # sort all the nodes in ascending order
        # based on their frequency
        left = heapq.heappop(nodes)
        right = heapq.heappop(nodes)
    
        # assign directional value to these nodes
        left.huff = 0
        right.huff = 1
    
        # combine the 2 smallest nodes to create
        # new node as their parent
        newNode = node(left.freq+right.freq, left.symbol+right.symbol, left, right)
    
        heapq.heappush(nodes, newNode)

    if nodes:
        return nodes[0]
    else:
        return None

def huffman_encoding(data):
    data = str(data)

    nodes = build_huffman_tree(data)
    # Huffman Tree is ready!
    encode_dict = dict()
    EncodeNodes(nodes, encode_dict)

    encode = ''
    for i in data:
        encode += encode_dict[i] 

    return encode, nodes

def DecodeNodes(node, decode_dict, val=''):
    if node is None:
        return 0

    # huffman code for current node
    newVal = val + str(node.huff)
 
    # if node is not an edge node
    # then traverse inside it
    height_l = DecodeNodes(node.left, decode_dict, newVal)
    height_r = DecodeNodes(node.right, decode_dict, newVal)

    # if node is edge node then
    # save it as dict
    
    if(not node.left and not node.right):
        if newVal == '':
            newVal = '0'
        decode_dict[newVal] = node.symbol

    height = max(height_l, height_r) + 1
    return height

def huffman_decoding(data,tree):
    decode_dict = dict()
    max_h = DecodeNodes(tree, decode_dict)

    decode_char = ''
    decoded_data = ''
    for i in data:

        decode_char += i
        if decode_char in decode_dict:
            decoded_data += decode_dict[decode_char]
            decode_char = ''

    try:
        decoded_data = int(decoded_data)
    except ValueError:
            decoded_data

    return decoded_data

def whole_package(a_great_sentence, case):
    print(case)
    print("===============================")
    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)
    
    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))

if __name__ == "__main__":
    # Example
    a_great_sentence = "The bird is the word"
    whole_package(a_great_sentence, "Example")

    # print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    # print ("The content of the data is: {}\n".format(a_great_sentence))

    # encoded_data, tree = huffman_encoding(a_great_sentence)

    # print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    # print ("The content of the encoded data is: {}\n".format(encoded_data))

    # decoded_data = huffman_decoding(encoded_data, tree)

    # print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    # print ("The content of the encoded data is: {}\n".format(decoded_data))

# # Add your own test cases: include at least three test cases
# # and two of them must include edge cases, such as null, empty or very large values

# Test Case 1
a_great_sentence = "AAAAAAABBBCCCCCCCDDEEEEEE"
whole_package(a_great_sentence, "Case1")
# Test Case 2
a_great_sentence = 123
whole_package(a_great_sentence, "Case2")
# Test Case 3
a_great_sentence = " "
whole_package(a_great_sentence, "Case3")