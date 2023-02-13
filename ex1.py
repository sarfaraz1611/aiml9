import numpy as np
import math
import pandas as pd
df = pd.read_csv('PlayTennis.csv')
print(df)
outlook = df['Outlook'].tolist()
temperature = df['Temperature'].tolist()
humidity = df['Humidity'].tolist()
wind = df['Wind'].tolist()
play = df['Played football(yes/no'].tolist()
print("\n---------------------Outlook-----------------------\n")
totalOutlook = len(outlook)
totyes = totno = 0
for i in play:
 if i == "Yes":
 totyes += 1
 elif i == "No":
 totno += 1

print("Yes is:", totyes)
print("No is:", totno)
totyesno = totyes + totno
print(totyesno)
entropy = -((totyes/totyesno) * math.log2(totyes/totyesno)) - ((totno/totyesno) * math.log2(totno/totyesno))
print("Entropy: ",entropy)
sunnyyes = sunnyno = overyes = overno = rainyes = rainno = 0
for i, j in zip(outlook, play):
 if i == "Sunny" and j == "Yes":
 sunnyyes += 1
 elif i == "Sunny" and j == "No":
 sunnyno += 1
 elif i == "Overcast" and j == "Yes":
 overyes += 1
 elif i == "Overcast" and j == "No":
 overno += 1
 elif i == "Rain" and j == "Yes":
 rainyes += 1
 elif i == "Rain" and j == "No":
 rainno += 1
print("Sunny Yes: ",sunnyyes)
print("Sunny No: ",sunnyno)
print("Overcast Yes: ",overyes)
print("Overcast No: ",overno)
print("Rain Yes: ",rainyes)
print("Rain No: ",rainno)
#Counting total of yes and no values sunny rain and overcast 

totsunny = sunnyyes + sunnyno
totovercast = overyes + overno
totrain = rainyes + rainno
print("Total Sunny: ", totsunny)
print("Total Overcast: ", totovercast)
print("Total Rain: ", totrain)
#Finding entropy of sunny
if totsunny == sunnyyes or totsunny == sunnyno:
 sunnyEntropy = 0
else:
 sunnyEntropy = -((sunnyyes/totsunny) * math.log2(sunnyyes/totsunny)) - ((sunnyno/totsunny) * math.log2(sunnyno/totsunny))
print("Sunny Entropy: ",sunnyEntropy)

#Finding entropy of overcast
if totovercast == overyes or totovercast == overno:
 overcastEntropy = 0
else:
 overcastEntropy = -((overyes/totovercast) * math.log2(overyes/totovercast)) - ((overno/totovercast) * math.log2(overno/totovercast))
print("Overcast Entropy: ",overcastEntropy)

#Finding entropy of rain
if totrain == rainyes or totrain == rainno:
 rainEntropy = 0
else:
 rainEntropy = -((rainyes/totrain) * math.log2(rainyes/totrain)) - ((rainno/totrain) * math.log2(rainno/totrain))
print("Rain Entropy: ",rainEntropy)
#The information gain of Outlook is:
gainOutlook = entropy - (totsunny/totyesno) * sunnyEntropy - (totovercast/totyesno) * overcastEntropy - (totrain/totyesno) * rainEntropy
print("Outlook Gain: ", gainOutlook)
