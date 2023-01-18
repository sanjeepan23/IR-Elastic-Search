from h2o_wave import Q, ui


async def about_page_impl(q: Q, details=None):
    q.app.tab = "about"
    items = [
        ui.text_l(
            content="Our “Next Best Conversation” platform redefines the marketing model – creating a centralised, always-on brain to drive relevant interactions for each customer powered by big data, machine learning and real-time contextual data."
        ),
    ]

    cfg = {
        "tag": "about",
        "items": items,
        "flag": "",
    }
    return cfg
