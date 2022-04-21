"""
Useful commands lives here
"""

import requests
from .constants import BASE_OS_URL
from requests.models import Response
from web3 import Web3
from .constants import RINKEBY_END_POINT, ERC_721_ABI


def fetch_opensea(contract_address, token_id) -> Response:
    """
    Try to fetch metadata from OpenSea
    :param contract_address (str):
    :param token_id (str):
    :return: ResponseObject
    """
    try:
        url = f"{BASE_OS_URL}{contract_address}/{token_id}"
        opensea_response = requests.request("GET", url)
    except:  #:TODO Return error cause and Log
        opensea_response = requests.models.Response()
        opensea_response.status_code = (
            490  # Dummy status code for Connection Problem between Backend and OpenSea
        )
    return opensea_response


def fetch_blockchain(contract_address, token_id) -> Response:
    """
    Fetch data from blockchain
    :param contract_address:(str)
    :param token_id:(str)
    :return: ResponseObject
    """
    expected_response = Response()
    web3 = Web3(Web3.HTTPProvider(RINKEBY_END_POINT))
    # TODO: Figure out which category this address fits in
    contract = web3.eth.contract(address=contract_address, abi=ERC_721_ABI)
    name = contract.functions.name().call()
    symbol = contract.functions.symbol().call()
    metadata = contract.functions.tokenURI(token_id).call()
    # TODO: Decode the URI and fetch required metadata
    # TODO: Create the response object based on data
    return expected_response
