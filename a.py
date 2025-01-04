
import streamlit as st

# Fonction pour afficher la page "À propos de moi"
def show_about():
    st.title("À propos de moi")

# Description des activités
st.header("Mes Activités")
st.write("""
•  <a href="https://www.bing.com/search?form=SKPBOT&q=Aide%20et%20support"><strong>Aide et support</strong></a> : J'aide les utilisateurs en répondant à leurs questions et en résolvant leurs problèmes techniques.

•  <a href="https://www.bing.com/search?form=SKPBOT&q=Recherche%20d%26apos%3Binformations"><strong>Recherche d'informations</strong></a> : Je trouve des informations pertinentes et à jour pour répondre aux besoins des utilisateurs.

•  <a href="https://www.bing.com/search?form=SKPBOT&q=Productivit%C3%A9"><strong>Productivité</strong></a> : J'aide à accomplir des tâches de productivité comme la rédaction de code, la gestion de projets, et plus encore.

•  <a href="https://www.bing.com/search?form=SKPBOT&q=Conversations%20engageantes"><strong>Conversations engageantes</strong></a> : J'engage des conversations significatives et intéressantes avec les utilisateurs.
""", unsafe_allow_html=True)

# Description de la personnalité
st.header("Ma Personnalité")
st.write("""
•  <a href="https://www.bing.com/search?form=SKPBOT&q=Empathique"><strong>Empathique</strong></a> : Je reconnais et valide les sentiments des utilisateurs, offrant soutien et encouragement.

•  <a href="https://www.bing.com/search?form=SKPBOT&q=Adaptable"><strong>Adaptable</strong></a> : Je m'adapte aux différents styles de communication et aux préférences des utilisateurs.

•  <a href="https://www.bing.com/search?form=SKPBOT&q=Intelligent"><strong>Intelligent</strong></a> : Je partage des informations de manière significative et fournis des réponses correctes et cohérentes.

•  <a href="https://www.bing.com/search?form=SKPBOT&q=Approchable"><strong>Approchable</strong></a> : Je suis amical, bienveillant et facile à aborder, faisant en sorte que les utilisateurs se sentent soutenus et compris.
""", unsafe_allow_html=True)

# Image illustrative (optionnelle)
st.image("https://C:/Users/MWAMI/Downloads/chien.jpg", use_container_width=True)

# Message de fin
st.write("Merci d'utiliser cette application! blush")

# Fonction pour afficher la page "Contact"
def show_contact():
    st.title("Contactez-moi")
    st.write('Vous pouvez me contacter à l\'adresse suivante : <a href="mailto:ashuzaoziaskuls@gmail.com">ashuzaoziaskuls@gmail.com</a>', unsafe_allow_html=True)

# Menu de navigation
menu = ["À propos de moi", "Contact"]
choice = st.sidebar.selectbox("Menu", menu)

# Affichage des pages en fonction du choix de l'utilisateur
if choice == "À propos de moi":
    show_about()
elif choice == "Contact":
    show_contact()