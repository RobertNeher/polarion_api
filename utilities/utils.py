import requests
from utilities.configuration import Configuration

def polarionRequest(apiEndpoint: str) -> map:
    config = Configuration()
    url = f"{config.schema}://{config.polarionHost}/{config.polarionAPIPrefix}/{apiEndpoint}"
    return  requests.get(url=url,
            params=config.dataFilter,
            headers=config.header
    )
