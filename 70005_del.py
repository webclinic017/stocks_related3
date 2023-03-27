import pandas as pd
df = pd.read_csv("titanic.csv")
df.head()


# https://github.com/codebasics/py/blob/master/ML/14_naive_bayes/titanic.csv

df.drop(['PassengerId','Name','SibSp','Parch','Ticket','Cabin','Embarked'],axis='columns',inplace=True)
df.head()

inputs = df.drop('Survived',axis='columns')
target = df.Survived

dummies = pd.get_dummies(inputs.Sex)
dummies.head(3)
inputs.drop(['Sex'],axis='columns',inplace=True)
inputs.head(3)

inputs.columns[inputs.isna().any()]
inputs.Age[:10]

inputs.Age = inputs.Age.fillna(inputs.Age.mean())
inputs.head()

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(inputs,target,test_size=0.3)
print(inputs)


from sklearn.naive_bayes import GaussianNB
model = GaussianNB()
print(model)

model.fit(X_train,y_train)

model.score(X_test,y_test)

X_test[0:10]

y_test[0:10]

model.predict(X_test[0:10])

model.predict_proba(X_test[:10])

from sklearn.model_selection import cross_val_score
p=cross_val_score(GaussianNB(),X_train, y_train, cv=5)
print(p)
