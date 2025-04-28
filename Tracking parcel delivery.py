import streamlit as st
import hashlib
import datetime

# Blockchain implementation
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

# Streamlit app
def main():
    st.title("Blockchain Parcel Tracking")
    
    # Create a blockchain instance
    blockchain = Blockchain()

    st.header("Add Parcel Tracking Information")
    parcel_id = st.text_input("Enter Parcel ID", "")
    status = st.text_input("Enter Parcel Status", "")

    if st.button("Add Parcel Tracking Data"):
        if parcel_id and status:
            data = {"parcel_id": parcel_id, "status": status}
            blockchain.add_block(data)
            st.success("Parcel tracking data added successfully!")
        else:
            st.error("Please provide both Parcel ID and Status.")

    st.header("Blockchain Integrity Check")
    if st.button("Check Blockchain Validity"):
        is_valid = blockchain.is_valid()
        if is_valid:
            st.success("Blockchain is valid!")
        else:
            st.error("Blockchain is not valid!")

    st.header("Blockchain Data")
    for block in blockchain.chain:
        st.subheader(f"Block {block.timestamp}")
        st.write(f"Data: {block.data}")
        st.write(f"Hash: {block.hash}")
        st.write(f"Previous Hash: {block.previous_hash}")
        st.write("-" * 80)

if __name__ == "__main__":
    main()
