# Runtime Analysis

### Task 5: Blockchain
- Worst-case time complexity is O(n).
- The time complexity for this program is O(n) because the length of our cache array is a fixed capacity.
  
```python
# block = BlockLinkList("Hello, block chain")
# block.print_block_chain()
------ head ------
timestamp: 2022-12-17 23:05:46.060858
data: Hello, block chain
hash: 9a0edf6d6d8f8b9a3088500b213b02a85a191670aa3ed3cd13d6c815386a636e
previous_hash: 0
------ tail ------

# # Test Case 1
# block.create_block(None)
# block.print_block_chain()
------ head ------
timestamp: 2022-12-17 23:05:46.060858
data: Hello, block chain
hash: 9a0edf6d6d8f8b9a3088500b213b02a85a191670aa3ed3cd13d6c815386a636e
previous_hash: 0
------ v ------
timestamp: 2022-12-17 23:05:46.060900
data: 
hash: 7acaa58d5c22f46230890a51d1d7f3edccdbfc56998a9830854f2e0dd41662df
previous_hash: 9a0edf6d6d8f8b9a3088500b213b02a85a191670aa3ed3cd13d6c815386a636e
------ tail ------

# # Test Case 2
# block.create_block(1314)
# block.print_block_chain()
------ head ------
timestamp: 2022-12-17 23:05:46.060858
data: Hello, block chain
hash: 9a0edf6d6d8f8b9a3088500b213b02a85a191670aa3ed3cd13d6c815386a636e
previous_hash: 0
------ v ------
timestamp: 2022-12-17 23:05:46.060900
data: 
hash: 7acaa58d5c22f46230890a51d1d7f3edccdbfc56998a9830854f2e0dd41662df
previous_hash: 9a0edf6d6d8f8b9a3088500b213b02a85a191670aa3ed3cd13d6c815386a636e
------ v ------
timestamp: 2022-12-17 23:05:46.060920
data: 1314
hash: 65f9d8287382c6b81203c05a783b575b2179583ccfbe8a1fb1a948dccd07fbc7
previous_hash: 7acaa58d5c22f46230890a51d1d7f3edccdbfc56998a9830854f2e0dd41662df
------ tail ------

# # Test Case 3
# block.create_block()
# block.print_block_chain()
------ head ------
timestamp: 2022-12-17 23:05:46.060858
data: Hello, block chain
hash: 9a0edf6d6d8f8b9a3088500b213b02a85a191670aa3ed3cd13d6c815386a636e
previous_hash: 0
------ v ------
timestamp: 2022-12-17 23:05:46.060900
data: 
hash: 7acaa58d5c22f46230890a51d1d7f3edccdbfc56998a9830854f2e0dd41662df
previous_hash: 9a0edf6d6d8f8b9a3088500b213b02a85a191670aa3ed3cd13d6c815386a636e
------ v ------
timestamp: 2022-12-17 23:05:46.060920
data: 1314
hash: 65f9d8287382c6b81203c05a783b575b2179583ccfbe8a1fb1a948dccd07fbc7
previous_hash: 7acaa58d5c22f46230890a51d1d7f3edccdbfc56998a9830854f2e0dd41662df
------ v ------
timestamp: 2022-12-17 23:05:46.061007
data: 
hash: 67d7aa7c946a9b3a8c7eb23def2143ebf4f82939cbad7cd943c73eafee62e5f6
previous_hash: 65f9d8287382c6b81203c05a783b575b2179583ccfbe8a1fb1a948dccd07fbc7
------ tail ------
```