import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# read the data file
file = pd.read_excel("C:/Users/Developer/Desktop/QCR Project/student-mat.xlsx")
# extract the data for grade and study time and create a DataFrame
Grade = file["G3"].tolist()
study_t = file["studytime"].tolist()
data_set = pd.DataFrame({"Grade": Grade, "Study Time": study_t})
# group the data by grade and study time and count the occurrences
data_set = data_set.groupby(["Grade", "Study Time"]).size().reset_index(name="Count")
# reshape the data to create a pivot table
data_set = data_set.pivot("Grade", "Study Time", "Count")
# plot the heatmap
sns.heatmap(data_set, annot=True, fmt="g", cmap="YlGnBu")
plt.title("Relationship between Final Grade and Weekly Study Time")
plt.show()
