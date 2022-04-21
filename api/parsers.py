"""
Parse Functions and Classes lives here
"""


def parse_opensea(data) -> dict:
    """
    Custom Parser for Parsing the OpenSea Response
    and remove unnecessary items
    :param data (dict):
    :return (dict):
    """
    parsed_data = {}
    parsed_data["contract_address"] = data["asset_contract"]["address"]
    parsed_data["token_id"] = data["token_id"]
    parsed_data["category"] = data["asset_contract"]["schema_name"]
    parsed_data["decimals"] = data["decimals"]
    parsed_data["thumbnail_url"] = data["image_thumbnail_url"]
    parsed_data["animation_url"] = data["animation_url"]
    parsed_data["name"] = data["name"]
    parsed_data["contract_name"] = data["asset_contract"]["name"]
    parsed_data["symbol"] = data["asset_contract"]["symbol"]
    if data["collection"]["safelist_request_status"] == "verified":
        parsed_data["is_verified"] = True
    else:
        parsed_data["is_verified"] = False
    return parsed_data
