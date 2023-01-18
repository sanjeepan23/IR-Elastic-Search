from h2o_wave import Q, app, ui, data, main, on, handle_on, pack
import pandas as pd
from src.layout import create_layout


async def render_template(q: Q, page_cfg):

    create_layout(q, tag=page_cfg["tag"])

    if page_cfg["tag"] == "home":
        q.page["card_10"] = ui.form_card(
            box=ui.box(
                "content_0_0",
            ),
            title="",
            items=page_cfg["items"],
        )

        q.page["card_11"] = ui.form_card(
            box=ui.box(
                "content_0_1",
            ),
            title="",
            items=page_cfg["right"],
        )
    await q.page.save()
