import numpy as np
import pandas as pd

df = pd.DataFrame({
    "Region": np.random.choice(["Nord","Centro","Sud"],200),
    "Salesperson": np.random.choice(["Mirco","Gordon","Goku","Saitama","Charles","Walus"],200),
    "Revenue": np.random.normal(5000,100,200).round(2),
    "Costs": np.random.normal(1000,50,200).round(2),
    "Quarter": np.random.choice(["Q1","Q2","Q3","Q4"],200)
})

listIdx = list(df.index)

for col in ["Revenue","Costs"]:
    nan_idx = np.random.choice(listIdx,20,False)
    df.loc[nan_idx,col] = np.nan

df = df.dropna(subset=["Revenue"])

df["Costs"] = df["Costs"].fillna(df.groupby("Region")["Costs"].transform("mean"))

df["Profit"] = df["Revenue"]-df["Costs"]

df_new = df.groupby(["Region","Quarter"]).agg(
    Profit_Medio=("Profit", "mean"),
    Profit_Totale=("Profit", "sum"),
    Numero_Vendite=("Profit", "count")
    )

SalesAvg = df.groupby(["Region","Salesperson"])["Revenue"].mean()
df_new = SalesAvg.groupby(level=0).idxmax()
df_new_avg = SalesAvg[df_new].reset_index()

print(df_new_avg)


df["region_total"] = df.groupby("Region")["Profit"].sum()
df["region_percent"] = df["Profit"]/df["region_total"]