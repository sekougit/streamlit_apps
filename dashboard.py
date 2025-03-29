import streamlit as st
import numpy as np
import pandas as pan
import plotly.express as px
import matplotlib.pyplot as plt
import re
import random as rd
from models_scoring import get_trained_model, train_model  # Assurez-vous que cette fonction existe et fonctionne bien
# Importer le modèle entraîné
#import sys
#C:/Users/Sekou Drame/Desktop/EXCEL/EXCEL_AS1
donnees = pan.read_csv("sample_test_imputed.csv")
bon_base = pan.DataFrame(donnees)
base_sample = bon_base.sample(50)
list_id = base_sample['SK_ID_CURR'].unique().tolist()

# Charger le modèle entraîné (fonction supposée exister)
model = get_trained_model()  # Ici, tu dois t'assurer que cette fonction renvoie un modèle entraîné

def main():
    st.sidebar.checkbox("Bienvenu dans le menu de l'application", False)
    st.sidebar.write("Bienvenu dans le menu de l'application")
    option = st.sidebar.radio("Faites votre choix", ["Accueil", "Données", "Prédiction"])
    id = st.sidebar.selectbox("Veuillez choisir l'ID", list_id)
    
    if option == "Accueil":
        st.title("Application de prédiction de scoring crédit")
        st.markdown('''
            **La mise en application du scoring de crédit est essentielle pour optimiser l’octroi de prêts en réduisant les risques financiers
            pour les institutions bancaires et de microfinance. En utilisant un modèle de machine learning, il devient possible d’évaluer rapidement et
            objectivement la solvabilité d’un individu en se basant sur des données historiques et des critères prédictifs. Cela permet non seulement d’accélérer
            le processus de décision, mais aussi d’améliorer l’inclusion financière en offrant des opportunités de crédit à des personnes qui pourraient être exclues
            par les méthodes traditionnelles d’évaluation. De plus, un système automatisé de scoring réduit les biais humains et renforce la transparence des décisions,
            contribuant ainsi à une meilleure gestion du risque et à une relation de confiance entre prêteurs et emprunteurs.**''')

    if option == "Données":
        st.title("Partie pour les visualisations de tableau de données automatiques")
        st.subheader("Auteur: Sèkou Dramé")
        st.write("Tableau de données des élèves de la classe AS1")
        st.write("Dans cette base, nous avons ", len(base_sample), " individus.")
        st.write(base_sample)

    if option == "Prédiction":
        infos=base_sample[base_sample["SK_ID_CURR"] == id].T
        st.write(infos)
        # Prédiction
        if st.button("Prédire la solvabilité"):
            input_data = base_sample[base_sample["SK_ID_CURR"] == id].drop(columns=["TARGET", "SK_ID_CURR"]).values
            prediction = model.predict(input_data)[0]

            if prediction == 1:
                st.success("✅ Crédit accepté !")
            else:
                st.error("❌ Crédit refusé.")

if __name__ == '__main__':
    main()
