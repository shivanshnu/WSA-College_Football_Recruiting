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

def df_column_switch(df, column1, column2):
    i = list(df.columns)
    a, b = i.index(column1), i.index(column2)
    i[b], i[a] = i[a], i[b]
    df = df[i]
    return df


# Read csvs
testing_data = pd.read_csv("data/recruit_2024_data.csv", index_col=False)
college_stats = pd.read_csv("data/college_2024_data.csv", index_col=False)

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


testing_data = testing_data[["Year", "Name", "Position", "Rating"]]

testing_data = testing_data.dropna()

print(testing_data)

# Perform Cartesian join using merge
testing_data = pd.merge(testing_data, college_stats, on="Year").drop("Year", axis=1)

testing_data = df_column_switch(testing_data, "Rating", "College Name")

testing_data["Position"] = testing_data.apply(
    lambda row: (position_map[row["Position"]]),
    axis=1,
)

testing_data = testing_data.dropna()

testing_data["Net Passing Yards"] = (
    testing_data["Net Passing Yards"].str.replace(",", "").astype(int)
)
testing_data["Rushing Yards"] = (
    testing_data["Rushing Yards"].str.replace(",", "").astype(int)
)
testing_data["Total Yards"] = (
    testing_data["Total Yards"].str.replace(",", "").astype(int)
)

print(testing_data)
testing_data.to_csv("data/testing_data.csv", index=False)
