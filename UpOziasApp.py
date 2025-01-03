import streamlit as st

# Fonction pour afficher la page "À propos de moi"
def show_about():
    st.title("À propos de moi")

# Description des activités
st.header("Mes Activités")
st.write("""
•  <a href="https://www.bing.com/search?form=SKPBOT&q=Aide%20et%20support">[**Aide et support**](https://www.bing.com/search?form=SKPBOT&q=Aide%20et%20support)</a> : J'aide les utilisateurs en répondant à leurs questions et en résolvant leurs problèmes techniques.

•  <a href="https://www.bing.com/search?form=SKPBOT&q=Recherche%20d%26apos%3Binformations">[**Recherche d'informations**](https://www.bing.com/search?form=SKPBOT&q=Recherche%20d%26apos%3Binformations)</a> : Je trouve des informations pertinentes et à jour pour répondre aux besoins des utilisateurs.

•  <a href="https://www.bing.com/search?form=SKPBOT&q=Productivit%C3%A9">[**Productivité**](https://www.bing.com/search?form=SKPBOT&q=Productivit%C3%A9)</a> : J'aide à accomplir des tâches de productivité comme la rédaction de code, la gestion de projets, et plus encore.

•  <a href="https://www.bing.com/search?form=SKPBOT&q=Conversations%20engageantes">[**Conversations engageantes**](https://www.bing.com/search?form=SKPBOT&q=Conversations%20engageantes)</a> : J'engage des conversations significatives et intéressantes avec les utilisateurs.
""", unsafe_allow_html=True)

# Description de la personnalité
st.header("Ma Personnalité")
st.write("""
•  <a href="https://www.bing.com/search?form=SKPBOT&q=Empathique">[**Empathique**](https://www.bing.com/search?form=SKPBOT&q=Empathique)</a> : Je reconnais et valide les sentiments des utilisateurs, offrant soutien et encouragement.

•  <a href="https://www.bing.com/search?form=SKPBOT&q=Adaptable">[**Adaptable**](https://www.bing.com/search?form=SKPBOT&q=Adaptable)</a> : Je m'adapte aux différents styles de communication et aux préférences des utilisateurs.

•  <a href="https://www.bing.com/search?form=SKPBOT&q=Intelligent">[**Intelligent**](https://www.bing.com/search?form=SKPBOT&q=Intelligent)</a> : Je partage des informations de manière significative et fournis des réponses correctes et cohérentes.

•  <a href="https://www.bing.com/search?form=SKPBOT&q=Approchable">[**Approchable**](https://www.bing.com/search?form=SKPBOT&q=Approchable)</a> : Je suis amical, bienveillant et facile à aborder, faisant en sorte que les utilisateurs se sentent soutenus et compris.
""", unsafe_allow_html=True)

# Image illustrative (optionnelle)
st.image("C:/Users/MWAMI/Downloads/PHOTO13.jpeg", use_container_width=True)

# Message de fin
st.write("Merci d'utiliser cette application! blush")

# Fonction pour afficher la page "Contact"
def show_contact():
    st.title("Contactez-moi")
    st.write("Vous pouvez me contacter à l'adresse suivante : example@example.com")

# Menu de navigation
menu = ["À propos de moi", "Contact"]
choice = st.sidebar.selectbox("Menu", menu)

# Affichage des pages en fonction du choix de l'utilisateur
if choice == "À propos de moi":
    show_about()
elif choice == "Contact":
    show_contact()