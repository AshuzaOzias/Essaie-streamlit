import streamlit as st
from streamlit.components.v1 import html
from PIL import Image
import time

# Page Configuration
st.set_page_config(
    page_title="Bienvenue !",
    page_icon="🌸",
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
    st.image("C:/Users/MWAMI/Downloads/A6.jpg", caption="La beauté de la nature", use_column_width=True)
    st.write("Explorez notre application à travers les différentes pages en utilisant le menu à gauche 👈.")
    animated_text("Commencez votre exploration maintenant !")

# Page 1 : Découverte
elif selected_page == "Page 1 : Découverte":
    st.header("🌍 Découvrez un monde inspirant")
    st.write("Découvrez des paysages magnifiques et des informations enrichissantes sur la nature.")
    st.image("C:/Users/MWAMI/Downloads/chien.jpg")
    st.write("La nature est un livre ouvert rempli d'aventures et de mystères. Cherchez, apprenez, découvrez.")

# Page 2 : Services
elif selected_page == "Page 2 : Services":
    st.header("✨ Nos Services")
    services = ["Des visites guidées", "Des ateliers éducatifs", "Des programmes interactifs"]
    for service in services:
        st.subheader(f"✔️ {service}")
    st.image("https://source.unsplash.com/800x600/?tourism,education")

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
            f"[LinkedIn]({creator['linkedin']}) | "
            f"[Twitter]({creator['twitter']})"
        )

    st.image("https://source.unsplash.com/800x300/?team,technology", caption="Notre équipe")

# Footer
st.markdown("---")
st.markdown("<p style='text-align: center;'>🌸 Merci de visiter notre application Streamlit 💫 | Fait avec ❤️ par notre équipe.</p>", unsafe_allow_html=True)
st.balloons()
st.toast('CONGRATULATIONS!', icon='🎉')
with st.spinner('Wait for it...'):
    time.sleep(5)
st.success("Done!")