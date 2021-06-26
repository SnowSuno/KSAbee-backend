import requests
from bs4 import BeautifulSoup


def get_user_info(user_name):
    url = f'https://www.op.gg/summoner/userName={user_name}'

    user_data = {
        'nickname': '',
        'profileImage': '',
        'tier': '',
        'tierInfo': {
            'leaguePoints': 0,
            'wins': 0,
            'losses': 0,
            'winRate': 0,
        }
    }

    response = requests.get(url)

    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')

        if soup.select_one('.SummonerNotFoundLayout') is not None:
            return {}

        user_data['nickname'] = soup.select_one('.Profile>.Information>.Name').text
        user_data['profileImage'] = "https:" + soup.select_one('.ProfileImage')['src']


        tier = soup.select_one('.TierRank').text.strip()
        user_data['tier'] = tier


        if tier != 'Unranked':
            user_data['tierInfo']['leaguePoints'] = int(soup.select_one('.LeaguePoints').text.strip()[:-3])
            user_data['tierInfo']['wins'] = int(soup.select_one('.wins').text[:-1])
            user_data['tierInfo']['losses'] = int(soup.select_one('.losses').text[:-1])
            user_data['tierInfo']['winRate'] = int(soup.select_one('.winratio').text.split()[-1][:-1])

        return user_data

    else:
        raise Exception('fetch fail')


if __name__ == '__main__':
    from pprint import pprint
    pprint(get_user_info('침대에서 뒹굴'))
    pprint(get_user_info('마리마리착마리'))
    pprint(get_user_info('qwerqwefdsad'))
