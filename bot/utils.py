from constants import HEADERS
import requests

def request(url: str, **kwargs: any) -> requests.Response:
    return requests.get(
        f"{url}?{'&'.join([key+'='+kwargs[key] for key in kwargs.keys()])}",
        headers=HEADERS
    )

def post(url: str, **kwargs: any) -> requests.Response:
    return requests.post(url, params=kwargs, headers=HEADERS)
