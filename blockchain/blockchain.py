from web3 import Web3
import json

class CarbonCreditMarketplace:
    def __init__(self):
        self.web3 = Web3(Web3.HTTPProvider('HTTP://172.17.80.240:6969'))
        self.contract_address = '0xa5523a57c4fCEfB43eB48a65985A26FD01Bfa346'  # Replace with your contract address
        with open('CarbonCreditMarketplaceABI.json') as f:
            self.contract_abi = json.load(f)
        self.contract = self.web3.eth.contract(address=self.contract_address, abi=self.contract_abi)

    def mint_credit(self, project_name: str, amount: int, price: int, sender_address: str, private_key: str):
        try:
            tx = self.contract.functions.mintCredit(project_name, amount, price).build_transaction({
                'from': sender_address,
                'nonce': self.web3.eth.get_transaction_count(sender_address),
                'gas': 300000,
                'gasPrice': self.web3.to_wei('5', 'gwei')
            })
            
            # Sign and send the transaction
            signed_tx = self.web3.eth.account.sign_transaction(tx, private_key)
            tx_hash = self.web3.eth.send_raw_transaction(signed_tx.rawTransaction)

            return self.web3.to_hex(tx_hash)
        except Exception as e:
            return str(e)

    def list_credit(self, credit_id: int, price: int, sender_address: str, private_key: str):
        try:
            tx = self.contract.functions.listCredit(credit_id, price).build_transaction({
                'from': sender_address,
                'nonce': self.web3.eth.get_transaction_count(sender_address),
                'gas': 300000,
                'gasPrice': self.web3.to_wei('5', 'gwei')
            })
            
            # Sign and send the transaction
            signed_tx = self.web3.eth.account.sign_transaction(tx, private_key)
            tx_hash = self.web3.eth.send_raw_transaction(signed_tx.rawTransaction)

            return self.web3.to_hex(tx_hash)
        except Exception as e:
            return str(e)

    def buy_credit(self, credit_id: int, price: int, buyer_address: str, private_key: str):
        try:
            tx = self.contract.functions.buyCredit(credit_id).build_transaction({
                'from': buyer_address,
                'value': self.web3.to_wei(price, 'wei'),
                'nonce': self.web3.eth.get_transaction_count(buyer_address),
                'gas': 300000,
                'gasPrice': self.web3.to_wei('5', 'gwei')
            })
            
            # Sign and send the transaction
            signed_tx = self.web3.eth.account.sign_transaction(tx, private_key)
            tx_hash = self.web3.eth.send_raw_transaction(signed_tx.rawTransaction)

            return self.web3.to_hex(tx_hash)
        except Exception as e:
            return str(e)

# Test function
def test_mint_and_list_credit():
    blockchain = CarbonCreditMarketplace()
    
    # Account details
    sender_address = '0x8443cdbe2334C4e111C3b0eA5b8Cd904c3E473cc'
    sender_private_key = '0x0cd00e74ffdbb95554ab6a2814047e58bc7c857b22bccb5cdda14d39776876cd'
    
    # Mint a new credit
    mint_tx_hash = blockchain.mint_credit("Test Project", 1000, 500, sender_address, sender_private_key)
    print(f"Mint transaction hash: {mint_tx_hash}")
    
    # List the minted credit
    credit_id = 0  # Assuming this is the first credit minted
    list_tx_hash = blockchain.list_credit(credit_id, 500, sender_address, sender_private_key)
    print(f"List transaction hash: {list_tx_hash}")

# Run the test function
test_mint_and_list_credit()