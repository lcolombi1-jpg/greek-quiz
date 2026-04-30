import streamlit as st

# Configurazione della pagina
st.set_page_config(page_title="Laboratorio Greco", page_icon="📜")

st.title("📜 Laboratorio di Analisi e Traduzione")
st.write("""
Per ogni forma greca proposta:
1. Scrivi l'**analisi morfologica** completa (es. '3 sing impf ind att').
2. Scegli la **traduzione** corretta tra quelle proposte.
""")

# Database completo dal file Word
if 'quiz_completo' not in st.session_state:
    st.session_state.quiz_completo = [
        {"id": 1, "gr": "ἤγγελλε", "op": ["Annunciava", "Annunciare", "Annunziarono"], "cor_tr": "Annunciava", "cor_an": "3 xs sing a imperfetto indicativo"},
        {"id": 2, "gr": "γιγνώσκειν", "op": ["Conoscono", "Conoscere", "Conosciuto"], "cor_tr": "Conoscere", "cor_an": "infinito presente attivo"},
        {"id": 3, "gr": "εἶχον", "op": ["Io avevo", "Voi avevate", "Essi hanno"], "cor_tr": "Io avevo", "cor_an": "1 xs sing impf ind"},
        {"id": 4, "gr": "ἴσθι", "op": ["Sii tu", "Egli è", "Essere"], "cor_tr": "Sii tu", "cor_an": "2 xs sing imperativo pres att"},
        {"id": 5, "gr": "ἐβούλεσθε", "op": ["Voi volevate", "Loro volevano", "Voi volete"], "cor_tr": "Voi volevate", "cor_an": "2 xs sing impf a"},
        {"id": 6, "gr": "θνῄσκουσι", "op": ["Moriva", "Muoiono", "Morire"], "cor_tr": "Muoiono", "cor_an": "3 xs pl a pres ind"},
        {"id": 7, "gr": "λύεσθαι", "op": ["Sciogliere", "Essere sciolto", "Sciolto"], "cor_tr": "Essere sciolto", "cor_an": "infinito presente medio/passivo"},
        {"id": 8, "gr": "πίμπλης", "op": ["Io riempio", "Tu riempi", "Egli riempiva"], "cor_tr": "Tu riempi", "cor_an": "2 xs sing a pres ind"},
        {"id": 9, "gr": "ἵστασαν", "op": ["Loro collocavano", "Loro collocano", "Collocare"], "cor_tr": "Loro collocavano", "cor_an": "3 xs pl impf ind a"},
        {"id": 10, "gr": "ηὑρίσκετο", "op": ["Egli trovava", "Egli era trovato", "Trovarsi"], "cor_tr": "Egli era trovato", "cor_an": "3 xs sing impf ind mp"},
        {"id": 11, "gr": "κρινέσθω", "op": ["Sia giudicato lui!", "Egli giudica", "Giudicare"], "cor_tr": "Sia giudicato lui!", "cor_an": "3 xs sing mp imperativo pres"},
        {"id": 12, "gr": "εἱπόμεθα", "op": ["Noi seguivamo", "Voi seguite", "Noi seguiamo"], "cor_tr": "Noi seguivamo", "cor_an": "1 xs pl mp impf ind"},
        {"id": 13, "gr": "ἐδεικνύμην", "op": ["Io mostravo", "Io ero mostrato", "Mostrare"], "cor_tr": "Io ero mostrato", "cor_an": "1 xs sing mp impf ind"},
        {"id": 14, "gr": "ἀκουέτω", "op": ["Senta egli!", "Loro sentono", "Sentire"], "cor_tr": "Senta egli!", "cor_an": "3 xs sing imperativo pres att"},
        {"id": 15, "gr": "εἶναι", "op": ["Io sono", "Essere", "Sia egli"], "cor_tr": "Essere", "cor_an": "inf pres a"},
        {"id": 16, "gr": "ἐλαμβανόμην", "op": ["Io ero preso", "Io prendevo", "Prendere"], "cor_tr": "Io ero preso", "cor_an": "1 xs sing mp impf ind"},
        {"id": 17, "gr": "ἐγραφέτην", "op": ["Loro due scrivevano", "Voi due scrivete", "Scrivere"], "cor_tr": "Loro due scrivevano", "cor_an": "III duale impf a ind"},
        {"id": 18, "gr": "ᾀδόντων / ᾀδέτωσαν", "op": ["Loro cantano", "Cantino loro!", "Cantare"], "cor_tr": "Cantino loro!", "cor_an": "3 pl imperativo a pres"},
        {"id": 19, "gr": "τιθέασι", "op": ["Loro pongono", "Loro ponevano", "Porre"], "cor_tr": "Loro pongono", "cor_an": "3 pl ind pres a"},
        {"id": 20, "gr": "ἐδίδοσθον", "op": ["Voi due eravate dati", "Loro due danno", "Dare"], "cor_tr": "Voi due eravate dati", "cor_an": "II duale mp impf ind"},
        {"id": 21, "gr": "ἐνομίζεσθε", "op": ["Voi eravate ritenuti", "Voi ritenete", "Ritenere"], "cor_tr": "Voi eravate ritenuti", "cor_an": "2 xs sing mp impf ind"},
        {"id": 22, "gr": "φέρετον", "op": ["Portate voi due!", "Loro due portano", "Portare"], "cor_tr": "Portate voi due!", "cor_an": "II duale imperativo attivo"},
        {"id": 23, "gr": "ἐκέλευον", "op": ["Loro ordinavano", "Loro ordinano", "Ordinare"], "cor_tr": "Loro ordinavano", "cor_an": "3 pl a impf ind"},
        {"id": 24, "gr": "ἵεμαι", "op": ["Io sono mandato", "Io mando", "Mandare"], "cor_tr": "Io sono mandato", "cor_an": "1 xs sing mp pres ind"},
        {"id": 25, "gr": "πυνθάνεσθαι", "op": ["Informarsi", "Essere informato", "Informato"], "cor_tr": "Essere informato", "cor_an": "inf mp pres"},
        {"id": 26, "gr": "ἡγéου", "op": ["Tu guidavi", "Tu guidi", "Guidare"], "cor_tr": "Tu guidavi", "cor_an": "impf mp 2 xs sing"},
        {"id": 27, "gr": "ἐγίγνοντο", "op": ["Loro diventavano", "Loro diventano", "Diventare"], "cor_tr": "Loro diventavano", "cor_an": "impf mo 3 pl"},
        {"id": 28, "gr": "ἐστόν", "op": ["Loro due sono", "Voi due siete", "Essere"], "cor_tr": "Loro due sono", "cor_an": "III duale a pers ind"},
        {"id": 29, "gr": "ἔρριπτον", "op": ["Io scagliavo", "Io scaglio", "Scagliare"], "cor_tr": "Io scagliavo", "cor_an": "1 xs sing a impf ind"},
        {"id": 30, "gr": "δείκνυσθαι", "op": ["Mostrare", "Essere mostrato", "Mostrato"], "cor_tr": "Essere mostrato", "cor_an": "inf mp pres"}
    ]

# Ciclo di esercizi
for q in st.session_state.quiz_completo:
    st.subheader(f"Forma: {q['gr']}")
    
    # Slot per l'analisi (Testo libero)
    st.text_input(f"Inserisci l'analisi per {q['gr']}:", key=f"an_{q['id']}")
    
    # Radio per la traduzione
    st.radio(f"Scegli la traduzione per {q['gr']}:", q['op'], key=f"tr_{q['id']}", index=None)
    
    st.divider()

# Bottone di correzione
if st.button("Verifica Laboratorio", type="primary"):
    st.write("### Risultati della Verifica:")
    
    punti_tr = 0
    for q in st.session_state.quiz_completo:
        ans_studente = st.session_state.get(f"an_{q['id']}", "").strip().lower()
        tr_studente = st.session_state.get(f"tr_{q['id']}")
        
        # Controllo traduzione
        if tr_studente == q['cor_tr']:
            punti_tr += 1
            st.success(f"**{q['gr']}**: Traduzione corretta! ✅")
        else:
            st.error(f"**{q['gr']}**: Traduzione errata. Era: '{q['cor_tr']}' ❌")
            
        # Visualizzazione analisi corretta (senza punteggio automatico causa varianti di scrittura)
        st.info(f"💡 *Analisi attesa:* {q['cor_an']} | *Tua risposta:* {ans_studente}")
        st.write("---")
    
    st.metric("Traduzioni corrette", f"{punti_tr}/30")
