from h2o_wave import Q, ui
from Engine.Query import basic_search
import requests


async def home_page_impl(q: Q, details=None):

    left = [
        ui.text_xl(content="Search"),
        ui.textbox(name="query", label="Input your query"),
        ui.button(name="query_btn", label="Search"),
    ]

    right = [
        ui.text_xl(content="Results"),
    ]

    if q.args.query_btn:
        q_code = basic_search(q.args.query)
        response = requests.post(
            "http://localhost:9200/arrtamil/_search",
            json=q_code,
        )
        json_data = response.json()
        hits = json_data["hits"]["hits"]
        print(len(hits))
        right += [
            ui.text_l(f"results: {idx+1}" + str(hits[idx]["_source"]))
            for idx in range(len(hits))
        ]

    cfg = {
        "tag": "home",
        "items": left,
        "right": right,
        "flag": details["flag"],
    }
    return cfg
