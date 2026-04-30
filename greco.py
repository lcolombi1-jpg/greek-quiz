import streamlit as st

# Configurazione della pagina per il Greco
st.set_page_config(page_title="Simulatore di Greco", page_icon="📜")

st.title("📜 Esercitazione di Morfologia Greca")
st.write("Analisi verbale: scegli la forma greca corretta per il verbo italiano indicato.")

# Database delle domande basato sul tuo file Word
if 'domande_greco' not in st.session_state:
    st.session_state.domande_greco = [
        {
            "id": 1,
            "italiano": "Annunciava",
            "analisi": "3ª pers. sing. impf. ind. att.",
            "opzioni": ["ἤγγελλε", "ἀγγέλλει", "ἤγγελλον", "ἀγγέλλοι"],
            "corretta": "ἤγγελλε"
        },
        {
            "id": 2,
            "italiano": "Conoscere",
            "analisi": "Infinito presente attivo",
            "opzioni": ["γιγνώσκειν", "γιγνώσκει", "γιγνώσκομεν", "γιγνώσκων"],
            "corretta": "γιγνώσκειν"
        },
        {
            "id": 3,
            "italiano": "Io avevo",
            "analisi": "1ª pers. sing. impf. ind. att.",
            "opzioni": ["ἔχω", "εἶχον", "ἔχει", "εἴχομεν"],
            "corretta": "εἶχον"
        },
        {
            "id": 4,
            "italiano": "Sii tu!",
            "analisi": "2ª pers. sing. imperativo pres. att.",
            "opzioni": ["εἶ", "ἴσθι", "ἔστω", "ἔστε"],
            "corretta": "ἴσθι"
        },
        {
            "id": 5,
            "italiano": "Voi volevate",
            "analisi": "2ª pers. plur. impf. ind. med/pass.",
            "opzioni": ["ἐβούλεσθε", "βούλεσθε", "ἐβούλοντο", "βούλοισθε"],
            "corretta": "ἐβούλεσθε"
        },
        {
            "id": 6,
            "italiano": "Muoiono",
            "analisi": "3ª pers. plur. pres. ind. att.",
            "opzioni": ["θνῄσκουσι", "ἔθνῃσκον", "θνῄσκει", "θνῄσκοιεν"],
            "corretta": "θνῄσκουσι"
        },
        {
            "id": 7,
            "italiano": "Essere sciolto",
            "analisi": "Infinito presente medio/passivo",
            "opzioni": ["λύειν", "λύεσθαι", "λύεται", "λύονται"],
            "corretta": "λύεσθαι"
        },
        {
            "id": 8,
            "italiano": "Tu riempi",
            "analisi": "2ª pers. sing. pres. ind. att.",
            "opzioni": ["πίμπλημι", "πίμπλης", "ἐπίμπλης", "πιμπλάναι"],
            "corretta": "πίμπλης"
        },
        {
            "id": 9,
            "italiano": "Loro collocavano",
            "analisi": "3ª pers. plur. impf. ind. att.",
            "opzioni": ["ἵστασαν", "ἵστανται", "ἵστατε", "ἵσταμεν"],
            "corretta": "ἵστασαν"
        },
        {
            "id": 10,
            "italiano": "Egli era trovato",
            "analisi": "3ª pers. sing. impf. ind. med/pass.",
            "opzioni": ["ηὑρίσκετο", "ηὑρίσκει", "εὑρίσκεται", "ηὑρίσκοντο"],
            "corretta": "ηὑρίσκετο"
        },
        {
            "id": 11,
            "italiano": "Noi seguivamo",
            "analisi": "1ª pers. plur. impf. ind. med/pass.",
            "opzioni": ["ἑπόμεθα", "εἱπόμεθα", "ἕπονται", "ἕπεσθε"],
            "corretta": "εἱπόμεθα"
        },
        {
            "id": 12,
            "italiano": "Essere",
            "analisi": "Infinito presente attivo",
            "opzioni": ["εἰμί", "εἶναι", "ὤν", "ἔσομαι"],
            "corretta": "εἶναι"
        }
    ]

# Ciclo per mostrare le domande
for q in st.session_state.domande_greco:
    st.subheader(f"Verbo: {q['italiano']}")
    st.write(f"**Analisi richiesta:** {q['analisi']}")
    
    st.radio(
        "Seleziona la forma greca corretta:",
        q['opzioni'],
        key=f"gr_{q['id']}",
        index=None
    )
    st.divider()

# Bottone di verifica
if st.button("Verifica Simulazione Greco", type="primary"):
    punti = 0
    for q in st.session_state.domande_greco:
        risposta = st.session_state.get(f"gr_{q['id']}")
        if risposta == q['corretta']:
            punti += 1
            st.success(f"{q['italiano']}: Corretto! ✅")
        else:
            st.error(f"{q['italiano']}: Errato. La forma corretta è {q['corretta']} ❌")
    
    st.metric("Punteggio Greco", f"{punti}/{len(st.session_state.domande_greco)}")
    if punti == len(st.session_state.domande_greco):
        st.balloons()
