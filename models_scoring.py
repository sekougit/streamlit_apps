import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
donnees=pd.read_csv("sample_train_imputed.csv")
donnees=donnees.drop("")
bon_base=pd.DataFrame(donnees)
base_sample=bon_base.sample(50)




# 📌 2️⃣ Fonction pour entraîner le modèle
def train_model():
    data=base_sample
    X = data.drop(columns=["TARGET"])
    y = data["TARGET"]

    # Division en ensemble d'entraînement et de test
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Entraînement du modèle RandomForest
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Évaluation du modèle
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"🎯 Accuracy du modèle : {accuracy * 100:.2f}%")

    return model

# 📌 3️⃣ Fonction pour récupérer un modèle déjà entraîné
def get_trained_model():
    return train_model()  # Renvoie directement un modèle entraîné