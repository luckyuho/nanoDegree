import hashlib
from datetime import datetime


class Block:
    def __init__(self, timestamp, data=None, previous_hash=None):
      self.timestamp = timestamp
      self.data = data
      self.previous_hash = previous_hash
      self.hash = self.calc_hash()
      self.next = None

    def calc_hash(self):
      sha = hashlib.sha256()
      if self.data is None:
        self.data = ""
      hash_str = (str(self.data) + str(self.timestamp)).encode('utf-8')
      sha.update(hash_str)
      return sha.hexdigest()

class BlockLinkList(Block):
    def __init__(self, data=None):
        _block = Block(datetime.now(), data, 0)
        self.head = _block
        self.tail = self.head

    def create_block(self, data=None):
        _block = Block(datetime.now(), data, self.tail.hash)
        self.tail.next = _block
        self.tail = self.tail.next

    def print_block_chain(self):
        current = self.head

        print("------ head ------")
        while current:    
            print("timestamp:", current.timestamp)
            print("data:", current.data)
            print("hash:", current.hash)
            print("previous_hash:", current.previous_hash)

            current = current.next

            if current:
                print("------ v ------")
            else:
                print("------ tail ------")


# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values
block = BlockLinkList("Hello, block chain")
block.print_block_chain()

# Test Case 1
block.create_block(None)
block.print_block_chain()

# Test Case 2
block.create_block(1314)
block.print_block_chain()
# Test Case 3
block.create_block()
block.print_block_chain()