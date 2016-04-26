def get_google_api_key():
    with open("/Users/macbook/Desktop/Mark Nagelberg/address-validation/address_validator/google_api_key") as f:
        key = f.read().strip()
    return key

#Tests for GoogleAddressQuery class
def test_url():
    key = get_google_api_key()
    assert GoogleAddressQuery.url == "https://maps.googleapis.com/maps/api/geocode/json"

def test_returning_results():
    key = get_google_api_key()
    query = GoogleAddressQuery(query = "3 Warrendale Pl. Winnipeg MB Canada",
                               key = key)
    assert query.addresses.num_addresses()  > 0

#Tests for GoogleAddress class
def test_postal_code():
    key = get_google_api_key()
    query = GoogleAddressQuery(query = "390 Rosedale Ave. Winnipeg MB Canada",
                               key = key)
    assert query.addresses.get_address(0).get_postal_code() == "R3L 1M2"

import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
from address_validator.address_validate import GoogleAddressQuery


