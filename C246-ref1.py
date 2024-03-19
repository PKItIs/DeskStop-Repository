from web3 import Web3
# Connect to the Ethereum network using a provider (e.g., Infura)
web3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/cded6e6690d04259b05137dd10b170c3'))
gas_prices = web3.eth.gas_price
# Calculate gas prices at different levels
current_gas_price = gas_prices()

safe_low_gas_price = int(current_gas_price * 0.9)  # 90% of the current gas price
average_gas_price = int(current_gas_price * 1.0)   # Same as the current gas price
fast_gas_price = int(current_gas_price * 1.1)      # 110% of the current gas price
fastest_gas_price = int(current_gas_price * 1.2)   # 120% of the current gas price
# Convert gas prices from Wei to Gwei
safe_low_gas_price_gwei = web3.fromWei(safe_low_gas_price, 'gwei')
average_gas_price_gwei = web3.fromWei(average_gas_price, 'gwei')
fast_gas_price_gwei = web3.fromWei(fast_gas_price, 'gwei')
fastest_gas_price_gwei = web3.fromWei(fastest_gas_price, 'gwei')
print("Safe Low Gas Price (Gwei):", safe_low_gas_price_gwei)
print(f"Average Gas Price (Gwei):", average_gas_price_gwei)
print(f"Fast Gas Price (Gwei):", fast_gas_price_gwei)
print(f"Fastest Gas Price (Gwei): {fastest_gas_price_gwei}")
# Conversion of gas price into ether and dollars
gas_price = web3.eth.gas_price
current_gas_price1 = gas_price()

print("Gas Price in Gwei", current_gas_price1)
gas_price_in_ether = (current_gas_price1/10**18)
print(f'gas price in ether: {gas_price_in_ether:.22f}')
gas_price_in_dollar = gas_price_in_ether * 3105.35
print("gas price in dollar:",gas_price_in_dollar)