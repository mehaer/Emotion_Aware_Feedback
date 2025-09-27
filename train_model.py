import pickle
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

# Load data from file
data = np.loadtxt('data.txt', delimiter=None)  # use delimiter=',' if comma-separated

# Split features and labels
X = data[:, :-1]  # all columns except last
y = data[:, -1]   # last column is the label

# Split into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, shuffle=True, stratify=y)

# Initialize and train the model
clf = RandomForestClassifier()
clf.fit(X_train, y_train)

# Predict and evaluate
y_pred = clf.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print(f"Test Accuracy: {accuracy:.2f}")
print(confusion_matrix(y_test, y_pred))

with open('./model', 'wb') as f:
    pickle.dump(clf, f)