import requests
import pandas as pd
from bs4 import BeautifulSoup


colleges = {
    "Air Force Falcons": "Air-Force-Falcons-Football-132",
    "Akron Zips": "Akron-Zips-Football-111",
    "Alabama Crimson Tide": "Alabama-Crimson-Tide-Football-164",
    "Appalachian State Mountaineers": "Appalachian-State-Mountaineers-Football-350",
    "Arizona State Sun Devils": "Arizona-State-Sun-Devils-Football-148",
    "Arizona Wildcats": "Arizona-Wildcats-Football-146",
    "Arkansas Razorbacks": "Arkansas-Razorbacks-Football-166",
    "Arkansas State Red Wolves": "Arkansas-State-Red-Wolves-Football-188",
    "Army Black Knights": "Army-Black-Knights-Football-107",
    "Auburn Tigers": "Auburn-Tigers-Football-168",
    "Ball State Cardinals": "Ball-State-Cardinals-Football-113",
    "Baylor Bears": "Baylor-Bears-Football-25",
    "Boise State Broncos": "Boise-State-Broncos-Football-202",
    "Boston College Eagles": "Boston-College-Eagles-Football-1",
    "Bowling Green Falcons": "Bowling-Green-Falcons-Football-115",
    "Brigham Young Cougars": "Brigham-Young-Cougars-Football-134",
    "Brown Bears": "Brown-Bears-Football-292",
    "California Golden Bears": "California-Golden-Bears-Football-150",
    "Central Michigan Chippewas": "Central-Michigan-Chippewas-Football-118",
    "Charlotte 49ers": "Charlotte-49ers-Football-474",
    "Chattanooga Mocs": "Chattanooga-Mocs-Football-351",
    "Cincinnati Bearcats": "Cincinnati-Bearcats-Football-49",
    "Clemson Tigers": "Clemson-Tigers-Football-3",
    "Colgate Raiders": "Colgate-Raiders-Football-767",
    "Colorado Buffaloes": "Colorado-Buffaloes-Football-27",
    "Colorado State Rams": "Colorado-State-Rams-Football-135",
    "Columbia Lions": "Columbia-Lions-Football-293",
    "Connecticut Huskies": "Connecticut-Huskies-Football-51",
    "Cornell Big Red": "Cornell-Big-Red-Football-294",
    "Dartmouth Big Green": "Dartmouth-Big-Green-Football-295",
    "Duke Blue Devils": "Duke-Blue-Devils-Football-5",
    "Duquesne Dukes": "Duquesne-Dukes-Football-323",
    "East Carolina Pirates": "East-Carolina-Pirates-Football-87",
    "Eastern Michigan Eagles": "Eastern-Michigan-Eagles-Football-448",
    "Florida Atlantic Owls": "Florida-Atlantic-Owls-Football-443",
    "Florida Gators": "Florida-Gators-Football-170",
    "Florida State Seminoles": "Florida-State-Seminoles-Football-7",
    "Fordham Rams": "Fordham-Rams-Football-768",
    "Fresno State Bulldogs": "Fresno-State-Bulldogs-Football-440",
    "Georgetown Hoyas": "Georgetown-Hoyas-Football-765",
    "Georgia Bulldogs": "Georgia-Bulldogs-Football-172",
    "Georgia Southern Eagles": "Georgia-Southern-Eagles-Football-355",
    "Georgia State Panthers": "Georgia-State-Panthers-Football-288",
    "Georgia Tech Yellow Jackets": "Georgia-Tech-Yellow-Jackets-Football-9",
    "Harvard Crimson": "Harvard-Crimson-Football-296",
    "Hawaii Rainbow Warriors": "Hawaii-Rainbow-Warriors-Football-204",
    "Houston Cougars": "Houston-Cougars-Football-89",
    "Idaho Vandals": "Idaho-Vandals-Football-206",
    "Illinois Fighting Illini": "Illinois-Fighting-Illini-Football-65",
    "Illinois State Redbirds": "Illinois-State-Redbirds-Football-311",
    "Indiana Hoosiers": "Indiana-Hoosiers-Football-67",
    "Indiana State Sycamores": "Indiana-State-Sycamores-Football-312",
    "Iowa Hawkeyes": "Iowa-Hawkeyes-Football-69",
    "Iowa State Cyclones": "Iowa-State-Cyclones-Football-29",
    "Jackson State Tigers": "Jackson-State-Tigers-Football-372",
    "Kansas Jayhawks": "Kansas-Jayhawks-Football-31",
    "Kansas State Wildcats": "Kansas-State-Wildcats-Football-33",
    "Kent State Golden Flashes": "Kent-State-Golden-Flashes-Football-119",
    "Kentucky Wildcats": "Kentucky-Wildcats-Football-174",
    "LSU Tigers": "LSU-Tigers-Football-176",
    "Louisiana Ragin' Cajuns": "Louisiana-Ragin-Cajuns-Football-190",
    "Louisiana-Monroe Warhawks": "LouisianaMonroe-Warhawks-Football-192",
    "Louisville Cardinals": "Louisville-Cardinals-Football-53",
    "Marshall Thundering Herd": "Marshall-Thundering-Herd-Football-91",
    "Maryland Terrapins": "Maryland-Terrapins-Football-11",
    "Memphis Tigers": "Memphis-Tigers-Football-93",
    "Miami (OH) RedHawks": "Miami-OH-RedHawks-Football-121",
    "Miami Hurricanes": "Miami-Hurricanes-Football-13",
    "Michigan State Spartans": "Michigan-State-Spartans-Football-73",
    "Michigan Wolverines": "Michigan-Wolverines-Football-71",
    "Middle Tennessee State Blue Raiders": "Middle-Tennessee-State-Blue-Raiders-Football-194",
    "Minnesota Golden Gophers": "Minnesota-Golden-Gophers-Football-75",
    "Mississippi State Bulldogs": "Mississippi-State-Bulldogs-Football-180",
    "Missouri State Bears": "Missouri-State-Bears-Football-313",
    "Missouri Tigers": "Missouri-Tigers-Football-458",
    "NC State Wolfpack": "NC-State-Wolfpack-Football-17",
    "Navy Midshipmen": "Navy-Midshipmen-Football-108",
    "Nebraska Cornhuskers": "Nebraska-Cornhuskers-Football-37",
    "Nevada Wolf Pack": "Nevada-Wolf-Pack-Football-438",
    "New Mexico Lobos": "New-Mexico-Lobos-Football-137",
    "New Mexico State Aggies": "New-Mexico-State-Aggies-Football-210",
    "North Carolina A&T Aggies": "North-Carolina-AT-Aggies-Football-307",
    "North Carolina Tar Heels": "North-Carolina-Tar-Heels-Football-15",
    "North Dakota Fighting Hawks": "North-Dakota-Fighting-Hawks-Football-753",
    "North Dakota State Bison": "North-Dakota-State-Bison-Football-314",
    "North Texas Mean Green": "North-Texas-Mean-Green-Football-196",
    "Northern Illinois Huskies": "Northern-Illinois-Huskies-Football-123",
    "Northern Iowa Panthers": "Northern-Iowa-Panthers-Football-315",
    "Northwestern Wildcats": "Northwestern-Wildcats-Football-77",
    "Notre Dame Fighting Irish": "Notre-Dame-Fighting-Irish-Football-109",
    "Ohio Bobcats": "Ohio-Bobcats-Football-125",
    "Ohio State Buckeyes": "Ohio-State-Buckeyes-Football-79",
    "Oklahoma Sooners": "Oklahoma-Sooners-Football-39",
    "Oklahoma State Cowboys": "Oklahoma-State-Cowboys-Football-41",
    "Old Dominion Monarchs": "Old-Dominion-Monarchs-Football-277",
    "Ole Miss Rebels": "Ole-Miss-Rebels-Football-178",
    "Oregon Ducks": "Oregon-Ducks-Football-152",
    "Oregon State Beavers": "Oregon-State-Beavers-Football-154",
    "Penn State Nittany Lions": "Penn-State-Nittany-Lions-Football-81",
    "Pennsylvania Quakers": "Pennsylvania-Quakers-Football-297",
    "Pittsburgh Panthers": "Pittsburgh-Panthers-Football-460",
    "Princeton Tigers": "Princeton-Tigers-Football-758",
    "Purdue Boilermakers": "Purdue-Boilermakers-Football-83",
    "Rhode Island Rams": "Rhode-Island-Rams-Football-278",
    "Rice Owls": "Rice-Owls-Football-428",
    "Richmond Spiders": "Richmond-Spiders-Football-279",
    "Rutgers Scarlet Knights": "Rutgers-Scarlet-Knights-Football-57",
    "SMU Mustangs": "SMU-Mustangs-Football-426",
    "San Diego State Aztecs": "San-Diego-State-Aztecs-Football-139",
    "San Jose State Spartans": "San-Jose-State-Spartans-Football-212",
    "South Alabama Jaguars": "South-Alabama-Jaguars-Football-289",
    "South Carolina Gamecocks": "South-Carolina-Gamecocks-Football-182",
    "South Florida Bulls": "South-Florida-Bulls-Football-59",
    "Southern Illinois Salukis": "Southern-Illinois-Salukis-Football-317",
    "Southern Miss Golden Eagles": "Southern-Miss-Golden-Eagles-Football-95",
    "Stanford Cardinal": "Stanford-Cardinal-Football-156",
    "Syracuse Orange": "Syracuse-Orange-Football-461",
    "TCU Horned Frogs": "TCU-Horned-Frogs-Football-456",
    "Temple Owls": "Temple-Owls-Football-127",
    "Tennessee State Tigers": "Tennessee-State-Tigers-Football-335",
    "Tennessee Volunteers": "Tennessee-Volunteers-Football-184",
    "Texas A&M Aggies": "Texas-AM-Aggies-Football-459",
    "Texas Longhorns": "Texas-Longhorns-Football-43",
    "Texas State Bobcats": "Texas-State-Bobcats-Football-290",
    "Texas Tech Red Raiders": "Texas-Tech-Red-Raiders-Football-47",
    "Toledo Rockets": "Toledo-Rockets-Football-128",
    "Troy Trojans": "Troy-Trojans-Football-198",
    "Tulane Green Wave": "Tulane-Green-Wave-Football-97",
    "UAB Blazers": "UAB-Blazers-Football-101",
    "UCF Knights": "UCF-Knights-Football-103",
    "UCLA Bruins": "UCLA-Bruins-Football-158",
    "UMass Minutemen": "UMass-Minutemen-Football-475",
    "UNLV Rebels": "UNLV-Rebels-Football-142",
    "USC Trojans": "USC-Trojans-Football-214",
    "UTEP Miners": "UTEP-Miners-Football-105",
    "UTSA Roadrunners": "UTSA-Roadrunners-Football-291",
    "Utah State Aggies": "Utah-State-Aggies-Football-439",
    "Utah Utes": "Utah-Utes-Football-144",
    "Vanderbilt Commodores": "Vanderbilt-Commodores-Football-186",
    "Villanova Wildcats": "Villanova-Wildcats-Football-281",
    "Virginia Cavaliers": "Virginia-Cavaliers-Football-19",
    "Virginia Tech Hokies": "Virginia-Tech-Hokies-Football-21",
    "Wake Forest Demon Deacons": "Wake-Forest-Demon-Deacons-Football-23",
    "Washington Huskies": "Washington-Huskies-Football-160",
    "Washington State Cougars": "Washington-State-Cougars-Football-162",
    "West Virginia Mountaineers": "West-Virginia-Mountaineers-Football-457",
    "Western Carolina Catamounts": "Western-Carolina-Catamounts-Football-357",
    "Western Kentucky Hilltoppers": "Western-Kentucky-Hilltoppers-Football-200",
    "Western Michigan Broncos": "Western-Michigan-Broncos-Football-130",
    "William & Mary Tribe": "William-Mary-Tribe-Football-282",
    "Wisconsin Badgers": "Wisconsin-Badgers-Football-85",
    "Wyoming Cowboys": "Wyoming-Cowboys-Football-430",
}

player_data = pd.DataFrame(
    columns=["Year", "Pick", "Name", "Position", "College", "Rating"]
)

headers = {"User-Agent": "..."}

for college_name in colleges:
    for year in range(2000, 2024):

        url = requests.get(
            f"https://247sports.com/college/akron/Team/{colleges[college_name]}/DraftPicks/?year={year}",
            headers=headers,
        )
        soup = BeautifulSoup(url.text, "html.parser")
        table = soup.find("section", attrs={"class": "main-content list-content"}).find(
            "ul"
        )

        count = 0
        rows = table.find_all("li", recursive=False)

        for row in rows:
            if row.get("class") == None:
                columns = row.find_all("div")

                player = {
                    "Year": year,
                    "Pick": columns[1].find_all("span")[1].text,
                    "Name": columns[3].find("a").text,
                    "Position": columns[2].find("ul").find("li").text,
                    "College": college_name,
                    "Rating": columns[4].find_all("span")[5].text,
                }

                print(player)

                player_data.loc[len(player_data)] = player


print(player_data)
player_data.to_csv("data/all_draftees.csv", index=False)
