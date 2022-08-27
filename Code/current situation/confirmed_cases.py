import seaborn as sns
import matplotlib.pyplot as plt
from dataset_info import case

palette = ["#F38181", "#FCE38A", "#EAFFD0", "#95E1D3", "#A8D8EA", "#AA96DA", "#FCBAD3", "#FFFFD2", "#E4F9F5", "#30E3CA",
           "#11999E", "#40514E", "#F67280", "#C06C84", "#6C5B7B"]

sns.palplot(sns.color_palette(palette))

case_temp1 = case.sort_values(["Confirmed_Cases"], ascending=False)
case_temp2 = case.sort_values(["Suspected_Cases"], ascending=False)

# prepare the layout
_, axs = plt.subplots(1, 2, figsize=(20, 8))
plt.tight_layout(pad=4.0)

# draw "Confirmed_Cases - country" bar chart
sns.barplot(x=case_temp1["Country"][:15], y=case_temp1["Confirmed_Cases"], ax=axs[0], palette=palette, saturation=1)
axs[0].set_ylabel("Total Confirmed Cases")
axs[0].set_xticklabels(axs[0].get_xticklabels(), rotation=90)
for container in axs[0].containers:
    axs[0].bar_label(container, label_type="edge", padding=2, size=15, color="black")

# draw "Suspected_Cases - country" bar chart
sns.barplot(x=case_temp2["Country"][:15], y=case_temp2["Suspected_Cases"], ax=axs[1], palette=palette, saturation=1)
axs[1].set_ylabel("Total Suspected Cases")
axs[1].set_xticklabels(axs[1].get_xticklabels(), rotation=90)
for container in axs[1].containers:
    axs[1].bar_label(container, label_type="edge", padding=2, size=15, color="black")

plt.suptitle("Countries Contaminated With Monkeypox\n", fontsize=30)
sns.despine(left=True, bottom=True)
plt.show()

case_temp3 = case.sort_values(["Total_Cases"], ascending=False)

plt.subplots(figsize=(20, 10))
p = sns.barplot(x=case_temp3["Country"][:15], y=case_temp3["Total_Cases"], palette=palette, saturation=1)
p.axes.set_title("\nCountries Contaminated With Monkeypox\n", fontsize=30)
plt.ylabel("Total Cases")
plt.xticks(rotation=90)
for container in p.containers:
    p.bar_label(container, label_type="center", padding=2, size=15, color="black", rotation=0)

sns.despine(left=True, bottom=True)
plt.show()

# Total

case_temp = case.sort_values(["Total_Cases"], ascending=False)[:15]

case_melt = case_temp.melt(id_vars=['Country'], value_vars=["Total_Cases", "Hospitalized"],
                           var_name="Variables", value_name="Values")

plt.subplots(figsize=(20, 15))
p = sns.barplot(y=case_melt["Country"], x=case_melt["Values"], hue=case_melt["Variables"],
                palette=["#48466D", "#46CDCF"], saturation=1)
p.axes.set_title("\nTop Contaminated Countries' Hospitalized Ratio\n", fontsize=20)
plt.ylabel("Country")
plt.xlabel("Cases")
plt.xticks(rotation=0)
for container in p.containers:
    p.bar_label(container, label_type="edge", padding=2, size=15, color="black", rotation=0)

sns.despine(left=True, bottom=True)
plt.show()
