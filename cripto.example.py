from web3 import Web3

RPC_URL = "https://mainnet.base.org"

w3 = Web3(Web3.HTTPProvider(RPC_URL))

private_key = "YOUR_PRIVATE_KEY"
sender = "0xYourAddress"
receiver = "0xReceiverAddress"

nonce = w3.eth.get_transaction_count(sender)

tx = {
    "nonce": nonce,
    "to": receiver,
    "value": w3.to_wei(0.001, "ether"),
    "gas": 21000,
    "gasPrice": w3.eth.gas_price,
    "chainId": 8453
}

signed_tx = w3.eth.account.sign_transaction(tx, private_key)

tx_hash = w3.eth.send_raw_transaction(signed_tx.raw_transaction)

print("Transaction Hash:", tx_hash.hex())
