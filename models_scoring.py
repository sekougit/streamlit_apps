import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# 📌 Charger les données d'entraînement
try:
    donnees_train = pd.read_csv("sample_train_imputed.csv")
except FileNotFoundError:
    print("❌ Fichier sample_train_imputed.csv non trouvé. Vérifiez le nom et l'emplacement.")
    exit()

# 📌 Vérifier si les colonnes nécessaires existent
required_columns = ["SK_ID_CURR", "TARGET"]
for col in required_columns:
    if col not in donnees_train.columns:
        print(f"❌ La colonne {col} est manquante dans le fichier d'entraînement.")
        exit()

# 📌 Fonction d'entraînement du modèle
def train_model():
    X = donnees_train.drop(columns=["TARGET", "SK_ID_CURR"])
    y = donnees_train["TARGET"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    accuracy = accuracy_score(y_test, model.predict(X_test))
    print(f"🎯 Précision du modèle : {accuracy * 100:.2f}%")
    
    return model

# 📌 Entraîner et charger le modèle
model = train_model()

# 📌 Fonction pour récupérer le modèle
def get_trained_model():
    return model
