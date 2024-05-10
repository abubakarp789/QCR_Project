import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

std_s = []
std_n_s = []
dfmat = pd.read_excel("/Users/Developer/Desktop/QCR Project/student-mat.xlsx")
scs = (dfmat["schoolsup"]).tolist()
stt = (dfmat["G3"]).tolist()
for i in range(len(scs)):
    if scs[i]=='yes':
        std_s.append(stt[i])
    else:
        std_n_s.append(stt[i])
sns.violinplot([std_s,std_n_s])
plt.xlabel('School Support')
plt.ylabel('Final Grade (G3)')
plt.xticks([0, 1], ['Student with scholarship', 'Student without scholarship'])
plt.title('Distribution of Final Grades with and without School Support')
plt.show()
