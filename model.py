import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import r2_score
from imblearn.over_sampling import RandomOverSampler
from imblearn.under_sampling import RandomUnderSampler

warnings.filterwarnings('ignore')

# Load data
df = pd.read_csv('hds.csv')
df.dropna(inplace=True)
print(df.info())

# Encode categorical variables
label_encoder = LabelEncoder()
for column in df.columns:
    df[column] = label_encoder.fit_transform(df[column])

# Prepare features and target variable
X = df.iloc[:, :-1].values  # Features
y = df["stroke"]  # Target variable

# Perform train-test split with both oversampling and undersampling
ros = RandomOverSampler()
rus = RandomUnderSampler()

X_resampled, y_resampled = ros.fit_resample(X, y)
X_resampled, y_resampled = rus.fit_resample(X_resampled, y_resampled)

X_train, X_test, y_train, y_test = train_test_split(X_resampled, y_resampled, test_size=0.2, stratify=y_resampled)

# Initialize and train RandomForestClassifier
clf = RandomForestClassifier(n_estimators=10, criterion='entropy', random_state=0)
clf.fit(X_train, y_train)

# Make predictions
y_pred = clf.predict(X_test)

# Evaluate accuracy
accuracy = r2_score(y_test, y_pred)*100
print(f'Accuracy: {accuracy}')


# Plotting
plt.figure(figsize=(12, 6))

# Pie chart showing the distribution of the stroke column
plt.subplot(1, 2, 1)
df['stroke'].value_counts().plot(kind='pie', autopct='%1.1f%%', colors=['skyblue', 'lightcoral'])
plt.title('Distribution of Stroke Column - Pie chart')
plt.ylabel('')
plt.legend(['No Stroke', 'Stroke'])

# Create a new figure for the histogram of age
plt.figure(figsize=(8, 6))
sns.histplot(df['age'], kde=False, color='skyblue')
plt.title('Distribution of Age - histplot ')
plt.xlabel('Age')
plt.ylabel('Count')

plt.show()
