import os
import textwrap

from pyzenodo3.base import Zenodo
from tabulate import tabulate

token = os.getenv("ZENODO_TOKEN", None)
zenodo_client = Zenodo(api_key=token, base_url="https://zenodo.org/api/")


def search_records(
    search="User tools for the NSLS-II Science Network",
    showindex=True,
    tablefmt="grid",
    **kwargs,
):
    results = zenodo_client.search(search, **kwargs)

    data_dict = dict(
        ids=[],
        titles=[],
        versions=[],
        files=[],
        checksums=[],
        dates=[],
    )

    if showindex:
        counter = range(1, len(results)+1)
    else:
        counter = False

    for res in results:
        data = res.data
        meta = data["metadata"]

        data_dict["ids"].append(data["id"])
        title = meta["title"]
        wrapped_title = "\n".join(textwrap.wrap(title, width=30))
        data_dict["titles"].append(wrapped_title)
        data_dict["versions"].append(meta.get("version", "---"))
        data_dict["files"].append(
            "\n".join([f"{f['key']}" for f in data.get("files", [])])
        )
        data_dict["checksums"].append(
            "\n".join([f"{f['checksum']}" for f in data.get("files", [])])
        )
        data_dict["dates"].append(meta["publication_date"])

    print(tabulate(data_dict, headers=data_dict.keys(), showindex=counter,
                   tablefmt=tablefmt))

    return data_dict
