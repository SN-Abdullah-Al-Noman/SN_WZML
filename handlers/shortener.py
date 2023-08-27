# (c) @LCUBOTS

import contextlib
from shortzy import Shortzy


async def short_link(user_info, link):
    if "shortener_api" in user_info and "base_site" in user_info:
        shortzy = Shortzy(user_info["shortener_api"], user_info["base_site"]) 
        with contextlib.suppress(Exception):
            link = await shortzy.convert(link)
    return link
