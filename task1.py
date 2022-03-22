import pandas as pd

#Task1
print("Task 1")

redWine = pd.read_csv("https://raw.githubusercontent.com/data-max-hq/workshop-epoka/main/data/winequality-red.csv")
print(redWine)
#Task2 
#Atributi qe pershkruan me mire cilesine eshte "Quality"
print("Task 2")
qualityDataset = pd.DataFrame({'Quality': redWine.quality})
print(qualityDataset)

#Task3
print("Task 3")
qualityValueRange = pd.unique(redWine.quality)
#redWine.quality.unique()
print( qualityValueRange)

#Task 4
#11  float
#1 int
print("Task 4")
print(redWine.dtypes)

#Task5
print("Task 5")
cnt=0
sum=0

for value in redWine.quality:
  sum+= value
  cnt+=1
avg= sum/cnt
print(round(avg,3))
print(round(redWine.quality.mean(),3))
#Task6
print("Task 6")
cnt=0
sum=0
avg=0

alcoholBestQuality =redWine.loc[redWine.quality == max(qualityValueRange)].alcohol

for value in alcoholBestQuality:
  sum+= value
  cnt+= 1
  
avg= sum/cnt
print(round(avg,3))

#Task7
cnt=0
sum=0
avg=0
print("Task 7")
alcoholWorstQuality =redWine.loc[redWine.quality == min(qualityValueRange)].alcohol

for value in alcoholWorstQuality:
  sum+= value
  cnt+= 1
  
avg= sum/cnt
print(round(avg,3))

#task8
print("Task 8")
sulfurDioxideLimit =redWine[(redWine['total sulfur dioxide']>=175) & (redWine['total sulfur dioxide']<=203) ].sort_values(by=["total sulfur dioxide"], ascending=False)
print(sulfurDioxideLimit.loc[:,['total sulfur dioxide']])

#Task9
print("Task 9")
redWine.groupby(['quality']).size().plot.pie(y='count')