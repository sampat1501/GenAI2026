import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
import pickle

# Load the dataset
df = pd.read_csv("Churn_Modelling.csv")

# Prepare features
features = df.drop(["RowNumber", "CustomerId", "Surname", "Exited"], axis=1).copy()

# Encode Gender
label_encoder_gender = LabelEncoder()
features["Gender"] = label_encoder_gender.fit_transform(features["Gender"])

# One-hot encode Geography
geo_encoded_df = pd.get_dummies(features["Geography"], prefix="Geography")
features = pd.concat([features.drop("Geography", axis=1), geo_encoded_df], axis=1)

# Split into train and test sets
X = features
Y = df["Exited"]
X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.2, random_state=42
)

# Scale the features
scalar = StandardScaler()
X_train = scalar.fit_transform(X_train)
X_test = scalar.transform(X_test)

# Save the encoders and scaler
with open("label_encoder_gender.pkl", "wb") as file:
    pickle.dump(label_encoder_gender, file)

with open("scaler.pkl", "wb") as file:
    pickle.dump(scalar, file)

print("Training shape:", X_train.shape)
print("Testing shape:", X_test.shape)
