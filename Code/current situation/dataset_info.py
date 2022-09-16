import pandas as pd

# read dataSet
case = pd.read_csv("../../Dataset/cases/Monkey_Pox_Cases_Worldwide.csv")
case_timeline = pd.read_csv("../../Dataset/cases/Worldwide_Case_Detection_Timeline.csv")
case_country = pd.read_csv("../../Dataset/cases/Daily_Country_Wise_Confirmed_Cases.csv")

# print basic information
print(f"Summary of Case Dataset :")

print(f"Informations of Case Dataset :\n")
print(case.info())

print(f"Informations of Case Timeline Dataset :")
print(case_timeline.info())

print(f"Informations of Case Country Wise Dataset :")
print(case_country.info())

# Preprocess the data
case[["Confirmed_Cases", "Suspected_Cases", "Hospitalized", "Travel_History_Yes", "Travel_History_No"]] = case[
    ["Confirmed_Cases", "Suspected_Cases", "Hospitalized", "Travel_History_Yes", "Travel_History_No"]].astype("int")
case["Total_Cases"] = case[["Confirmed_Cases", "Suspected_Cases"]].sum(axis=1)
