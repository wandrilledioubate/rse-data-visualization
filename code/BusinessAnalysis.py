import streamlit as st 
import pandas as pd

@st.cache_data(persist="disk")
def display_business_analysis():
    st.markdown("<h3 style='text-align: center;'>👔 Business Analysis 👔</h3>", unsafe_allow_html=True)
    st.markdown("<p>🔍 In order to better understand and analyze this dataset, I will first make a business analysis</p>", unsafe_allow_html=True)
    st.markdown("<p>🚔 As part of their judicial activity, security forces (police services and gendarmerie units) are required to draft procedures relating to offences, before transmitting them to the judicial authority which is likely to requalify them later. These offences could be found following a complaint filed by a victim, a report, a testimony, a flagrante delicto, a denunciation, etc., but also on the initiative of the security forces.</p>", unsafe_allow_html=True)
    st.markdown("<p>💾 In order to promote the opening of data on delinquency and insecurity, the SSMSI has made available, since March 2022, two annual databases on the main indicators of crimes recorded by the national police and gendarmerie, since 2016: one at the municipal level and the other at the departmental level, both according to the place of commission.</p>", unsafe_allow_html=True)
    st.markdown("<h5>🧐 The caracteristics of this dataset</h5>", unsafe_allow_html=True)
    display_tab_data()
    st.markdown("<h5>🎯 Goal of the project</h5>", unsafe_allow_html=True)
    st.markdown("<p>The main objective of this analysis will be to decipher trends, patterns, and anomalies in criminal incidents recorded across different regions and departments. By dissecting these data, we aim to identify high-risk areas, understand seasonal or annual fluctuations in crime rates, and assess the effectiveness of current crime prevention measures. This introspection is crucial to guide future policing and resource management strategies, enabling authorities to effectively target problem areas, Adapt policies and programs in response to the changing nature of crime, and implement proactive initiatives for safe communities. Moreover, by analyzing the correlation between demography, housing, and criminal incidents, we can inform broader discussions about urban development, social cohesion, and crime prevention in various social-economic contexts.</p>", unsafe_allow_html=True)
    st.write("")
    st.write("")
    st.markdown("<h5>❓ Problematic of the project</h5>", unsafe_allow_html=True)
    st.markdown("<h6 style='text-align: center;'>How do trends, patterns and anomalies in recorded criminal incidents across different regions and departments of France reveal the socio-economic and cultural implications, and how this information can-Are they being used to improve crime prevention and resource management strategies?</h6>", unsafe_allow_html=True)
    st.divider()



@st.cache_data(persist="disk")
def display_tab_data():
    data = {
        'caracteristique': [
            'classe', 
            'annee', 
            'Code.département', 
            'Code.région', 
            'unité.de.compte', 
            'millPOP', 
            'millLOG', 
            'faits', 
            'POP', 
            'LOG', 
            'tauxpourmille'
        ],
        'definition': [
            'Type of crime or incident', 
            'Year of registration', 
            'Code representing the department', 
            'Code corresponding to the region',  
            'Unit used for the count', 
            'Population in millions',  
            'Housing in millions',  
            'Number of recorded facts', 
            'Total population number',  
            'Total number of housing units',  
            'Rate of facts per thousand people'
        ]
    }

    df = pd.DataFrame(data)
    st.table(df)

