import requests, os
from bs4 import BeautifulSoup



try:
    ELEMENTS_EMAIL = os.environ["ELEMENTS_EMAIL"]
    ELEMENTS_PASSWORD = os.environ["ELEMENTS_PASSWORD"]
    ELEMENTS_STUDIO_ID = os.environ.get('ELEMENTS_STUDIO_ID', 62)
except KeyError:
    raise Exception('Please set the environment variables ELEMENTS_EMAIL and ELEMENTS_PASSWORD')
    
BASE_URL = 'https://slots.elements.com/'
SHEET_BASE_URL = BASE_URL + 'sheet.php'
SHEET_URL = SHEET_BASE_URL + '?studio_id=' + str(ELEMENTS_STUDIO_ID)



headers = {'User-Agent': 'Mozilla/5.0'}
payload = {
    "action": "login",
    "send": "1",
    "email": ELEMENTS_EMAIL,
    "password": ELEMENTS_PASSWORD,
}


def process_link(session, link):
    full_url = SHEET_BASE_URL + link.get('href')
    print(full_url)
    try:
        response = session.get(full_url)
        response.raise_for_status()
        print('Success!')
    except requests.HTTPError as http_err:
        raise Exception(f'HTTP error occurred: {http_err}')
    except Exception as err:
        raise Exception(f'Other error occurred: {err}')


def main():
    session = requests.Session()
    session.post(BASE_URL, headers=headers, data=payload)

    response = session.get(SHEET_URL)
    response.raise_for_status()
    content = response.content

    soup = BeautifulSoup(content, 'html.parser')
    links = soup.find_all('a', href=lambda href: href and href.startswith("?action=register"))

    if links:
        for link in links:
            process_link(session, link)
    else:
        raise Exception('No links found')


if __name__ == '__main__':
    main()
