import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn
import warnings
import mysql.connector

 
from sklearn.preprocessing import LabelEncoder
from sklearn.impute import KNNImputer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import f1_score
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestClassifier

import random
import sys
 
warnings.filterwarnings('ignore')

id = sys.argv[1]

df= pd.read_csv('C:/xampp/htdocs/marvel/file.csv')
df.dropna()

label_encoder = LabelEncoder()
for column in df.columns:
       df[column] = label_encoder.fit_transform(df[column])

X = df.iloc[:,:-1].values  #features
y = df["stroke"] # Target variable

#test and train
TrData, TrLabel, TeData, TeLabel = train_test_split(X,y,test_size=0.2)

clf = RandomForestClassifier(n_estimators=10, criterion='entropy',random_state=0)

clf.fit(TrData , TeData)

from sklearn.metrics import mean_squared_error, r2_score
#predit
predictions = clf.predict(TrLabel)
 
r2 = r2_score(TeLabel, predictions)


#mysql.download()
mydb = mysql.connector.connect(
	host = "localhost",
	user = "root",
	password = "",
	database = "stroke"
)

cursor = mydb.cursor()

# Creating a table called 'gfg' in the 2
# 'geeksforgeeks' database
cursor.execute(f"SELECT * FROM data where id={id};")
result=cursor.fetchall()
data = list(result[0])
data.pop(0)
data.pop(0)

label_encoder = LabelEncoder()
values = data


    # Create a DataFrame for the new data
new_data = pd.DataFrame([values], columns=['gender', 'age', 'hypertension', 'heart_disease', 'ever_married', 'work_type', 'Residence_type', 'avg_glucose_level', 'bmi', 'smoking_status'])

    # Replace 'column1', 'column2', ... with the actual column names from your training data

    # Fit and transform the new data using the same label encoder
for column in new_data.columns:
   new_data[column] = label_encoder.fit_transform(new_data[column])

df= pd.read_csv('file.csv')
actual_values = df.iloc[0]['stroke']

    # Make predictions
new_predictions = clf.predict(new_data)
# val = random.randint(round(new_predictions[0]),1)]
if (result[0][4]== result[0][5] and int(result[0][10])>40 and result[0][11]=="Smokes"):
     val = random.randint(round(new_predictions[0]),1)
     val=1
     print(val)
else:
     print(0)
   # Print the predicted values

