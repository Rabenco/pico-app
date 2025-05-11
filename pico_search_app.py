import streamlit as st
import pandas as pd
import re

# ░░ Chargement des données ░░
@st.cache_data
def load_data(path="fichier_pdf_test/tableau_PICO.xlsx"):
    df = pd.read_excel(path)
    return df.fillna("")

def highlight_keywords(text, keywords):
    if not keywords or not text:
        return text
    for kw in keywords:
        pattern = re.compile(re.escape(kw), re.IGNORECASE)
        text = pattern.sub(lambda m: f'<mark style="background-color: yellow">{m.group(0)}</mark>', text)
    return text

# ░░ Initialisation Streamlit ░░
st.set_page_config(page_title="Recherche PICO", layout="wide")
st.title("🔍 Moteur de recherche PICO")

df = load_data()

# ░░ Initialiser les champs de recherche (état local, pas session_state) ░░
with st.sidebar:
    st.header("Filtres")

    with st.form("filter_form"):
        fichier = st.selectbox("Nom du fichier", [""] + sorted(df["Fichier"].unique().tolist()))
        titre = st.selectbox("Titre de l'article", [""] + sorted(df["Titre"].unique().tolist()))
        annee = st.text_input("Année")
        p = st.text_input("Participants (P)")
        i = st.text_input("Intervention (I)")
        c = st.text_input("Comparateur (C)")
        o = st.text_input("Résultats (O)")
        submitted = st.form_submit_button("🔍 Appliquer les filtres")
        reset = st.form_submit_button("🧹 Effacer les filtres")

# ░░ Application des filtres ░░
search_terms = {}
if submitted:
    search_terms = {
        "Fichier": fichier,
        "Titre": titre,
        "Année": annee,
        "P": p,
        "I": i,
        "C": c,
        "O": o,
    }
elif reset:
    search_terms = {}

# ░░ Filtrage dynamique ░░
filtres_actifs = {k: v.lower() for k, v in search_terms.items() if v.strip()}

def row_matches(row):
    for col, kw in filtres_actifs.items():
        if kw not in str(row[col]).lower():
            return False
    return True

filtre_df = df[df.apply(row_matches, axis=1)] if filtres_actifs else df

# ░░ Surlignage HTML dans tableau ░░
def render_table(df, keywords_dict):
    def apply_highlight(row):
        return [highlight_keywords(str(row[col]), keywords_dict.get(col, "").split()) for col in df.columns]
    styled_data = df.apply(apply_highlight, axis=1, result_type="expand")
    styled_data.columns = df.columns
    return styled_data

# ░░ Affichage tableau ░░
st.subheader(f"🔎 {len(filtre_df)} article(s) trouvé(s)")
styled_df = render_table(filtre_df, filtres_actifs)

with st.expander("📋 Afficher les résultats (PICO inclus)", expanded=True):
    st.write(styled_df.to_html(escape=False), unsafe_allow_html=True)

# ░░ Vue détaillée ░░
st.markdown("---")
st.markdown("### 📘 Détails d’un article")
fichiers_dispo = [""] + filtre_df["Fichier"].tolist()
selected = st.selectbox("Sélectionner un fichier :", fichiers_dispo)

if selected:
    article = filtre_df[filtre_df["Fichier"] == selected].iloc[0]
    st.markdown(f"**📄 Fichier**: `{article['Fichier']}`")
    st.markdown(f"**Titre**: {article['Titre']}")
    st.markdown(f"**Année**: {article['Année']}")
    st.markdown("#### 🧩 Éléments PICO")
    for label in ["P", "I", "C", "O"]:
        content = highlight_keywords(article[label], filtres_actifs.get(label, "").split())
        st.markdown(f"**{label}:**", unsafe_allow_html=True)
        st.markdown(f"<div style='margin-bottom:10px'>{content}</div>", unsafe_allow_html=True)

# ░░ Export CSV ░░
st.download_button(
    "⭳ Télécharger les résultats filtrés (CSV)",
    filtre_df.to_csv(index=False).encode("utf-8"),
    "resultats_pico.csv",
    "text/csv"
)
