import pandas as pd
from h2o_wave import Q, app, ui, data

config = {
    "app_title": "Search Engine",
    "sub_title": "Powered by Elasticsearch",
    "app_icon": "PeopleAlert",
    "footer_text": "DM & IR",
    "description": """
    """,
}


async def initialize_app(q):
    if q.user.config is None:
        q.user.config = config
        q.user.default_config = config

    if q.user.logo is None:

        q.user.logo_height = "40"

    q.user.init = True


def create_layout(q: Q, tag=None, tool_tab=None):

    config = q.user.config
    q.page.drop()

    q.page["header"] = ui.header_card(
        box=ui.box(
            "header",
            order=2,
        ),
        title=config["app_title"],
        subtitle=config["sub_title"],
        image=q.user.applogo,
        items=[
            ui.text(
                """<style>.wave-w6 {margin-bottom:10px;text-align:center}</style>"""
            ),
            ui.text(
                """<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/css/bootstrap.min.css" integrity="sha384-gH2yIJqKdNHPEq0n4Mqa/HGKIhSkIHeL5AyhkYV8i59U5AR6csBvApHHNl/vI1Bx" crossorigin="anonymous">"""
            ),
        ],
    )

    q.page["footer"] = ui.footer_card(box="footer", caption=config["footer_text"])

    q.page["meta"] = ui.meta_card(
        box="",
        theme="lighting",
        title=config["app_title"],
        layouts=[
            ui.layout(
                breakpoint="l",
                width="1600px",
                zones=[
                    ui.zone(
                        name="header",
                        size="80px",
                    ),
                    ui.zone(
                        name="content_0",
                        direction="row",
                        zones=[
                            ui.zone(
                                name="content_0_0",
                                size="30%",
                                direction="column",
                            ),
                            ui.zone(
                                name="content_0_1",
                                size="70%",
                                direction="column",
                            ),
                        ],
                    ),
                    ui.zone("footer"),
                ],
            )
        ],
    )
