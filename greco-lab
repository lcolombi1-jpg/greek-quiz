import streamlit as st
import random

st.set_page_config(page_title="Greco Lab", page_icon="🎓", layout="wide")

# --- SIDEBAR ---
with st.sidebar:
    st.title("Pannello Studente")
    st.info("Completa l'analisi e scegli la traduzione corretta per ogni verbo proposto.")
    # Esempio di contatore progressivo
    progresso = st.progress(0)

# --- DATABASE ---
if 'quiz' not in st.session_state:
    # Lista originale dal tuo file Word[cite: 1]
    raw_data = [
        {"gr": "ἤγγελλε", "tr": "Annunciava", "an": "3 xs sing a imperfetto indicativo"},
        {"gr": "γιγνώσκειν", "tr": "Conoscere", "an": "infinito presente attivo"},
        {"gr": "εἶχον", "tr": "Io avevo", "an": "1 xs sing impf ind"},
        {"gr": "ἴσθι", "tr": "Sii tu", "an": "2 xs sing imperativo pres att"}
    ]
    # Mischiamo le domande all'inizio della sessione
    random.shuffle(raw_data)
    st.session_state.quiz = raw_data

st.title("🏛️ Laboratorio di Morfologia Greca")

# --- ESERCIZI ---
risposte_date = 0
for i, q in enumerate(st.session_state.quiz):
    # Usiamo un contenitore elegante per ogni domanda
    with st.container(border=True):
        col1, col2 = st.columns([1, 2])
        
        with col1:
            st.markdown(f"### `{q['gr']}`")
            # Un piccolo aiuto espandibile
            with st.expander("💡 Suggerimento"):
                st.write(f"Il verbo base è: `{q['gr']}`") # Qui potresti mettere il paradigma
        
        with col2:
            st.text_input("Analisi morfologica:", key=f"an_{i}", placeholder="es: 3 sing pres ind...")
            st.radio("Traduzione corretta:", ["Opzione A", "Opzione B", q['tr']], key=f"tr_{i}", index=None, horizontal=True)
            
        # Calcolo progresso
        if st.session_state.get(f"tr_{i}"):
            risposte_date += 1

# Aggiorna barra progresso
progresso.progress(risposte_date / len(st.session_state.quiz))

# --- PULSANTE FINALE ---
if st.button("Consegna il compito 📝", use_container_width=True):
    # Logica di correzione...
    st.balloons()
    st.success("Analisi completata! Controlla i risultati qui sotto.")
