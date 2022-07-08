import json
from os.path import join, dirname
from os import getcwd

from web3 import Web3
import web3
import requests

ABI_DIR = join(dirname(__file__), "abi")


def get_web3_provider(network_rpc_url: str) -> Web3:
    return Web3(Web3.HTTPProvider(network_rpc_url))


def get_contract_instance(abi_filename: str, contract_address: str, w3_provider: Web3 = None):
    if w3_provider is None:
        w3_provider = get_web3_provider("https://bsc-dataseed.binance.org/")
        
    with open(join(ABI_DIR, abi_filename), 'r') as abi_file:
        return w3_provider.eth.contract(abi=json.load(abi_file),
                                        address=Web3.toChecksumAddress(contract_address))
    
    
def store_abi(abi_url: str, abi_filename: str) -> None:
    """
    Format and store a smart contract ABI in JSON locally

    :param abi_url: NETWORK SCAN -> Export ABI -> RAW/Text Format -> Get the URL
                    (ex. "http://api.etherscan.io/api?module=contract&action=getabi&address=0xc4a59cfed3fe06bdb5c21de75a70b20db280d8fe&format=raw")
    :param abi_filename: The desired filename for local storage
    """
    contract_abi = requests.get(abi_url).json()
    path = join(join(dirname(__file__)), "abi", abi_filename)
    with open(path, "w") as json_file:
        json_file.write(json.dumps(contract_abi, indent=2))


def checksum(address: str):
    return Web3.toChecksumAddress(address)
