from web3 import Web3
import json

# Connect to local Ethereum node
web3 = Web3(Web3.HTTPProvider('http://127.0.0.1:7545'))

# Check if connected to the blockchain
if not web3.is_connected():
    raise Exception("Unable to connect to the blockchain")

print("Connected to blockchain")

# Contract address and ABI (replace with your deployed contract details)
contract_address = '0xd6dc9c963Ec994FB1e0F37dFa0f28AA5b026eCff'
abi = [
	{
		"anonymous": False,
		"inputs": [
			{
				"indexed": False,
				"internalType": "uint256",
				"name": "id",
				"type": "uint256"
			},
			{
				"indexed": False,
				"internalType": "address",
				"name": "owner",
				"type": "address"
			},
			{
				"indexed": False,
				"internalType": "string",
				"name": "projectName",
				"type": "string"
			},
			{
				"indexed": False,
				"internalType": "uint256",
				"name": "amount",
				"type": "uint256"
			}
		],
		"name": "CreditMinted",
		"type": "event"
	},
	{
		"anonymous": False,
		"inputs": [
			{
				"indexed": False,
				"internalType": "uint256",
				"name": "id",
				"type": "uint256"
			},
			{
				"indexed": False,
				"internalType": "address",
				"name": "from",
				"type": "address"
			},
			{
				"indexed": False,
				"internalType": "address",
				"name": "to",
				"type": "address"
			}
		],
		"name": "CreditTransferred",
		"type": "event"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "projectName",
				"type": "string"
			},
			{
				"internalType": "uint256",
				"name": "amount",
				"type": "uint256"
			}
		],
		"name": "mintCredit",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "id",
				"type": "uint256"
			},
			{
				"internalType": "address",
				"name": "to",
				"type": "address"
			}
		],
		"name": "transferCredit",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"name": "credits",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "id",
				"type": "uint256"
			},
			{
				"internalType": "address",
				"name": "owner",
				"type": "address"
			},
			{
				"internalType": "string",
				"name": "projectName",
				"type": "string"
			},
			{
				"internalType": "uint256",
				"name": "amount",
				"type": "uint256"
			},
			{
				"internalType": "bool",
				"name": "isAvailable",
				"type": "bool"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "listAllCredits",
		"outputs": [
			{
				"components": [
					{
						"internalType": "uint256",
						"name": "id",
						"type": "uint256"
					},
					{
						"internalType": "address",
						"name": "owner",
						"type": "address"
					},
					{
						"internalType": "string",
						"name": "projectName",
						"type": "string"
					},
					{
						"internalType": "uint256",
						"name": "amount",
						"type": "uint256"
					},
					{
						"internalType": "bool",
						"name": "isAvailable",
						"type": "bool"
					}
				],
				"internalType": "struct CarbonCredits.CarbonCredit[]",
				"name": "",
				"type": "tuple[]"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "nextCreditId",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	}
]
contract = web3.eth.contract(address=contract_address, abi=abi)

if contract:
    print("Contract loaded successfully!")
else:
    print("Failed to load the contract.")

# Example user account setup (replace with actual private key and account)
private_key = "0x77b286ba815e09a86641f10535c376b874a6250b87f1977829af82af6f5cca3e"
account = web3.eth.account.from_key(private_key)

print(f"Using account: {account.address}")

# Helper to send transactions
def send_transaction(transaction):
    signed_txn = web3.eth.account.sign_transaction(transaction, private_key)
    txn_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
    txn_receipt = web3.eth.wait_for_transaction_receipt(txn_hash)
    print(f"Transaction successful: {txn_receipt.transactionHash.hex()}")

# Function to mint credits
def mint_credit(project_name, volume, price):
    nonce = web3.eth.get_transaction_count(account.address)
    transaction = contract.functions.mintCredit(project_name, volume, price).build_transaction({
        'chainId': web3.eth.chain_id,
        'gas': 300000,
        'gasPrice': web3.to_wei('10', 'gwei'),
        'nonce': nonce
    })
    send_transaction(transaction)

# Function to transfer credit
def transfer_credit(credit_id, to_address):
    nonce = web3.eth.get_transaction_count(account.address)
    transaction = contract.functions.transferCredit(credit_id, to_address).build_transaction({
        'chainId': web3.eth.chain_id,
        'gas': 300000,
        'gasPrice': web3.to_wei('10', 'gwei'),
        'nonce': nonce
    })
    send_transaction(transaction)

# Function to buy credit
def buy_credit(credit_id, payment_amount):
    nonce = web3.eth.get_transaction_count(account.address)
    transaction = contract.functions.buyCredit(credit_id).build_transaction({
        'chainId': web3.eth.chain_id,
        'gas': 300000,
        'gasPrice': web3.to_wei('10', 'gwei'),
        'nonce': nonce,
        'value': payment_amount
    })
    send_transaction(transaction)

# Function to burn expired credits
def burn_expired_credit(credit_id):
    nonce = web3.eth.get_transaction_count(account.address)
    transaction = contract.functions.burnExpiredCredits(credit_id).build_transaction({
        'chainId': web3.eth.chain_id,
        'gas': 300000,
        'gasPrice': web3.to_wei('10', 'gwei'),
        'nonce': nonce
    })
    send_transaction(transaction)

def list_all_credits():
    credits = contract.functions.listAllCredits().call()
    for credit in credits:
        print("ID:", credit[0], "Owner:", credit[1], "Project:", credit[2], "Volume:", credit[3], "Price:", credit[4], "Expiry:", credit[5], "Circulated:", credit[6])

# Example usage
list_all_credits()