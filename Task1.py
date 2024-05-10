import pandas as pd
from matplotlib import pyplot as plt
pas = []
fail = []
df=pd.read_excel("C:/Users/Developer/Desktop/QCR Project/student-mat.xlsx")
specific_column=df["G3"].tolist()
study_time = df["studytime"].tolist()
for i in range(len(specific_column)):
  if specific_column[i]>=10:
    pas.append(study_time[i])P
  else:
    fail.append(study_time[i])
plt.boxplot([pas,fail],   boxprops=dict(color='Green'), labels=['Pass Students Study Time','Fail Students Study Time'])
plt.title("Relation Between Pass & Fail Student Study")
plt.ylabel("Study Time")
plt.show()
