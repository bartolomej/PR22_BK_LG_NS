import pandas as pd
from datetime import datetime
from matplotlib.pyplot import plot


# import functions

def get_acquisitions():
    return pd.read_csv("data/acquisitions.csv", sep=",")


def get_degrees():
    return pd.read_csv("data/degrees.csv", sep=",")


def get_funding_rounds():
    return pd.read_csv("data/funding_rounds.csv", sep=",")


def get_funds():
    return pd.read_csv("data/funds.csv", sep=",")


def get_investments():
    return pd.read_csv("data/investments.csv", sep=",")


def get_ipos():
    return pd.read_csv("data/ipos.csv", sep=",")


def get_milestones():
    return pd.read_csv("data/milestones.csv", sep=",")


def get_objects():
    return pd.read_csv("data/objects.csv", sep=",", low_memory=False)


def get_offices():
    return pd.read_csv("data/offices.csv", sep=",")


def get_people():
    return pd.read_csv("data/people.csv", sep=",")


def get_relationships():
    return pd.read_csv("data/relationships.csv", sep=",")


# other helper functions

def plot_year_count(data, col="created_at", date_format='%Y-%m-%d %H:%M:%S', transform=lambda x: x):
    series = pd.DataFrame(
        [datetime.strptime(str(date), date_format).year for date in data[col].dropna()]
    )
    series = transform(series)
    count = series.groupby(0).size()
    plot(count.index, count.values)
