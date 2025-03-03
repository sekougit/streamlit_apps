import streamlit as st
import numpy as np
import pandas as pan
import random as rd
donnees=pan.read_excel("parrain.xlsx",sheet_name="python",usecols="B,C")
base=pan.DataFrame(donnees)
print(base)
def main():
    st.sidebar.checkbox("Bienvenu dans le menu de l'application",False)
    st.sidebar.write("Bienvenu dans le menu de l'application") 
    option=st.sidebar.radio("Faites votre choix",["Parrainage AS1","Parrainage ISEP1","Parrainage ISE-ECO","Parrainage ISE-MATHS"]) 
    if option=="Parrainage AS1":
        st.image("C:/Users/Sekou Drame/moncodepython/tableau_bord.jpg",caption="Tableau de Bord Excel")
        st.write(base)
        new=base["Prénoms_et_NOM"].tolist()
        old=base["NOM"].tolist()
        alea=rd.randint(0,22)
        alea_1=rd.randint(0,22)
        if st.button("Appuyer ici"):
            st.write("Le parrain:",old[alea])
            #filleuil.append(old[alea])

        if st.button("Appuyer de nouveau ici pour choix du parrain"):
            st.write("Le filleuil:",new[alea_1])

    if option=="Parrainage ISEP1":  
        st.image("C:/Users/Sekou Drame/moncodepython/tableau_bord.jpg",caption="Tableau de Bord Excel")
        st.write(base)
    if option=="Parrainage ISE-ECO":
        st.image("C:/Users/Sekou Drame/moncodepython/tableau_bord.jpg",caption="Tableau de Bord Excel")
        st.write(base)
    if option=="Parrainage ISE-MATHS":
        st.image("C:/Users/Sekou Drame/moncodepython/tableau_bord.jpg",caption="Tableau de Bord Excel")
        st.write(base)

if __name__=='__main__':
    main()     