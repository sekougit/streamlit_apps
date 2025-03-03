import streamlit as st
import numpy as np
import pandas as pan
import plotly.express as px
import matplotlib.pyplot as plt
import re
import random as rd
from sklearn.linear_model import LinearRegression
#from streamlit_option_menu import option_menu
#from numerize.numerize import numerize
import query

st.set_page_config(page_title="Tableau de bord",page_icon=":bar_chart:",layout="wide")

donnees=pan.read_csv("export.csv")
bon_base=pan.DataFrame(donnees)
Moyenne_1=bon_base["Moyenne_1S"]
Moyenne_2=bon_base["Moyenne_2S"]
Moyenne_T=bon_base["Moyenne_A"]
def  modif(x):
    liste=["Passable","Assez Bien","Bien","Trés Bien","Faible"]
    if x<10:
        return liste[4]
    
    elif (x>=10 and x<12):
        return liste[0]

    elif (x>=12 and x<14):
        return liste[1]

    elif (x>=14 and x<16):
        return liste[2]

    elif (x>=16 and x<18):
        return liste[3]

bon_base["Mention_1S"]=Moyenne_1.apply(lambda x: modif(x))
bon_base["Mention_2S"]=Moyenne_2.apply(lambda x: modif(x))
bon_base["Mention_A"]=Moyenne_T.apply(lambda x: modif(x))

def main():

    #st.dataframe(bon_base)C:/Users/Sekou Drame/Data_science.jpg
    st.sidebar.image("https://t4.ftcdn.net/jpg/02/62/17/37/360_F_262173764_3sxll45SOaGP5uEC7PukV3LHOB7H8dp2.jpg",caption="IMAGE")
    option=st.sidebar.radio("Faites votre choix",["Home","Données","Filtre","Statistiques","Graphique","Graphique pour filtre"])

    st.sidebar.header("Filter par ici:")
    res=st.sidebar.checkbox("Restaurer la base",False)
    res_1=st.sidebar.checkbox("Filtrer par nationalité",False)
    res_2=st.sidebar.checkbox("Filtrer par sexe",False)
    nationalite_f=st.sidebar.multiselect("Filtre par nationalité",options=bon_base["nationalité"].unique(),default=bon_base["nationalité"].unique())
    sexe_f=st.sidebar.multiselect("Filtre par sexe",options=bon_base["sexe"].unique(),default=bon_base["sexe"].unique())
    nationalite=st.sidebar.selectbox("Filtre par nationalité",options=bon_base["nationalité"].unique().tolist())
    sexe=st.sidebar.selectbox("Filtre par sexe",options=bon_base["sexe"].unique().tolist())
    moyenne=st.sidebar.selectbox("Choisissez la moyenne par semestre ou annuelle",options=["Moyenne_1S","Moyenne_2S","Moyenne_A"])
    mention=st.sidebar.selectbox("Choisissez l'appréciation par semestre ou annuelle",options=["Mention_1S","Mention_2S","Mention_A"])
    bourse=st.sidebar.selectbox("Choisissez la part de la bourse",options=["bourse_sexe","bourse_nationalité"])
    sexe_natio=st.sidebar.selectbox("Choisissez sexe ou nationalité",options=["sexe","nationalité"])


    #base nationalité
    b_n_1=bon_base[bon_base["nationalité"]==str(nationalite)]

    #base sexe
    b_n_2=bon_base[bon_base["sexe"]==str(sexe)]

    base_filtre=bon_base.query("nationalité==@nationalite_f & sexe==@sexe_f")

    #base nationalité et sexe
    cond1=bon_base["nationalité"]==str(nationalite)
    cond2=bon_base["sexe"]==str(sexe)
    
    b_n_3=bon_base[cond1 & cond2]

    if option=="Home":
        st.title("Application de visualisation de données interactif")
        #text="De nos jours avec le flux importants de donnees que dispose toute entité,une analyse de ces données devient judicieux afin de tirer des informations pertinentes pour ameliorer le developpement de l'entité.De ce fait cette application est concue dans le but de realiser ces analyses de manière automatique "
        #st.write(text) 
        st.markdown(''':blue[**De nos jours avec le flux importants de donnees que dispose les entrepises,
                    une analyse de ces données devient judicieux afin de tirer des informations
                    pertinentes pour ameliorer le developpement de l'entreprise.De ce fait cette 
                    application est concue dans le but de realiser ces analyses automatiquement**]''')
    if option=="Données": 
        st.title("Partie pour les visualisation  de tableau de données automatiques")
        st.subheader("Auteur: Sèkou Dramé")
        st.subheader("Tabeau de données des élèves de la classe AS1")
        if res and nationalite in bon_base["nationalité"].unique().tolist() and sexe in bon_base["sexe"].unique().tolist():
            st.write("Dans cette classe on a ",len(bon_base["sexe"].tolist()),"élèves.")
            st.write(bon_base)
        if res_1:
            st.write("Dans cette classe on a ",len(b_n_1["sexe"].tolist()),str(nationalite),".")
            st.write(b_n_1)
        if res_2:
            st.write("Dans cette classe on a ",len(b_n_2["sexe"].tolist()),"élèves de sexe",str(sexe),".")
            st.write(b_n_2)

    if option=="Filtre":
        st.title("Partie pour les filtres avancés du tableau de données")
        st.subheader("Tabeau de données des élèves de la classe AS1")
        st.write("Dans la base il y'a ",len(base_filtre["sexe"]),"individus maintenant")
        st.write(base_filtre)
    #partage de l'application en colonne
    if option=="Statistiques":
        col1,col2,col3=st.columns(3)
        with col1:
            st.subheader("Nationalité",divider="blue")
            st.subheader(f"Moyenne {str(nationalite)}")
            #st.subheader(str(nationalite))
            st.subheader(round(b_n_1[str(moyenne)].mean(),3))

            st.subheader(f"Bourse(F CFA) moyenne {str(nationalite)}")
            st.subheader(round(b_n_1["bourse"].mean(),3))

            st.subheader(f"Age moyen {str(nationalite)}")
            st.subheader(round(b_n_1["age"].mean(),1))


        with col2:
            st.subheader("Sexe",divider="blue")
            st.subheader(f"Moyenne sexe {str(sexe)}")
            #st.subheader(str(sexe))
            st.subheader(round(b_n_2[str(moyenne)].mean(),3))

            st.subheader(f"Bourse(F CFA) moyenne sexe {str(sexe)}")
            st.subheader(round(b_n_2["bourse"].mean(),3))

            st.subheader(f"Age moyen sexe {str(sexe)}")
            st.subheader(round(b_n_2["age"].mean(),1))


        with col3:
            st.subheader("Nationalité et Sexe",divider="blue")
            st.subheader(f"Moyenne {str(nationalite)} de sexe {str(sexe)}")
            #st.subheader(str(nationalite),str(sexe))
            st.subheader(round(b_n_3[str(moyenne)].mean(),3))
            
            st.subheader(f"Bourse(F CFA) moyenne {str(nationalite)} de sexe {str(sexe)}")
            st.subheader(round(b_n_3["bourse"].mean(),3))

            st.subheader(f"Age moyen {str(nationalite)} de sexe {str(sexe)}")
            st.subheader(round(b_n_3["age"].mean(),1))

        
    if option=="Graphique":
        #graph2,
        graph1,graph3=st.columns(2)
        fig_1=px.bar(data_frame=base_filtre,y=base_filtre[str(mention)].unique().tolist(),x=base_filtre[str(mention)].value_counts().tolist(),orientation="h",title="Répartition des élèves par "+str(mention))
        graph1.plotly_chart(fig_1,use_container_width=True)

        #fig_2=px.bar(data_frame=bon_base,x=bon_base[str(mention)].unique().tolist(),y=bon_base[str(mention)].value_counts().tolist(),title="Répartition des élèves par "+str(mention))
        #graph2.plotly_chart(fig_2,use_container_width=True)

        fig_pie_3=px.pie(names=base_filtre[str(sexe_natio)].unique().tolist(),values=base_filtre[str(sexe_natio)].value_counts().tolist())
        graph3.plotly_chart(fig_pie_3,use_container_width=True)

    if option=="Graphique pour filtre":
        graph4,graph5=st.columns(2)
        fig_4=px.bar(data_frame=base_filtre,x=base_filtre[str(mention)].unique().tolist(),y=base_filtre[str(mention)].value_counts().tolist(),title="Répartition des élèves par "+str(mention))
        graph4.plotly_chart(fig_4,use_container_width=True)

        fig_pie_5=px.pie(names=base_filtre[str(sexe_natio)].unique().tolist(),values=base_filtre[str(sexe_natio)].value_counts().tolist())
        graph5.plotly_chart(fig_pie_5,use_container_width=True)
if __name__=='__main__':
    main()