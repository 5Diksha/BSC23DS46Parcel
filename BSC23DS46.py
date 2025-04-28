# BSc23DS46
import hashlib
import datetime

class Block:
    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        sha = hashlib.sha256()
        sha.update(str(self.timestamp).encode('utf-8') + 
                   str(self.data).encode('utf-8') + 
                   str(self.previous_hash).encode('utf-8'))
        return sha.hexdigest()

class Blockchain:
    def __init__(self):
        self.genesis_block = Block(datetime.datetime.now(), "Genesis Block", "0")
        self.chain = [self.genesis_block]

    def add_block(self, data):
        previous_block = self.chain[-1]
        new_block = Block(datetime.datetime.now(), data, previous_block.hash)
        self.chain.append(new_block)

    def is_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i-1]
            if current_block.hash != current_block.calculate_hash():
                return False
            if current_block.previous_hash != previous_block.hash:
                return False
        return True

# Create a blockchain instance
blockchain = Blockchain()

# Add parcel tracking data
blockchain.add_block({"parcel_id": "1234567890", "status": "Picked up"})
blockchain.add_block({"parcel_id": "1234567890", "status": "In transit"})
blockchain.add_block({"parcel_id": "1234567890", "status": "Delivered"})

# Verify the blockchain integrity
print(blockchain.is_valid())  # Output: True

# Print the blockchain data (for demonstration purposes)
for block in blockchain.chain:
    print(block.data)
