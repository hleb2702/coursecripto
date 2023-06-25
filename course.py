import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

def course(valute='bitcoin'):
    URL = f'https://myfin.by/crypto-rates/{valute}'
    HEADERS = {
        'User-Agent': UserAgent().random
    }
    response = requests.get(URL, headers=HEADERS)
    soup = BeautifulSoup(response.content, 'html.parser')
    items = soup.find('div', class_ = "birzha_info_head_rates").get_text(strip=True)
    return float(items[:-1])

def valute_list():
    return [
        'bitcoin',
        'ethereum',
        'tether',
        'ripple',
        'bitcoincash',
        'ethereumclassic',
        'monero',
        'dogecoin',
        'litecoin',
        'tronix',
        'omisego',
        'stellar',
        'gigitalcash',
        'neo',
        'eos',
        'verge',
        'decentraland',
        'zcash',
        'lisk',
        'decred'
    ]

print(course('ripple'))


