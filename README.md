# 📄 PICO Extractor & Search App

Cette application permet d'extraire automatiquement les éléments PICO (Participants, Intervention, Comparateur, Outcome) à partir d'articles médicaux en PDF, puis d'explorer les résultats dans une interface Streamlit interactive.

---

## ⚙️ Fonctionnalités

- 🧠 Extraction PICO avec le modèle BioELECTRA-PICO (`kamalkraj/BioELECTRA-PICO`)
- 🔍 Recherche multicritère (titre, année, P, I, C, O...)
- ✨ Surlignage automatique des mots-clés
- 📘 Vue détaillée d’un article sélectionné
- ⭳ Export CSV des résultats filtrés

---

## 📁 Structure

pico-projet/
├── fichier_pdf_test/ # Dossier contenant les fichiers PDF à analyser
├── fichier_pdf_test/
│   ├── [PDFs]                     # Les articles PDF à analyser
│   ├── tableau_PICO.xlsx         # Résultats d'extraction (générés automatiquement)
│   ├── rapport_PICO_BioELECTRA.docx # Rapport Word des résultats (généré automatiquement)
├── bioelectra_extraction.py # Script d'extraction PICO
├── pico_search_app.py # Interface Streamlit
├── requirements.txt # Dépendances du projet
└── README.md # Présentation du projet

---

## 🚀 Déploiement (Streamlit Cloud)

1. Crée un dépôt GitHub et envoie ce projet.
2. Va sur [https://streamlit.io/cloud](https://streamlit.io/cloud)
3. Connecte ton dépôt, et choisis :
   - **Main file**: `pico_search_app.py`
   - **Branch**: `main`
4. Clique sur **Deploy**

---

## ✅ Dépendances

Listées dans `requirements.txt` :

- `streamlit`
- `pandas`
- `openpyxl`
- `transformers`
- `torch`
- `PyMuPDF`
- `pytesseract`
- `pillow`
- `tqdm`

---

## 📝 Remarques

- Le modèle BioELECTRA-PICO fonctionne bien sur les abstracts ou sections cliniques.
- L’OCR est utilisé uniquement si aucun texte n’est détecté dans un PDF (nécessite Tesseract installé localement).
- Le moteur de recherche est accessible via l’interface Streamlit.

---

## 📬 Contact

Développé avec ❤️ pour l'analyse médicale intelligente.
Rabenco-Datasciences
chris@rabenco-datasciences.fr
