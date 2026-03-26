import pandas as pd

week1 = pd.read_csv('week_1_sales.csv')
week2 = pd.read_csv('week_2_sales.csv')

#Vertical concat
weekTot = pd.concat([week1,week2], axis=0).drop_duplicates()

bothWeek = pd.merge(week1,week2,on='Customer ID', how='inner')
bothWeekFood = pd.merge(week1,week2,on=['Customer ID','Food ID'], how='inner')

onlyWeek1 = week1 - bothWeek
onlyWeek2 = week2 - bothWeek

customers = pd.read_csv('customers.csv')
customers = customers.rename(columns={"ID":"Customer ID"}).set_index('Customer ID')
print(customers)
custInfo = pd.merge(customers, week1['Customer ID'], on='Customer ID', how='inner')

print(custInfo)