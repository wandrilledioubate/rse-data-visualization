import streamlit as st 

def display_conclusion():
    st.markdown("<h3 style='text-align: center;'>🗒️ Conclusion 🗒️</h3>", unsafe_allow_html=True)
    st.markdown("""
    Through our comprehensive analysis using the data visualization application *CrimeApp*, we have been able to explore various aspects of criminality in France. Criminal incidents, ranging from theft without violence to sexual violence, exhibit distinct trends that are crucial for understanding the underlying dynamics of French society.

    We identified that regions with high population density, especially major metropolitan areas like Paris, Lille, Marseille, and Nantes, are associated with higher crime rates. This observation underscores the correlation between population density and the volume of crime, indicating unique security challenges in urban environments. Moreover, the COVID-19 health crisis has had a visible impact, causing fluctuations in criminal trends, particularly a significant decrease in 2020.

    The alarming increase of 125% in sexual violence between 2016 and 2022 calls for special attention and resources to combat this type of crime. The distribution of incidents, as well as their correlation with factors such as demography and housing, suggests that crime prevention strategies need to be adapted and targeted based on local characteristics.

    Finally, the effective visualization of data, highlighting specific trends and anomalies, is an indispensable tool for decision-makers and authorities in developing crime prevention strategies. By understanding the dynamics of crime, we can form safer communities, promote social cohesion, and steer public policies towards a more informed and proactive response to the challenges of criminality in France.
    """)

