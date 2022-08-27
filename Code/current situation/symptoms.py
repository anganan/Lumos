import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from dataset_info import case_timeline
from confirmed_cases import palette

symptoms = case_timeline[["Symptoms"]]
symptoms["Symptoms"].replace(np.nan, "NA", inplace=True)
symptoms = symptoms[symptoms["Symptoms"].isin(["NA"]) == False]
symptoms["Symptoms"] = symptoms["Symptoms"].str.split(", | , | ,|;")
symptoms = symptoms.explode("Symptoms")

# basic natural language processing
symptoms.replace(
    to_replace=[" rash", "rash", "rashes", "vesicular rash", "Rashes", "rash on the skin", "vasicular rashes",
                "rashes in the groin area", "rashes typical of Monkeypox", "Rashes in the perianal region",
                "skin rashes", "Genital rashes", "genital rash"], value="Rash", inplace=True)
symptoms.replace(to_replace=["headache", "headaches"], value="Headache", inplace=True)
symptoms.replace(to_replace=["genital ulcers"], value="oral and genital ulcers", inplace=True)
symptoms.replace(to_replace=["muscle pain", "muscle ache", "back pain", "body pains"], value="Muscle Pain",
                 inplace=True)
symptoms.replace(to_replace=["Swelling", "swelling of lymph nodes", "enlarged lymph nodes",
                             "Slight swallowing difficulties and an elevated temperature"], value="swollen lymph nodes",
                 inplace=True)
symptoms.replace(to_replace=["lesions", "skin manifestations", "isolated skin lesions", "lower abdomen skin lesions",
                             "Spots on skin", "Three lesions typical of monkeypox"], value="skin lesions", inplace=True)
symptoms.replace(to_replace=["fever", "mild fever", "high fever"], value="Fever", inplace=True)
symptoms.replace(to_replace=["fatigue", " myalgia", "vesicles", " inguinal adenopathy"],
                 value=["Fatigue", "myalgia", "Vesicles", "inguinal adenopathy"], inplace=True)
symptoms["Symptoms"] = symptoms["Symptoms"].str.title()

plt.subplots(figsize=(20, 8))
p = sns.countplot(x=symptoms["Symptoms"], order=symptoms["Symptoms"].value_counts().index[:10], palette=palette,
                  saturation=1)

p.axes.set_title("\nSymptom-wise Occurances\n", fontsize=20)
plt.ylabel("Total Occurances")
plt.xlabel("Symptoms")
plt.xticks(rotation=90)
for container in p.containers:
    p.bar_label(container, label_type="center", padding=2, size=20, color="black", rotation=0)

sns.despine(left=True, bottom=True)
plt.show()

# word cloud for symptoms
wordcloud = WordCloud(width=800, height=160,
                      background_color="white", colormap="RdYlGn", max_font_size=40).generate(
    str(symptoms["Symptoms"].values))

plt.figure(figsize=(20, 8), facecolor="#ffd100")
plt.imshow(wordcloud)
plt.axis("off")
plt.margins(x=0, y=0)
plt.tight_layout(pad=0)
plt.show()
