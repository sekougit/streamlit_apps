import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
from models_scoring import get_trained_model  # Importer le modèle depuis model.py

# 📌 Charger les données de test
try:
    donnees_test = pd.read_csv("sample_test_imputed.csv")
except FileNotFoundError:
    st.error("❌ Fichier sample_test_imputed.csv non trouvé.")
    st.stop()

# 📌 Vérifier si les colonnes essentielles existent
required_columns = ["SK_ID_CURR", "TARGET"]
for col in required_columns:
    if col not in donnees_test.columns:
        st.error(f"❌ La colonne {col} est absente du fichier de test.")
        st.stop()

# 📌 Préparer un échantillon de données
base_sample = donnees_test.sample(50, random_state=42)
list_id = base_sample["SK_ID_CURR"].unique().tolist()

# 📌 Charger le modèle
model = get_trained_model()

# 📌 Interface Streamlit
def main():
    st.sidebar.write("Bienvenue dans le menu de l'application")
    option = st.sidebar.radio("Faites votre choix", ["Accueil", "Données", "Prédiction"])
    id = st.sidebar.selectbox("Veuillez choisir l'ID client", list_id)

    if option == "Accueil":
        st.title("Application de prédiction de scoring crédit")
        st.markdown("""
            **L'application de scoring de crédit aide à évaluer la solvabilité des individus à l'aide d'un modèle de Machine Learning.
            Cela accélère le processus de décision et améliore l'inclusion financière tout en réduisant les biais humains.**
        """)

    elif option == "Données":
        st.title("Visualisation des données")
        st.subheader("Auteur: Sèkou Dramé")
        st.write(f"Base de données avec {len(base_sample)} individus")
        st.write(base_sample)

    elif option == "Prédiction":
        infos = base_sample[base_sample["SK_ID_CURR"] == id].T
        st.write(infos)

        if st.button("Prédire la solvabilité"):
            try:
                input_data = base_sample[base_sample["SK_ID_CURR"] == id].drop(columns=["TARGET", "SK_ID_CURR"]).values
                prediction = model.predict(input_data)[0]

                if prediction == 1:
                    st.success("✅ Crédit accepté !")
                else:
                    st.error("❌ Crédit refusé.")
            except Exception as e:
                st.error(f"Erreur de prédiction : {e}")

if __name__ == '__main__':
    main()
