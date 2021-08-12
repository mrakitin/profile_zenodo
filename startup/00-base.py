import os

from pyzenodo3.base import Zenodo

token = os.getenv("ZENODO_SANDBOX_TOKEN", None)
zenodo_client = Zenodo(
    api_key=token, base_url="https://sandbox.zenodo.org/api/"
)

# res = zenodo_client.search("User tools for the NSLS-II Science Network")
