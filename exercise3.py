from hashlib import sha256
import json
import time
import requests
import random
import string
import copy


class Block:
    def __init__(self, index, transactions, timestamp, previous_hash):

        self.index = index
        self.transactions = transactions
        self.timestamp = timestamp
        self.previous_hash = previous_hash # Adding the previous hash field

    def compute_hash(self):
        block_string = json.dumps(self.__dict__, sort_keys=True)
        return sha256(block_string.encode()).hexdigest()


response = requests.get('https://raw.githubusercontent.com/tygerprotocol/tp-test/master/testblock.json')
amount = []
address = []
if response.status_code == 200:
    raw_data = response.json()
    index = raw_data['BlockIndex']
    timestamp = raw_data['TimeStamp']
    prev_hash = raw_data['PrevHash']
    nonce = raw_data['Nonce']
    transactions = raw_data['Transactions']

    # Create new transactions
    new_transactions = copy.deepcopy(transactions)
    for i in range(len(transactions)):
        temp1 = transactions[i][0]
        kk1 = temp1.replace("'", '"')
        result1 = json.loads(kk1)

        temp2 = new_transactions[i][0]
        kk2 = temp2.replace("'", '"')
        result2 = json.loads(kk2)
        transactions[i][0] = result1
        new_transactions[i][0] = result2
        new_amount = random.random()
        count = random.randrange(1, 10)
        address1 = ''.join(random.choices(string.ascii_uppercase + string.digits, k=count))
        address2 = ''.join(random.choices(string.ascii_uppercase + string.digits, k=count))
        new_send_address = sha256(address1.encode()).hexdigest()
        new_recp_address = sha256(address2.encode()).hexdigest()
        new_transactions[i][0]['Amount'] = new_amount
        new_transactions[i][0]['SenderAddress'] = new_send_address
        new_transactions[i][0]['RecipientAddress'] = new_recp_address

    block1 = Block(index, transactions, timestamp, prev_hash)
    hash1 = block1.compute_hash()
    block2 = Block(index+1, new_transactions, time.time(), hash1)
    print(json.dumps(block1.__dict__))
    print(json.dumps(block2.__dict__))
else:
    print('An error occurred while attempting to retrieve data from the API.')