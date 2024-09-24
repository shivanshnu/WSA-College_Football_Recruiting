import requests
import pandas as pd
from bs4 import BeautifulSoup


headers = {"User-Agent": "..."}

url = requests.get(
    "https://247sports.com/League/NCAA-FB/Teams/",
    headers=headers,
)
soup = BeautifulSoup(url.text, "html.parser")
conferences = soup.find_all("ul", attrs={"class": "team-index college"})

teams = {}
for conference in conferences:
    for table in conference.find_all("li"):
        for team_row in table.find_all("li"):

            try:
                team_name = team_row.find("a").text
                team_link = team_row.find("a").get("href").split("/")[-2]
            except:
                continue

            teams[team_name] = team_link

teams = dict(sorted(teams.items()))
print(teams)


draft_link = {}
for team_name in teams:
    url = requests.get(
        f"https://247sports.com/college/{teams[team_name]}/",
        headers=headers,
    )

    soup = BeautifulSoup(url.text, "html.parser")

    try:
        drop_downs = soup.find("ul", attrs={"class": "site-nav-list"}).find_all(
            "li", recursive=False
        )
    except:
        continue

    for drop_down in drop_downs:
        if (
            drop_down.find("span")
            and drop_down.find("span").text
            and drop_down.find("span").text == "Football"
        ):

            link = drop_down.find_all("li")[5].find("a").get("href")

            id = link.split("/")[6]

            draft_link[team_name] = id

            print(id)

draft_link = dict(sorted(draft_link.items()))
print(draft_link)


url = requests.get(
    "https://www.espn.com/college-football/teams",
    headers=headers,
)
soup = BeautifulSoup(url.text, "html.parser")
teams = soup.find_all("section", attrs={"class": "TeamLinks flex items-center"})

ids = {}
for team_row in teams:
    try:
        team_name = team_row.find("div").find("a").text
        team_id = team_row.find("a").get("href").split("/")[-2]
    except:
        continue

    ids[team_name] = team_id

ids = dict(sorted(ids.items()))
print(ids)
