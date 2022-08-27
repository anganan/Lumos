import seaborn as sns
import matplotlib.pyplot as plt
from dataset_info import case

palette_cmap = ["#480838", "#580838", "#600840", "#680840", "#7e002f", "#8c0034", "#900C3F", "#9D0208", "#D00000",
                "#DC2F02", "#E85D04", "#F48C06", "#F5B301", "#FFC300", "#FED053", "#7C7C7C", "#3B3F46", "#2A2E34",
                "#1E2328"]

sns.palplot(sns.color_palette(palette_cmap))

plt.subplots(figsize=(10, 8))

case["Travel_History"] = case[["Travel_History_Yes", "Travel_History_No"]].sum(axis=1)
sns.heatmap(case.drop(columns=["Country", "Total_Cases", "Travel_History"]).corr(), cmap=palette_cmap, square=True,
            cbar_kws=dict(shrink=.95),
            annot=True, vmin=-1, vmax=1, linewidths=0.1, linecolor='white', annot_kws=dict(fontsize=12))
plt.title("Pearson Correlation Of Features\n", size=15)
plt.xticks(rotation=90)
plt.show()
