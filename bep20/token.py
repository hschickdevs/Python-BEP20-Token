from .util import get_contract_instance, network_rpc_url

class BEP20Token:
    def __init__(self, token_address: str, network_rpc_url: str):
        self.contract = get_contract_instance(token_address, "BEP20Token.json")

    def name(self):
        return self.contract.functions.name().call()
    
    def symbol(self):
        return self.contract.functions.symbol().call()
    
    def decimals(self):
        return self.contract.functions.decimals().call()
    
    
"""
5.1.1 Methods
5.1.1.1 name
5.1.1.2 symbol
5.1.1.3 decimals
5.1.1.4 totalSupply
5.1.1.5 balanceOf
5.1.1.6 getOwner
5.1.1.7 transfer
5.1.1.8 transferFrom
5.1.1.9 approve
5.1.1.10 allowance
"""
