import requests

class GoogleAddressQuery:
    """
    Creates an address query to interact with the 
    Google geocoding API.
    """

    url = "https://maps.googleapis.com/maps/api/geocode/json"

    def __init__(self, query, key):
        self.query = query
        self.key = key
        params = {'address':self.query, 'key': self.key}
        r = requests.get(self.url, params = params)
        self.addresses = r.json()["results"]
        self.status = r.json()["status"]

    def num_addresses(self):
        return len(self.addresses)

    def exact_match_exists(self):
        """
        Returns true if at least one address is not a partial
        match (so presumably exact) and at least one address returned
        from the query..
        """

        if self.num_addresses() == 0:
            return False

        for address in self.addresses:
            if "partial_match" in address and address["partial_match"] == True:
                return False
        return True

class GoogleAddress:
    """
    An individual address returned from Google Geocode API.
    """

    def __init__(self, **kwargs):
        self.formatted_address = kwargs["formatted_address"]
        self.address_components = kwargs["address_components"]

        if "partial_match" in kwargs:
            self.partial_match = kwargs["partial_match"]
        else:
            self.partial_match = False



class GoogleAddresses:
    """
    Collection of GoogleAddress
    """


