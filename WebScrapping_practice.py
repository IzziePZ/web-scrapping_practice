# Web scrapping practice from https://www.scrapethissite.com/pages/forms/

import requests
from bs4 import BeautifulSoup

url = 'https://www.scrapethissite.com/pages/forms/'
response = requests.get(url)
print(response.status_code)

soup = BeautifulSoup(response.text, 'html.parser')

print(soup.prettify())

#Extract all the team names and their corresponding wins and losses from the table on the page.
teams = soup.find_all('tr', class_='team')

print("Team Names and their Wins and Losses:\n")
for team in teams:
    team_name = team.find('td', class_='name').text.strip()
    wins = team.find('td', class_='wins').text.strip()
    losses = team.find('td', class_='losses').text.strip()
    print(f"Team: {team_name}, Wins: {wins}, Losses: {losses}")

    