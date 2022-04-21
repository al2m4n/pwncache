import datetime
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .constants import BASE_OS_URL, MAX_CACHE_AGE
from .parsers import parse_opensea
from .commands import fetch_opensea
from .models import Asset


@api_view(["GET"])
def retrieve_asset(request, contract_address, token_id):
    """
    1. Fetch data from OPENSEA TestNets
    2. If received update/create Cache and return to USER
    3. Search Cache and check Cache Validity and return to USER
    4.Fetch data from blockchain and return to USER
    :param request:
    :param contract_address: (str)
    :param token_id: (str)
    :return: Response to User
    """
    lcontract_address = contract_address.lower()
    opensea_response = fetch_opensea(contract_address, token_id)
    if opensea_response.status_code == 200:  # OpenSea is working and returned our data
        parsed_data = parse_opensea(
            opensea_response.json()
        )  # Parse according to required fields
        obj, created = Asset.objects.update_or_create(
            contract_address=lcontract_address,
            token_id=token_id,
            defaults=parsed_data,
        )  # Update existing cache or create if not exist
        parsed_data.pop("contract_address")
        parsed_data.pop("token_id")
        response = Response(parsed_data)
        response["Source"] = "OpenSea"  # Add Header for debug
        return response
    queryset = Asset.objects.filter(
        contract_address=lcontract_address, token_id=token_id
    )
    if queryset:  # Found in cache
        datetime_updated = queryset.values("update_date")[0]["update_date"]
        datetime_now = datetime.datetime.now()
        if (
            datetime_now.timestamp() < datetime_updated.timestamp() + MAX_CACHE_AGE
        ):  # Cache is Valid
            response = Response(
                queryset.values(
                    "category",
                    "decimals",
                    "thumbnail_url",
                    "animation_url",
                    "name",
                    "contract_name",
                    "symbol",
                )[0]
            )
            response["Source"] = "Cache"  # Add Header for debug
            response.data["is_verified"] = None
            return response
    # TODO: fetch data from blockchain and call fetch_blockchain function from commands
    return Response("Nothing Worked !")
