## Goals
Our general goal is to analyze company success. We are interested in which, why, and how did some companies become successful.
## 1. Data preparation
Primariy we read all the data from csv files into pandas dataframes. Additionally we already do a small amount of preprocessing here, for example, taking out only the objects that are companies (inestead of people, products...). Snippet for objets:

    import pandas as pd
    
    get_objects():
        return pd.read_csv("data/objects.csv", sep=",")
    investments = get_investments()
    companies = objects[objects["entity_type"] == "Company"]

We also figure out how much of the data is missing:
Total rows: 28716673
Total attributes: 145
Percentage of missing values: ~32%

## 2. Basic information
Distribution of startups by the state where they were founded:

![Locations](/images/location_bar.png)

Graph of companies created over time. We can see that there was an explosion of new companies created in just the last few years.

![Companies_time](/images/companies_over_time.png)

It would be also interesting to see how was this growth connected to the amount of funding received from VCs.

![Investment_time](/images/investment_over_time.png)

### 3. Industry sectors
Grouping together sectors/categories, we can see which of them have more companies, and also more total investments.

    count_by_category = objects.groupby("category_code").size().sort_values()
    total_fundings = funding_rounds.groupby("object_id", as_index=False)["raised_amount"].sum().sort_values("raised_amount",
                                                                                                            ascending=False)
    total_fundings_per_category = total_fundings.merge(objects, left_on="object_id", right_on="id")[["category_code", "raised_amount"]].groupby("category_code").sum()["raised_amount"].sort_values()
    total_fundings.merge(objects, left_on="object_id", right_on="id")[["category_code", "raised_amount"]].groupby(
        "category_code").sum()["raised_amount"].sort_values()

![total_comp_investments](/images/total_comp_investments.png)

We try to track the investments in different sectors by year, looking at the most invested industry per year:

    total_fundings_by_year = funding_rounds.copy()
    total_fundings_by_year = total_fundings_by_year.dropna(axis=0)
    total_fundings_by_year["funded_at"] = total_fundings_by_year["funded_at"].apply(
        lambda x: datetime.strptime(str(x), "%Y-%m-%d").year)
    total_fundings_by_year = total_fundings_by_year.merge(objects, left_on="object_id", right_on="id")[
        ["category_code", "raised_amount", "funded_at"]].dropna()
    max_fundings_in_year = total_fundings_by_year.groupby(["funded_at", "category_code"]).sum("raised_amount")
    max_fundings_in_year = max_fundings_in_year.reset_index().loc[
        max_fundings_in_year.reset_index().groupby("funded_at")["raised_amount"].idxmax()]

![Yearly_best](/images/yearly_best.png)