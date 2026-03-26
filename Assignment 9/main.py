import pandas as pd
import datetime as dt

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
daySeries = pd.Series([0,0,0,0,0,0,0],days)

def date_to_day(date):
    strdate = date.strip().split("/")
    date = dt.date(int(strdate[2]),int(strdate[0]),int(strdate[1]))
    day = date.strftime("%A")
    daySeries[day] += 1

days_of_war = pd.read_csv("revolutionary_war.csv")["Start Date"].dropna()

for row in days_of_war:
    date_to_day(row)


print(daySeries.idxmax())