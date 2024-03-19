from web3 import Web3

ganache_url = 'http://127.0.0.1:7545'
web3_ganache_connection = Web3(Web3.HTTPProvider(ganache_url))

Alice_account = '0x8BbD7CC0C9Fad451150dC155bAb78E43aFA1D033' #Enter the account address 1 from your Ganache platform
James_account = '0x467150aC7F7B1effcC77964D0c286bEeabD19cD9' #Enter the account address 2 from your Ganache platform

nonce = web3_ganache_connection.eth.getTransactionCount(Alice_account)
transaction_data = {
    'nonce':nonce,
    'to':James_account,
    'value':web3_ganache_connection.toWei(2, 'ether'),
    'gas':21000, 
    'gasPrice':web3_ganache_connection.toWei(0.000525,'gwei')
}

private_key = 'e9f69bea68ab204b007d8a9010b5c5cf95d6620b2b29a37025cee8da6a87fd33' #Enter the private key of the account address 1 from your Ganache platform
signed_transaction = web3_ganache_connection.eth.account.signTransaction(transaction_data,private_key)
transaction_hash = web3_ganache_connection.eth.sendRawTransaction(signed_transaction.rawTransaction)


print(web3_ganache_connection.toHex(transaction_hash))



