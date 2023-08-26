import pandas as pd
df = pd.read_csv("tested.csv")
inputs = df.drop("Survived",axis = "columns")
target = df["Survived"]
from sklearn.preprocessing import LabelEncoder
le_sex = LabelEncoder()
le_age = LabelEncoder()
le_fare = LabelEncoder()
inputs["sex_n"] = le_sex.fit_transform(inputs["Sex"])
inputs["age_n"] = le_age.fit_transform(inputs["Age"])
inputs["fare_n"] = le_fare.fit_transform(inputs["Fare"])
inputs.head()
inputs_n = inputs.drop(["PassengerId","Name","SibSp","Parch","Ticket","Cabin","Embarked","Sex","Age","Fare"],axis='columns')
inputs_n.head()
from sklearn import tree
model = tree.DecisionTreeClassifier()
model.fit(inputs_n,target)
model.score(inputs_n,target)
#example for prediction.
model.predict([[3,0,60,5]])