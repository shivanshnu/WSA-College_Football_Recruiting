import pandas as pd

position_map = {
    "LS": "LS",
    "WDE": "DE",
    "DL": "DL",
    "OLB": "LB",
    "ILB": "LB",
    "OG": "OG",
    "RB": "RB",
    "PRO": "QB",
    "ATH": "DB",
    "CB": "DB",
    "DT": "DT",
    "WR": "WR",
    "S": "DB",
    "TE": "TE",
    "SDE": "DE",
    "OT": "OT",
    "FB": "RB",
    "OC": "OC",
    "APB": "RB",
    "K": "K",
    "DUAL": "QB",
    "P": "P",
    "QB": "QB",
    "IOL": "OL",
    "LB": "LB",
    "Edge": "DE",
    None: None,
}

# Read csvs
draftees = pd.read_csv("data/all_draftees.csv", index_col=False)
recruits = pd.read_csv("data/recruit_data.csv", index_col=False)
college_stats = pd.read_csv("data/college_data.csv", index_col=False)


college_stats = college_stats.drop(
    columns=[
        "1st Downs",
        "3rd down efficiency",
        "4th down efficiency",
        "Passing",
        "Comp-Att",
        "Sacks-Yards Lost",
        "Rushing",
        "Offense",
        "Returns",
        "Kickoffs: Total",
        "Punt: Total",
        "INT: Total",
        "Kicking",
        "Punt: Total Yards",
        "FG: Good-Attempts",
        "Penalties",
        "Total-Yards",
        "Avg. Per Game (YDS)",
        "Time of Possession",
        "Possession Time Seconds",
        "Miscellaneous",
        "Fumbles-Lost",
        "Average Punt Return Yards",
        "Touchback Percentage",
        "Turnover Ratio",
    ]
)

recruits = recruits.dropna()

training_data = pd.merge(
    recruits,
    draftees,
    on=["Name", "Rating"],
    how="left",
    suffixes=("_recruit", "_draftee"),
)

# Create a new column indicating if the row matches or not
training_data["Drafted"] = training_data["Year_draftee"].notnull()


training_data["Year"] = training_data.apply(
    lambda row: row["Year_recruit"],
    axis=1,
)
training_data["Position"] = training_data.apply(
    lambda row: (
        row["Position_draftee"]
        if row["Drafted"]
        else position_map[row["Position_recruit"]]
    ),
    axis=1,
)
training_data["College"] = training_data.apply(
    lambda row: row["College_draftee"] if row["Drafted"] else row["College_recruit"],
    axis=1,
)


training_data = training_data[
    ["Year", "Name", "College", "Drafted", "Position", "Rating"]
]

# Filter out very young players
training_data = training_data[training_data["Year"] <= 2020]

print(training_data)

training_data = pd.merge(
    training_data,
    college_stats,
    on=["Year", "College"],
    how="left",
)

training_data = training_data.dropna()

training_data = training_data.drop(
    columns=[
        "Year",
        "Name",
        "College",
    ]
)

training_data = training_data.sort_values(
    by=["Drafted", "Rating"], ascending=[False, False]
)

training_data["Drafted"] = training_data["Drafted"].astype(int)
training_data["Net Passing Yards"] = (
    training_data["Net Passing Yards"].str.replace(",", "").astype(int)
)
training_data["Rushing Yards"] = (
    training_data["Rushing Yards"].str.replace(",", "").astype(int)
)
training_data["Total Yards"] = (
    training_data["Total Yards"].str.replace(",", "").astype(int)
)

print(training_data)
training_data.to_csv("data/training_data.csv", index=False)
