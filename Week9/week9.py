import pandas as pd
df = pd.read.csv("/workspaces/codespaces-blank/titanic.csv", r)

#1 
survivors_by_class = df.groupby("Pclass")["Survived"].sum()
avg_fare_by_class = df.groupby("Pclass")["Fare"].mean()

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))

ax1.bar(survivors_by_class.index.astype(str), survivors_by_class.values, color="skyblue")
ax1.set_title("Total Survivors by Class")
ax1.set_xlabel("Passenger Class")
ax1.set_ylabel("Count")

ax2.barh(avg_fare_by_class.index.astype(str), avg_fare_by_class.values, color="salmon")
ax2.set_title("Average Fare by Class")
ax2.set_xlabel("Fare ($)")
ax2.set_ylabel("Passenger Class")

plt.tight_layout()
plt.show()

#2
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid")

plt.figure(figsize=(8, 5))
sns.violinplot(
    data=df, 
    x="Pclass", 
    y="Age", 
    hue="Survived", 
    split=True, 
    inner="quartile"
)

plt.title("Age Distribution by Class and Survival Outcome")
plt.xlabel("Passenger Class")
plt.ylabel("Age")
plt.show()
         

#3
import plotly.express as px

df["FamilySize"] = df["SibSp"] + df["Parch"] + 1

fig = px.scatter(
    df,
    x="Age",
    y="Fare",
    color="Pclass",
    symbol="Survived",
    size="FamilySize",
    hover_name="Name",
    hover_data=["Embarked", "Sex"],
    title="Age vs. Fare by Demographic Signals",
    labels={"Pclass": "Class", "Survived": "Survived?"}
)

fig.show()
         

#4
from plotnine import ggplot, aes, geom_point, stat_smooth, facet_wrap, labs, theme_minimal

(
    ggplot(df, aes(x="Age", y="Fare", color="factor(Survived)"))
    + geom_point(alpha=0.6)
    + stat_smooth(method="lm", se=False)
    + facet_wrap("~ Embarked")
    + labs(
        title="Fare vs. Age Across Embarkation Ports",
        x="Age",
        y="Fare ($)",
        color="Survived (0=No, 1=Yes)"
    )
    + theme_minimal()
)