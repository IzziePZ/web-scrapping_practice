# Web scrapping practice from https://www.scrapethissite.com/pages/forms/
# NHL Teams Stats since 1990 to 2011

import requests
from bs4 import BeautifulSoup

url = 'https://www.scrapethissite.com/pages/forms/'
response = requests.get(url)
# print(response.status_code)

soup = BeautifulSoup(response.text, 'html.parser')

# print(soup.prettify())

# Change items that appear per page to 100 path "#per_page=100"
url = 'https://www.scrapethissite.com/pages/forms/?per_page=100'
response = requests.get(url)
# print(response.status_code)

soup = BeautifulSoup(response.text, 'html.parser')

# Handle Pagination
base_url = 'https://www.scrapethissite.com/pages/forms/'
params = {'per_page': 100}

pagination = soup.find('ul', class_='pagination')
page_links = pagination.find_all('a') if pagination else []

page_numbers = [
    int(a.text.strip())
    for a in page_links
    if a.text.strip().isdigit()
]

last_page = max(page_numbers) if page_numbers else 1
print(f"Total pages: {last_page}")

# Create list to store all team data
all_teams = []

for page_num in range(1, last_page + 1):
    params['page_num'] = page_num
    response = requests.get(base_url, params=params)
    soup = BeautifulSoup(response.text, 'html.parser')

    teams = soup.find_all('tr', class_='team')
    for team in teams:
        name = team.find('td', class_='name').text.strip()
        season = team.find('td', class_='year').text.strip()
        wins = team.find('td', class_='wins').text.strip()
        losses = team.find('td', class_='losses').text.strip()
        win_pct = team.find('td', class_='pct').text.strip()

        all_teams.append({
            'season': int(season) if season else None,
            'team': name,
            'wins': int(wins) if wins else None,
            'losses': int(losses) if losses else None,
            'win_pct': float(win_pct) if win_pct else None,
        })


