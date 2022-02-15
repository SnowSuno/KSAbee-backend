import json

from aiohttp import ClientSession
from bs4 import BeautifulSoup

from app.schemas import AccountData
from app.common.choices import Tier

import asyncio


async def get_user_data(session: ClientSession, nickname: str) -> AccountData:
    url = f'https://www.op.gg/summoner/userName={nickname}'
    headers = {'User-Agent': 'Mozilla/5.0'}

    try:
        async with session.get(url, headers=headers) as response:
            soup = BeautifulSoup(
                await response.text(), 'html.parser')
            data = json.loads(
                str(soup.select_one("script#__NEXT_DATA__").contents[0])
            )['props']['pageProps']['data']

            tier_data = data['league_stats'][0]['tier_info']

            return AccountData(
                id=data["summoner_id"],
                nickname=data["nickname"],
                profile_image=data["profile_image_url"],
                level=data["level"],
                tier_class=tier_data["tier"],
                division=tier_data["division"],
                league_points=tier_data["lp"],

            )
    except Exception:
        raise
        # raise exceptions.APIFetchError


# async def renew_user(name: str):


async def _test():
    async with ClientSession() as session:
        text = await get_user_data(session, "침대에서 뒹굴")
        print(text)


if __name__ == '__main__':
    asyncio.run(_test())
