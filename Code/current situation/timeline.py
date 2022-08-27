import seaborn as sns
import matplotlib.pyplot as plt
from dataset_info import case_country

case_country.set_index("Country", inplace=True)
timeline = case_country.T
timeline.head(5)

_, axs = plt.subplots(3, 3, figsize=(25, 20), sharex=True)
plt.tight_layout(pad=4.0)

sns.lineplot(x=timeline.index, y="Spain", data=timeline, ax=axs[0, 0], color="#0f4c5c")
axs[0, 0].set_title("\nConfirmed Cases of Spain\n", fontsize=20)
axs[0, 0].set_xlabel("Days")
axs[0, 0].set_ylabel("Number of Patients")

sns.lineplot(x=timeline.index, y="United States", data=timeline, ax=axs[0, 1], color="#FFC300")
axs[0, 1].set_title("\nConfirmed Cases of United States\n", fontsize=20)
axs[0, 1].set_xlabel("Days")
axs[0, 1].set_ylabel("Number of Patients")

sns.lineplot(x=timeline.index, y="Germany", data=timeline, ax=axs[0, 2], color="#7C7C7C")
axs[0, 2].set_title("\nConfirmed Cases of Germany\n", fontsize=20)
axs[0, 2].set_xlabel("Days")
axs[0, 2].set_ylabel("Number of Patients")

sns.lineplot(x=timeline.index, y="England", data=timeline, ax=axs[1, 0], color="#5f0f40")
axs[1, 0].set_title("\nConfirmed Cases of England\n", fontsize=20)
axs[1, 0].set_xlabel("Days")
axs[1, 0].set_ylabel("Number of Patients")

sns.lineplot(x=timeline.index, y="France", data=timeline, ax=axs[1, 1], color="#f85e00")
axs[1, 1].set_title("\nConfirmed Cases of France\n", fontsize=20)
axs[1, 1].set_xlabel("Days")
axs[1, 1].set_ylabel("Number of Patients")

sns.lineplot(x=timeline.index, y="Netherlands", data=timeline, ax=axs[1, 2], color="#9a031e")
axs[1, 2].set_title("\nConfirmed Cases of Netherlands\n", fontsize=20)
axs[1, 2].set_xlabel("Days")
axs[1, 2].set_ylabel("Number of Patients")

sns.lineplot(x=timeline.index, y="Canada", data=timeline, ax=axs[2, 0], color="#918450")
axs[2, 0].set_title("\nConfirmed Cases of Canada\n", fontsize=20)
axs[2, 0].set_xlabel("Days")
axs[2, 0].set_ylabel("Number of Patients")

sns.lineplot(x=timeline.index, y="Portugal", data=timeline, ax=axs[2, 1], color="#1d7874")
axs[2, 1].set_title("\nConfirmed Cases of Portugal\n", fontsize=20)
axs[2, 1].set_xlabel("Days")
axs[2, 1].set_ylabel("Number of Patients")

sns.lineplot(x=timeline.index, y="Brazil", data=timeline, ax=axs[2, 2], color="#333533")
axs[2, 2].set_title("\nConfirmed Cases of Brazil\n", fontsize=20)
axs[2, 2].set_xlabel("Days")
axs[2, 2].set_ylabel("Number of Patients")
axs[2, 2].set_xticks([], minor=False)

sns.despine(left=True, bottom=True)
plt.show()

_, axs = plt.subplots(figsize=(20, 10))
plt.tight_layout(pad=4.0)

sns.lineplot(x=timeline.index, y=timeline["Spain"].cumsum(axis=0), data=timeline, ax=axs, color="#0f4c5c")
sns.lineplot(x=timeline.index, y=timeline["United States"].cumsum(axis=0), data=timeline, ax=axs, color="#FFC300")
sns.lineplot(x=timeline.index, y=timeline["Germany"].cumsum(axis=0), data=timeline, ax=axs, color="#7C7C7C")
sns.lineplot(x=timeline.index, y=timeline["England"].cumsum(axis=0), data=timeline, ax=axs, color="#5f0f40")
sns.lineplot(x=timeline.index, y=timeline["France"].cumsum(axis=0), data=timeline, ax=axs, color="#f85e00")
sns.lineplot(x=timeline.index, y=timeline["Netherlands"].cumsum(axis=0), data=timeline, ax=axs, color="#9a031e")
sns.lineplot(x=timeline.index, y=timeline["Canada"].cumsum(axis=0), data=timeline, ax=axs, color="#918450")
sns.lineplot(x=timeline.index, y=timeline["Portugal"].cumsum(axis=0), data=timeline, ax=axs, color="#1d7874")
sns.lineplot(x=timeline.index, y=timeline["Brazil"].cumsum(axis=0), data=timeline, ax=axs, color="#333533")

axs.set_title("\nConfirmed Cases\n", fontsize=20)
axs.set_xlabel("Days")
axs.set_ylabel("Number of Patients")
axs.legend(["Spain", "United States", "Germany", "England", "France", "Netherlands", "Canada", "Portugal", "Brazil"])
axs.set_xticks([], minor=False)
sns.despine(left=True, bottom=True)
plt.show()
