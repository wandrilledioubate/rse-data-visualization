import streamlit as st 

@st.cache_data(persist="disk")
def display_home():
    st.markdown("<h1 style='text-align: center;'>🔪 CrimeApp 🔪</h1>", unsafe_allow_html=True)
    st.markdown("<h5 style='text-align: center;'>The dataviz app to analyse the criminality in France</h5>", unsafe_allow_html=True)
    st.write("  ")
    st.markdown("<p>As part of semester 7, we had to realize a web application of data visualization of a dataset of the site data.gouv.fr</p>", unsafe_allow_html=True)
    st.markdown("<p>For my part, I chose to do it on the dataset called 'Municipal and departmental statistical bases of delinquency recorded by the police and the national gendarmerie' <a href=\"https://www.data.gouv.fr/fr/datasets/bases-statistiques-communale-et-departementale-de-la-delinquance-enregistree-par-la-police-et-la-gendarmerie-nationales/#/resources\" target=\"_blank\">🔗 link 🔗</a>.</p>", unsafe_allow_html=True)
    st.divider()