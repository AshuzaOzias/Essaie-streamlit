import streamlit as st
from streamlit.components.v1 import html
from PIL import Image
import time
import os

# Page Configuration
st.set_page_config(
    page_title="Bienvenue !",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Styles CSS
def set_css():
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Lobster&family=Poppins:wght@300;400;600&display=swap');

        body {
           background-color: #ffebcd !important;
           color: #000000 !important;
           font-family: 'Times New Roman', Times, serif !important;
        }
        .main-header {
            font-size: 48px;
            color: #3b6978;
            font-family: 'Lobster', cursive;
            text-align: center;
            margin-top: 20px;
            animation: fadeInDown 1.5s;
        }
        .page-section {
            padding: 30px;
        }
        .btn {
            background-color: #3b6978;
            color: green;
            padding: 10px 20px;
            border-radius: 5px;
            text-decoration: none;
            font-weight: bold;
        }
        .btn:hover {
            background-color: #284b63;
            text-decoration: underline;
        }
        .social-icons img {
            width: 24px;
            margin-right: 10px;
            transition: transform 0.3s ease;
        }
        .social-icons img:hover {
            transform: scale(1.2);
        }
        @keyframes fadeInDown {
            0% {
                opacity: 0;
                transform: translateY(-20px);
            }
            100% {
                opacity: 1;
                transform: translateY(0);
            }
        }
        </style>
        """,
        unsafe_allow_html=True
    )

set_css()

# Sidebar Navigation
st.sidebar.title("Menu")
 mon_chemin_relatif = "A1.jpg"
    mon_chemin_absolu = os.path.abspath(mon_chemin_relatif)
    st.image(mon_chemin_absolu)
pages = ["Accueil", "Page 1 : Découverte", "Page 2 : Services", "Page 3 : Ressources", "À Propos"]
selected_page = st.sidebar.radio("Navigation", pages)

# Fonction pour afficher des animations simples en HTML
def animated_text(message):
    html_content = f"""
    <div style="font-size: 20px; animation: fadeInDown 1.5s;">{message}</div>
    """
    st.markdown(html_content, unsafe_allow_html=True)

# Accueil
if selected_page == "Accueil":
    st.markdown("<h1 class='main-header'>🌿 Bienvenue à notre Application Streamlit 🦺🌸🦺</h1>", unsafe_allow_html=True)
    mon_chemin_relatif = "A6.jpg"
    mon_chemin_absolu = os.path.abspath(mon_chemin_relatif)
    st.image(mon_chemin_absolu)
    st.write("Explorez notre application à travers les différentes pages en utilisant le menu à gauche 👈.")
    animated_text("Commencez votre exploration maintenant !")

# Page 1 : Découverte
elif selected_page == "Page 1 : Découverte":
    st.header("🌍 Découvrez un monde inspirant")
    st.write("Découvrez des paysages magnifiques et des informations enrichissantes sur la nature.")
    mon_chemin_relatif = "chien.jpg"
    mon_chemin_absolu = os.path.abspath(mon_chemin_relatif)
    st.image(mon_chemin_absolu)
    st.write("La nature est un livre ouvert rempli d'aventures et de mystères. Cherchez, apprenez, découvrez.")

# Page 2 : Services
elif selected_page == "Page 2 : Services":
    st.header("✨ Nos Services")
    services = ["Des visites guidées", "Des ateliers éducatifs", "Des programmes interactifs"]
    for service in services:
        st.subheader(f"✔️ {service}")
     mon_chemin_relatif = "F1.jpg"
    mon_chemin_absolu = os.path.abspath(mon_chemin_relatif)
    st.image(mon_chemin_absolu)

# Page 3 : Ressources
elif selected_page == "Page 3 : Ressources":
    st.header("📚 Ressources Utiles")
    st.write("Voici une liste de sites et d'outils pour explorer la beauté et préserver la nature.")
    links = {
        "National Geographic": "https://www.nationalgeographic.com/",
        "WWF (World Wildlife Fund)": "https://www.worldwildlife.org/",
        "Earth Justice": "https://earthjustice.org/"
    }
    for name, url in links.items():
        st.markdown(f"[{name}]({url})", unsafe_allow_html=True)
     mon_chemin_relatif = "PHOTO13.jpeg"
    mon_chemin_absolu = os.path.abspath(mon_chemin_relatif)
    st.image(mon_chemin_absolu)
# Page 4 : À Propos des Créateurs
elif selected_page == "À Propos":
    st.header("👨‍💻 À Propos des Créateurs🦺")
    st.write("Nous sommes une équipe de trois développeurs passionnés par la technologie et la nature.")
    creators = [
        {
            "name": "ASHUZA KULIMUSHI Ozias",
            "bio": "Développeur full-stack , passionnée par l'UI/UX et designer web.",
            "phone": "+243 971 418 729",
            "email": "ashuzaozias@uob.ac.cd",
            "linkedin": "https://linkedin.com/in/ashuzaozias",
            "twitter": "https://twitter.com/@oziasashuza"
        },
        {
            "name": "MAPENDANO NTUGULO Lebon",
            "bio": "Développeur back-end avec un amour pour la nature et la randonnée.",
            "phone": "+243 973 715 123",
            "email": "lebonroy2@gmail.com",
            "linkedin": "https://linkedin.com/in/lebonRoy",
            "twitter": "https://twitter.com/lebonRoy"
        },
        {
            "name": "USHINDI RUGAMIKA Jonathan",
            "bio": "Chef de projet full-stack spécialisé.",
            "phone": "+243 992 766 814",
            "email": "ushindirugamikajonathan@gmail.com",
            "linkedin": "https://linkedin.com/in/ushindijonathan",
            "twitter": "https://twitter.com/@ushindijonathan"
        }
    ]
    for creator in creators:
        st.subheader(creator["name"])
        st.write(creator["bio"])
        st.write(f"📞 {creator['phone']}")
        st.write(f"📧 [Email]({creator['email']})")
        st.write(
            "🔗 Réseaux : "
            
        )

        # Contenu des liens des médias sociaux
        les_medias_sociaux = f'''
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">

        <style>
            .icon_container {{
                display: flex; /* Affichage en ligne */
                flex-wrap: wrap; /* Permet de passer à la ligne si l'espace est insuffisant */
                gap: 15px; /* Espace entre les icônes */
                margin: 20px 0; /* Marge autour de l'ensemble */
            }}

            .icon_lien {{
                display: inline-flex; /* Affichage en ligne */
                align-items: center; /* Aligne verticalement les icônes et le texte */
                text-decoration: none;
                font-family: 'Lucida Sans';
                color: inherit; /* Utilise la couleur de l'icône définie */
            }}

            span {{
                margin-right: 8px; /* Espacement entre l'icône et le texte */
            }}

            .fa-facebook {{
                color: blue;
            }}

            .fa-instagram {{
                color: red;
            }}

            .fa-twitter {{
                color: rgb(77, 158, 245);
            }}

            .fa-tiktok {{
                color: black; /* Couleur Tiktok */
            }}

            .fa-linkedin {{
                color: #0077b5; /* Couleur LinkedIn */
            }}

            .fa-whatsapp {{
                color: #25D366; /* Couleur WhatsApp */
            }}

            .fa-github {{
                color: black; /* Couleur GitHub */
            }}

            .fa-envelope {{
                color: #EA4335; /* Couleur Gmail */
            }}
        </style>

        <div class="icon_container">
            <a href="https://www.facebook.com/mon_lien_facebook" class="icon_lien" target="_blank"><span class="fab fa-facebook"></span>{creator["name"]} Facebook</a>
            <a href="https://www.instagram.com/mon_lien_instagram" class="icon_lien" target="_blank"><span class="fab fa-instagram"></span>{creator["name"]} Instagram</a>
            <a href="https://twitter.com/mon_lien_twitter" class="icon_lien" target="_blank"><span class="fab fa-twitter"></span>{creator["name"]} Twitter</a>
            <a href="https://www.tiktok.com/@mon_lien_tiktok" class="icon_lien" target="_blank"><span class="fab fa-tiktok"></span>{creator["name"]} Tiktok</a>
            <a href="https://www.linkedin.com/in/mon_lien_linkedin" class="icon_lien" target="_blank"><span class="fab fa-linkedin"></span>{creator["name"]} Linkedin</a>
            <a href="https://wa.me/mon_lien_whatsapp" class="icon_lien" target="_blank"><span class="fab fa-whatsapp"></span>{creator["name"]} Whatsapp</a>
            <a href="mailto:votre_email@gmail.com" class="icon_lien"><span class="fas fa-envelope"></span>{creator["name"]} Gmail</a>
            <a href="https://github.com/mon_lien_github" class="icon_lien" target="_blank"><span class="fab fa-github"></span>{creator["name"]} GitHub</a>
        </div>
        '''

        # Affichage des médias sociaux dans Streamlit
        st.markdown(les_medias_sociaux, unsafe_allow_html=True)

    st.image("A5.jpg", caption="Notre équipe")

# Footer
st.markdown("---")
st.markdown("<p style='text-align: center;'>🌸 Merci de visiter notre application Streamlit 💫 | Fait avec ❤️ par notre équipe.</p>", unsafe_allow_html=True)
st.balloons()
st.toast('CONGRATULATIONS!', icon='🎉')
with st.spinner('Wait for it...'):
    time.sleep(5)
st.success("Done!")
