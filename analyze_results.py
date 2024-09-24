import pandas as pd

# Read csvs
results = pd.read_csv("data/results.csv", index_col=False)


position_map = {
    "TE": {
        "Nevada Wolf Pack": 68,
        "James Madison Dukes": 68,
        "Texas Longhorns": 51,
        "Michigan Wolverines": 8,
        "Kennesaw State Owls": 7,
        "Ole Miss Rebels": 2,
    },
    "OT": {
        "Tulane Green Wave": 105,
        "Notre Dame Fighting Irish": 105,
        "Michigan Wolverines": 59,
        "James Madison Dukes": 46,
    },
    "QB": {
        "USC Trojans": 93,
        "Oregon Ducks": 87,
        "Washington Huskies": 81,
        "Nevada Wolf Pack": 10,
        "Kennesaw State Owls": 5,
        "LSU Tigers": 3,
    },
    "OL": {
        "Kennesaw State Owls": 92,
        "Nevada Wolf Pack": 92,
        "Iowa Hawkeyes": 84,
        "Rice Owls": 8,
    },
    "DL": {
        "James Madison Dukes": 111,
        "Michigan Wolverines": 103,
        "Kennesaw State Owls": 72,
        "Texas Longhorns": 21,
        "USC Trojans": 19,
        "Oregon Ducks": 7,
        "Iowa Hawkeyes": 3,
    },
    "WR": {
        "James Madison Dukes": 129,
        "Texas Longhorns": 83,
        "South Carolina Gamecocks": 70,
        "Nevada Wolf Pack": 54,
        "Ohio State Buckeyes": 30,
        "Ole Miss Rebels": 16,
        "Michigan Wolverines": 3,
        "Utah State Aggies": 2,
    },
    "DB": {
        "Utah State Aggies": 321,
        "Appalachian State Mountaineers": 296,
        "James Madison Dukes": 251,
        "SMU Mustangs": 60,
        "Coastal Carolina Chanticleers": 25,
        "Ohio State Buckeyes": 10,
    },
    "K": {"Kennesaw State Owls": 4, "Nevada Wolf Pack": 4, "Iowa Hawkeyes": 4},
    "DE": {
        "James Madison Dukes": 90,
        "Michigan Wolverines": 78,
        "Ole Miss Rebels": 69,
        "Notre Dame Fighting Irish": 20,
        "Oregon State Beavers": 9,
        "Memphis Tigers": 4,
    },
    "RB": {
        "Nevada Wolf Pack": 72,
        "Iowa Hawkeyes": 72,
        "Charlotte 49ers": 59,
        "Kennesaw State Owls": 13,
    },
    "LB": {
        "Nevada Wolf Pack": 116,
        "Akron Zips": 90,
        "Coastal Carolina Chanticleers": 56,
        "USC Trojans": 49,
        "James Madison Dukes": 26,
        "Colorado Buffaloes": 11,
    },
    "P": {"Nevada Wolf Pack": 6, "Minnesota Golden Gophers": 6, "Iowa Hawkeyes": 6},
}

position_map = {}
for train_index, train_row in results.iterrows():
    college = train_row["College Name"]
    pos = train_row["Position"]

    try:
        position_map[pos]
    except:
        position_map[pos] = {}

    try:
        position_map[pos][college]
    except:
        position_map[pos][college] = 0

    position_map[pos][college] += 1

for key in position_map:
    position_map[key] = dict(
        sorted(position_map[key].items(), key=lambda item: item[1], reverse=True)
    )

print(position_map)
