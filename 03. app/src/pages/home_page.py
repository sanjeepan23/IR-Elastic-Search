from h2o_wave import Q, ui
from Engine.Query import basic_search, multi_match, agg_multi_match
import requests


async def home_page_impl(q: Q, details=None):

    left = [
        ui.text_xl(content="Search"),
        ui.dropdown(
            name="dropdown",
            label="Dropdown",
            value=q.app.drop,
            trigger=True,
            choices=[
                ui.choice(name="choice1", label="Basic"),
                ui.choice(name="choice2", label="Multi Match"),
                ui.choice(name="choice3", label="Aggregate"),
            ],
        ),
    ]
    if q.args.dropdown == "choice1":
        left += [
            ui.textbox(name="choice1_query", label="Query"),
        ]
    elif q.args.dropdown == "choice2":
        q.app.drop = "choice2"

        left += [
            ui.textbox(name="choice2_query", label="Query"),
            ui.textbox(name="choice2_field1", label="Filed 1"),
            ui.textbox(name="choice2_field2", label="Filed 2"),
        ]

    elif q.args.dropdown == "choice3":
        q.app.drop = "choice3"
        left += [
            ui.textbox(name="choice3_query", label="Query"),
            ui.textbox(name="choice3_field1", label="Filed 1"),
            ui.textbox(name="choice3_field2", label="Filed 1"),
        ]

    left += [ui.button(name="query_btn", label="Search")]

    right = [
        ui.text_xl(content="Results"),
    ]

    if q.args.query_btn:
        if q.args.dropdown == "choice1":
            q_code = basic_search(q.args.choice1_query)

        if q.args.dropdown == "choice2":
            q_code = multi_match(
                q.args.choice2_query,
                fields=[q.args.choice2_field1, q.args.choice2_field2],
            )

        if q.args.dropdown == "choice3":
            q_code = agg_multi_match(
                q.args.choice3_query,
                fields=[q.args.choice3_field1, q.args.choice3_field2],
            )

        response = requests.post(
            "http://localhost:9200/arrtamil2/_search",
            json=q_code,
        )
        json_data = response.json()
        print(json_data)
        hits = json_data["hits"]["hits"]

        right += [ui.text_l(f"Number of Hits: {len(hits)}")]
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
