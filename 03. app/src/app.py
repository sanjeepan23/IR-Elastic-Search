from h2o_wave import Q, app, main

from src.layout import initialize_app
from src.pages.home_page import home_page_impl
from src.render_template import render_template


@app("/")
async def serve(q: Q):
    print(q.args)
    if q.user.init != True:
        await initialize_app(q)

    if q.args.query_btn:
        await home_page(q, {"flag": "home"})
    await home_page(q, {"flag": "home"})
    await q.page.save()


async def home_page(q, details):
    cfg = await home_page_impl(q, details)
    await render_template(q, cfg)
