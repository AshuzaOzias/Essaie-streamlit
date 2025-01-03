import streamlit as st
from datetime import datetime
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import messagebox


# Informations de Mr ASHUZA KULIMUSHI Ozias
nom = "ASHUZA KULIMUSHI Ozias"
date_naissance = datetime(2002, 12, 27)
ville_naissance = "Bukavu/RDC"
passions = ["Engineering", "Musique", "Danse"] 
universite = "Université Officielle de Bukavu" 
annee_etude = "dernière année de licence"

# Calcul de l'âge 
aujourdhui = datetime.today() 
age = aujourdhui.year - date_naissance.year - ((aujourdhui.month, aujourdhui.day) < (date_naissance.month, date_naissance.day))  

# Configuration de la page 
st.set_page_config(page_title="Anniversaire de Ozias", page_icon="",layout="centered")

# Titre de l'application 
st.title(f"Joyeux Anniversaire {nom} !")  

 # Affichage des informations après devinette correcte ou trois tentatives 
if st.session_state.get('devine_correct'): 
    st.write(f"Mr. {nom} est né le {date_naissance.strftime('%d/%m/%Y')} à {ville_naissance}.") 
    st.write(f"Il est passionné par les domaines suivants : {', '.join(passions)}.") 
    st.write(f"Il est élève Ingénieur Civil des mines à l'{universite} en {annee_etude}.")  
 
# Diaporama de photos 
st.header("Photos de Mr. ASHUZA KULIMUSHI Ozias") 
photos = ["D:/Desktop/COURS L3 LMD GENIE MINIER/INITIATION A L'INTELLIGENCE ARTIFICIELLE/PHOTO1.jpg"]  
PHOTOS1 = st.file_uploader("Insere une photo")
img1 = Image.open(PHOTOS1) 
st.image(img1, caption=f"Photo de {nom}", use_container_width=True)
# Remplacez par les chemins réels des photos 
for photo in photos: 
    img = Image.open(photo) 
st.image(img, caption=f"Photo de {nom}", use_container_width=True)

# Section de devinette 
st.header("Devinez l'âge de Mr. ASHUZA KULIMUSHI Ozias")
devinette = st.text_input("Quel âge pensez-vous qu'il a AUJOURD'HUI ?") 
tentatives = st.session_state.get('tentatives', 0) 

if devinette:
    tentatives += 1 
    st.session_state['tentatives'] = tentatives 
    if int(devinette) == age:
        st.success("Bravo ! Vous avez deviné correctement.")
        st.session_state['devine_correct'] = True 
    elif tentatives >= 3:
        st.warning("Vous avez atteint le nombre maximum de tentatives mais vous n'avez pas encore deviné correctement.")
        st.session_state['devine_correct'] = True
    else: st.error("Désolé, ce n'est pas le bon âge. Essayez encore !") 
        
# Remerciements et réseaux sociaux
st.header("Remerciements") 
st.write("Merci à tous ceux qui ont visité cette application et souhaité un joyeux anniversaire à Mr. ASHUZA KULIMUSHI Ozias !") 
st.write("Vous pouvez le suivre sur ses réseaux sociaux :") 
st.write("[Facebook: Ozias Ashuza](https://www.facebook.com/OziasAhsuza)") 
st.write("[Instagram: @ozias_ashuza](https://www.instagram.com/ozias_ashuza)") 
st.write("[Twitter: ashuza kulimushi ozias](https://twitter.com/ashuza_kulimushi_ozias)") 
st.write("[TikTok: @ozias_as27](https://www.tiktok.com/@ozias_as27)") 
st.write("Emails : [ashuzaoziaskuls@gmail.com](mailto:ashuzaoziaskuls@gmail.com), [ashuzaozias@uob.ac.cd](mailto:ashuzaozias@uob.ac.cd)") 

 
#from PyQt5 import QtWidgets, uic
#import sys 

#class Ui(QtWidgets.QMain Window):
    #def_init_(self):
    #super(Ui,self)._init_()
    #uic.loadUi('design.ui',self)
    #app = QtWidgets.QApplication(sys.argv)
    #window = Ui()
    #app.exec_()
    
# Instructions pour partager l'application 
#st.write("Pour partager cette application, vous pouvez déployer votre application Streamlit en utilisant Streamlit Cloud ou tout autre service d'hébergement compatible. Voici comment faire avec Streamlit Cloud :") 
#st.write("1. Créez un compte sur [Streamlit Cloud](https://streamlit.io/cloud).") 
#st.write("2. Connectez votre dépôt GitHub contenant ce script.") 
#st.write("3. Déployez l'application et obtenez un lien partageable.")
#st.write('Bonjour Ozias')