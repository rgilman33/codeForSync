import pandas as pd 
import numpy as np 

names = ['grok', 'blogg', 'frag', 'quark', 'zoog', 'pete']
ages = np.random.randint(low=12, high=80, size=6)
df = pd.DataFrame({'name':names, 'age':ages})
print(df)

df_json = df.to_json(orient="records")
print(df_json)

ships = ['Black Pearl', 'Adventure Galley', "Whydah", "Queen Anne's Revenge", "Fancy", "Royal Fortune" ]
prey = ['England', 'Spain', "Netherlands", "France"]

a, p, d, b = [],[],[],[]
dateRange = pd.date_range('01/01/1800', '01/01/1850', freq='D')
for i in range(100):
	a.append(ships[np.random.randint(0,len(ships))])
	p.append(prey[np.random.randint(0,len(prey))])
	d.append(dateRange[np.random.randint(0,len(dateRange))])
	b.append(np.random.randint(0,1000000))

historicalBooty = pd.DataFrame({"Ship":a, 'Prey':p, 'Date':d, 'bootyAmount':b}).sort('Date', ascending=True)
print(historicalBooty.to_json(orient='records'))

totalBootyByShip = pd.pivot_table(historicalBooty, values='bootyAmount', index='Prey', aggfunc=np.sum)
print(totalBootyByShip)

historicalBooty.to_excel("historicalBooty.xlsx")