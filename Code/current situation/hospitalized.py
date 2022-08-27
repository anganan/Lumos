import seaborn as sns
import matplotlib.pyplot as plt
from dataset_info import case
from confirmed_cases import palette

case_temp4 = case.sort_values(["Hospitalized"], ascending=False)

plt.subplots(figsize=(20, 10))
p = sns.barplot(x=case_temp4["Country"][:15], y=case_temp4["Hospitalized"], palette=palette, saturation=1)
p.axes.set_title("\nCountry-wise Hospitalized Cases\n", fontsize=20)
plt.ylabel("Total Cases")
plt.xticks(rotation=90)
for container in p.containers:
    p.bar_label(container, label_type="center", padding=2, size=18, color="black", rotation=0)

sns.despine(left=True, bottom=True)
plt.show()
