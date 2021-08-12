import os

from pyzenodo3.base import Zenodo
from tabulate import tabulate

token = os.getenv("ZENODO_SANDBOX_TOKEN", None)
zenodo_client = Zenodo(
    api_key=token, base_url="https://sandbox.zenodo.org/api/"
)


def search_records(
    search="User tools for the NSLS-II Science Network", showindex=True
):
    results = zenodo_client.search(search)

    data_dict = dict(
        ids=[],
        titles=[],
        versions=[],
        files=[],
        checksums=[],
        dates=[],
    )

    for res in results:
        data = res.data
        meta = data["metadata"]

        data_dict["ids"].append(data["id"])
        data_dict["titles"].append(meta["title"])
        data_dict["versions"].append(meta["version"])
        data_dict["files"].append(
            "\n".join([f"{f['key']}" for f in data["files"]])
        )
        data_dict["checksums"].append(
            "\n".join([f"{f['checksum']}" for f in data["files"]])
        )
        data_dict["dates"].append(meta["publication_date"])

    print(tabulate(data_dict, headers=data_dict.keys(), showindex=showindex))

    return data_dict
