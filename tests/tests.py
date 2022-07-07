import sys
sys.path.insert(0, '..')

from bep20 import BEP20Token

BUSD_ADDRESS = "0xe9e7cea3dedca5984780bafc599bd69add087d56"

token = BEP20Token(token_address=BUSD_ADDRESS)

print("Name", token.name())
print("Symbol", token.symbol())
print("Decimals", token.decimals())
