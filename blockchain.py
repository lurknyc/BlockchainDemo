import hashlib
import json
from time import time
import requests
import Flask from request


class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.pending_transactions = []

        self.new_block(previous_hash="EEDBA33C1B1FF164A1FB3C11E2E8F1051AC5E6A257F717FE7C751BDFF8FF40DA", proof=100)


    def new_block(self, proof, previous_hash=None):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.pending_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }
        self.pending_transactions = []
        self.chain.append(block)

        return block


    @property
    def last_block(self):
 
        return self.chain[-1]


    def new_transaction(self, sender, recipient, amount):
        transaction = {
            'sender': sender,
            'recipient': recipient,
            'amount': amount
        }
        self.pending_transactions.append(transaction)
        return self.last_block['index'] + 1

# receive one block. Turn it into a string, turn that into Unicode (for hashing). Hash with SHA256 encryption, then translate the Unicode into a hexidecimal string.

    def hash(self, block):
        string_object = json.dumps(block, sort_keys=True)
        block_string = string_object.encode()

        raw_hash = hashlib.sha256(block_string)
        hex_hash = raw_hash.hexdigest()

        return hex_hash


blockchain = Blockchain()
t1 = blockchain.new_transaction("Satoshi", "Mike", '5 BTC')
t2 = blockchain.new_transaction("Mike", "Satoshi", '1 BTC')
t3 = blockchain.new_transaction("Satoshi", "Hal Finney", '5 BTC')
blockchain.new_block(12345)

t4 = blockchain.new_transaction("Mike", "Alice", '1 BTC')
t5 = blockchain.new_transaction("Alice", "Bob", '0.5 BTC')
t6 = blockchain.new_transaction("Bob", "Mike", '0.5 BTC')
blockchain.new_block(6789)

print("Genesis block: ", blockchain.chain)
