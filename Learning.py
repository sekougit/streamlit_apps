import streamlit as st
import numpy as np
import pandas as pan
import plotly.express as px
import matplotlib.pyplot as plt
import re
import random as rd
from sklearn.linear_model import LinearRegression
#import sys
#C:/Users/Sekou Drame/Desktop/EXCEL/EXCEL_AS1
donnees=pan.read_excel("parrain.xlsx",sheet_name="export",usecols="A,B,E,F,G,H,I,J,K")
bon_base=pan.DataFrame(donnees)
#bon_base=base.rename({"moyenne_1":"Moyenne_1S","moyenne_2":"Moyenne_2S","moyenne_t":"Moyenne_A"})
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

    st.sidebar.checkbox("Bienvenu dans le menu de l'application",False)
    st.sidebar.write("Bienvenu dans le menu de l'application") 
    option=st.sidebar.radio("Faites votre choix",["Home","Données","Graphique","filtre","Regression"]) 
    if option=="Home":

        st.title("Application de visualisation de données interactif")
        #text="De nos jours avec le flux importants de donnees que dispose toute entité,une analyse de ces données devient judicieux afin de tirer des informations pertinentes pour ameliorer le developpement de l'entité.De ce fait cette application est concue dans le but de realiser ces analyses de manière automatique "
        #st.write(text) 
        st.markdown(''':blue[**De nos jours avec le flux importants de donnees que dispose les entrepises,
                    une analyse de ces données devient judicieux afin de tirer des informations
                    pertinentes pour ameliorer le developpement de l'entreprise.De ce fait cette 
                    application est concue dans le but de realiser ces analyses automatiquement**]''') 
        #st.image("C:\Users\Sekou Drame\moncodepython\tableau_bord.jpg",caption="Tableau de Bord Excel")
    if option=="Données":
        st.title("Partie pour les visualisation  de tableau de données automatiques")
        st.subheader("Auteur: Sèkou Dramé")
        st.write("Tabeau de données des élèves de la classe AS1")

        
        st.write("Dans cette base on a ",len(bon_base["sexe"].tolist()),"individus.")
        st.write(bon_base)
        
        dict_1={"abscisse":np.arange(len(bon_base["sexe"].tolist())).tolist(),
                "moyenne_1":bon_base["Moyenne_1S"].tolist(),
                "moyenne_2":bon_base["Moyenne_2S"].tolist(),
                "moyenne_T":bon_base["Moyenne_A"].tolist(),
                "age":bon_base["age"].tolist(),
                "bourse":bon_base["bourse"].tolist(),
                "Mention_1":bon_base["Mention_1S"].tolist(),
                "mention_2":bon_base["Mention_2S"].tolist(),
                "Mention_T":bon_base["Mention_A"].tolist(),
                "sexe":bon_base["sexe"].tolist(),
                "nationalité":bon_base["nationalité"].tolist()} 
        
        base_1=pan.DataFrame(dict_1)
        
        choix_ordonnees=st.selectbox("Choisissez la variable de l'axe des ordonnées",["moyenne_1","moyenne_2","moyenne_T","age","bourse"])
        ma_couleur=st.selectbox("Choix de la variable catégorielle de la couleur",["Mention_1","Mention_2","Mention_T","sexe"])
        ma_fig=px.scatter(data_frame=base_1,x="abscisse", y=str(choix_ordonnees),color=ma_couleur)
        
        st.plotly_chart(ma_fig)

    if option=="Graphique":
        st.title("Partie pour les visualisation automatiques")
        st.subheader("Auteur: Sèkou Dramé")
        st.write("Tabeau de données des élèves de la classe AS1")        
        st.write(bon_base)
        
        nom_de_la_liste=["sexe","nationalité","Mention_1S","Mention_2S","Mention_A","bourse_nationalité","bourse_sexe"]
        var=st.selectbox("Faites un choix parmi cette liste",nom_de_la_liste)
        mes_couleurs=["#FF0000","#32CD32","#FFFF00","#FF8C00","#0000FF","#FD6C9E"]

        if var=="sexe" or var=="nationalité" or var=="Mention_1S" or var=="Mention_2S" or var=="Mention_A":
                premier="Répartition des élèves par " + str(var)
                st.write(premier)
                barre=pan.DataFrame(bon_base[var].value_counts().tolist(),bon_base[var].unique().tolist())
                #st.bar_chart(barre,color=mes_couleurs[len(base[var].unique().tolist())-1])
                st.bar_chart(barre,color=mes_couleurs[rd.randint(0,5)])
                

            
        if var=="bourse_nationalité" or var=="bourse_sexe":
                sep=str(var)
                sep_1=re.split("_",sep)
                groupe=bon_base.groupby([sep_1[1]]).agg({"bourse":"sum"})
                nom_col="Somme de la Bourse par "+str(sep_1[1])
                barre=pan.DataFrame({nom_col:groupe[sep_1[0]].tolist(),str(sep_1[1]):bon_base[sep_1[1]].unique().tolist()})
                fig_pie=px.pie(names=barre[str(sep_1[1])],values=barre[nom_col])
                st.write("Diagramme circulaire de la repartition de la part de la bourse par "+str(sep_1[1]))
                st.plotly_chart(fig_pie)
                #st.bar_chart(barre,color="#ffaa00")                

        
        
        st.write("Graphique avec matplotlib")
        fig_mat,ax_mat=plt.subplots()
        ax_mat.bar(bon_base["nationalité"].unique().tolist(),bon_base["nationalité"].value_counts().tolist(),color="green")
        plt.title("Répartition des élèves par nationalité de la classe AS1")
        plt.xlabel("Nationalité")
        plt.ylabel("Nombre Nationalité")
        st.pyplot(fig_mat)


        #liste_couleur=["Sexe","Mention"]
        #ma_couleur=st.selectbox("Faites un choix parmi cette liste",liste_couleur)
        #liste_base=["base_nationalité","base_sexe","base_mention"] 
        #choix_base=st.selectbox("Veuillez choisir une base",liste_base)
        
        base_nationalité={"nationalité":bon_base["nationalité"].unique().tolist(),"Nombre_Nationalité":bon_base["nationalité"].value_counts().tolist()}
        base_sexe={"sexe":bon_base["sexe"].unique().tolist(),"Nombre_Sexe":bon_base["sexe"].value_counts().tolist()}
        base_mention_1={"mention_1":bon_base["Mention_1S"].unique().tolist(),"Nombre_Mention_1":bon_base["Mention_1S"].value_counts().tolist()}
        base_mention_2={"mention_2":bon_base["Mention_2S"].unique().tolist(),"Nombre_Mention_2":bon_base["Mention_2S"].value_counts().tolist()}
        base_mention_T={"mention_T":bon_base["Mention_A"].unique().tolist(),"Nombre_Mention_T":bon_base["Mention_A"].value_counts().tolist()}
        
        liste_base=["base_nationalité","base_sexe","base_mention_1","base_mention_2","base_mention_T"]  
        button_base=st.selectbox("Choisissez une base",liste_base) 
        base_1=pan.DataFrame(base_nationalité)
        mes_cles=[]
        for i in base_nationalité:
        	mes_cles.append(i)
        	
        fig=px.bar(data_frame=base_1,x=str(mes_cles[0]),y=str(mes_cles[1]),title="Répartition des élèves par "+str(mes_cles[0]))
        st.plotly_chart(fig)    
    if option=="filtre":
        st.title("Partie pour les filtres automatiques")
        st.subheader("Auteur: Sèkou Dramé")
        st.write("Tabeau de données des élèves de la classe AS1")        
        st.write(bon_base)
        
        
        liste_filtre=["sexe","nationalité","Mention_1S","Mention_2S","Mention_A"]
        var=st.selectbox("Choisissez la variable de filtre",liste_filtre)
        var_filtre=bon_base[var].unique().tolist()
        var_1=st.selectbox("Choisissez la modalité de filtre",var_filtre)
        filtre=bon_base[bon_base[var]==str(var_1)]  
        st.write(filtre)
        
        graphe=["sexe","nationalité","Mention_1S","Mention_2S","Mention_A"]
        var_2=st.selectbox("Choisissez la variable a visualiser",graphe)
        
        
        #premier="Répartition des élèves par " + str(var)
        st.write("Visualisation du graphe")
        mes_couleurs_1=["#FF0000","#32CD32","#FFFF00","#FF8C00","#0000FF","#FD6C9E","#FFAA00"]
        
        barre=pan.DataFrame(filtre[var_2].value_counts().tolist(),filtre[var_2].unique().tolist())
        st.bar_chart(barre,color=mes_couleurs_1[rd.randint(0,6)])
    if option=="Regression":
        st.title("Partie pour le modéle de machine learning")
        st.subheader("Auteur: Sèkou Dramé")
        st.write("Ici on a un exemple de base sur les criquets: On cherche a savoir la relation entre la température et le nombre de leurs pulsations")
        exp_data=pan.DataFrame({"Température":[15,17,20,21,23,24,27,28,30,32,34],"Nombre_de_pulsation":[13.5,14.1,14.5,14.4,16.3,15.5,17.1,17.8,18.2,20.2,20.1]})
        st.write(exp_data)
        st.write("Nuages de points du nombre de pulsation en fonction de la température")
        fig_ex=px.scatter(data_frame=exp_data,x="Température",y="Nombre_de_pulsation")
        st.plotly_chart(fig_ex)
        boutton=st.button("le modele")
        if boutton: 
                X=np.array(exp_data["Température"].tolist()).reshape((11,1))
                Y=np.array(exp_data["Nombre_de_pulsation"].tolist()).reshape((11,1))
                mon_model=LinearRegression()
                mon_model.fit(X,Y)
                st.write("Le modéle a trouvé les paramétres suivants:")
                st.write("La pente: ",mon_model.coef_[0])
                st.write("L'ordonnée a l'origine: ",mon_model.intercept_)
                st.write("Le coefficient de determination: ",mon_model.score(X,Y))
                A=round(mon_model.score(X,Y)*100,3)
                st.write("Ce coefficient montre que",A," % de la variation du nombre de pulsation de ces criquets est expliqué par la variation de la température.")
        boutton_1=st.button("la prediction")
        if boutton_1:
                X=np.array(exp_data["Température"].tolist()).reshape((11,1))
                Y=np.array(exp_data["Nombre_de_pulsation"].tolist()).reshape((11,1))
                mon_model=LinearRegression()
                mon_model.fit(X,Y)
                a=mon_model.coef_[0]
                b=mon_model.intercept_ 
                exp_data_1=pan.DataFrame({"Température":[15,17,20,21,23,24,27,28,30,32,34]})
                exp_data_1["Prediction_Nombre_de_pulsation"]=exp_data_1["Température"].apply(lambda x:a*x+b)
                st.write("Base de la prédiction")
                st.write(exp_data_1)
if __name__=='__main__':
    main()
    