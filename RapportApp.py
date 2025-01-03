import streamlit as st

# Définir les questions du quiz
quiz = [
{
"question": "Quelle est la capitale de la France?",
"options": ["Paris", "Londres", "Berlin", "Madrid"],
"answer": "Paris",
"explanation": "Paris est la capitale et la plus grande ville de France.",
"resource": "https://fr.wikipedia.org/wiki/Paris"
},
{
"question": "Quelle est la plus grande planète du système solaire?",
"options": ["Terre", "Mars", "Jupiter", "Saturne"],
"answer": "Jupiter",
"explanation": "Jupiter est la plus grande planète du système solaire avec un diamètre de 139 820 km.",
"resource": "https://fr.wikipedia.org/wiki/Jupiter_(plan%C3%A8te)"
},
{
"question": "Qui a écrit 'Les Misérables'?",
"options": ["Victor Hugo", "Émile Zola", "Gustave Flaubert", "Honoré de Balzac"],
"answer": "Victor Hugo",
"explanation": "Victor Hugo est l'auteur du roman 'Les Misérables', publié en 1862.",
"resource": "https://fr.wikipedia.org/wiki/Les_Mis%C3%A9rables"
}
]

# Initialiser les scores
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'question_index' not in st.session_state:
    st.session_state.question_index = 0

# Afficher la question actuelle
current_question = quiz[st.session_state.question_index]
st.header(f"Question {st.session_state.question_index + 1}")
st.write(current_question["question"])

# Afficher les options de réponse
options = current_question["options"]
selected_option = st.radio("Choisissez une réponse:", options)

# Bouton pour soumettre la réponse
if st.button("Soumettre"):
    if selected_option == current_question["answer"]:
        st.session_state.score += 1
        st.success("Bonne réponse!")
else:
    st.error("Mauvaise réponse.")

st.write(f"Explication: {current_question['explanation']}")
st.write(f"Ressource: [En savoir plus]({current_question['resource']})")

# Passer à la question suivante
if st.session_state.question_index < len(quiz) - 1:
    st.session_state.question_index += 1
else:
    st.write(f"Quiz terminé! Votre score final est {st.session_state.score}/{len(quiz)}")
    st.session_state.question_index = 0
    st.session_state.score = 0

# Afficher le score actuel
st.sidebar.write(f"Score: {st.session_state.score}/{len(quiz)}")