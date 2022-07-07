from .util import get_contract_instance, checksum


class BEP20Token:
    """https://github.com/bnb-chain/BEPs/blob/master/BEP20.md"""

    def __init__(self, token_address: str, network_rpc_url: str):
        self.contract = get_contract_instance(network_rpc_url,
                                              abi_filename="BEP20.json",
                                              contract_address=token_address)

    def name(self) -> str:
        """Returns the name of the token - e.g. 'MyToken'."""
        return self.contract.functions.name().call()

    def symbol(self) -> str:
        """Returns the symbol of the token. E.g. “HIX”."""
        return self.contract.functions.symbol().call()

    def decimals(self) -> int:
        """
        Returns the number of decimals the token uses.
        E.g. 8, means to divide the token amount by 100000000 to get its user representation.
        """
        return self.contract.functions.decimals().call()

    def totalSupply(self) -> int:
        """
        Returns the total token supply. If the token will flow across the Binance Chain and Binance Smart Chain, 
        the number should be the total of circulation across 2 blockchains.
        """
        return self.contract.functions.totalSupply().call()

    def balanceOf(self, _owner: str) -> int:
        """Returns the account balance of an account with address _owner."""
        return self.contract.functions.balanceOf(checksum(_owner)).call()

    def getOwner(self):
        raise NotImplementedError

    def transfer(self, _to: str, _value: int):
        """Transfers _value of the token to _to."""
        raise NotImplementedError

    def transferFrom(self, _from: str, _to: str, _value: int):
        """Transfers _value amount of tokens from address _from to address _to"""
        raise NotImplementedError

    def approve(self, _spender: str, _value: str):
        """
        Allows _spender to withdraw from your account multiple times, up to the _value amount.
        If this function is called again it overwrites the current allowance with _value.
        """
        raise NotImplementedError

    def allowance(self, _owner: str, _spender: str) -> int:
        """Returns the amount which _spender is still allowed to withdraw from _owner"""
        return self.contract.functions.allowance(_owner, _spender).call()
