# Web scrapping practice from https://www.scrapethissite.com/pages/forms/
# NHL Teams Stats since 1990 to 2011

import requests
from bs4 import BeautifulSoup
import csv

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
        goals_favor = team.find('td', class_='gf').text.strip()
        goals_against = team.find('td', class_='ga').text.strip()
        goal_diff = team.find('td', class_='diff').text.strip()

        all_teams.append({
            'season': int(season) if season else None,
            'team': name,
            'wins': int(wins) if wins else None,
            'losses': int(losses) if losses else None,
            'win_pct': float(win_pct) if win_pct else None,
            'goals_favor': int(goals_favor) if goals_favor else None,
            'goals_against': int(goals_against) if goals_against else None,
            'goal_diff': int(goal_diff) if goal_diff else None,
        })

# Extract all data into a csv file
with open('nhl_teams_data.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['season', 'team', 'wins', 'losses', 'win_pct', 'goals_favor', 'goals_against', 'goal_diff']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for team in all_teams:
        writer.writerow(team)
