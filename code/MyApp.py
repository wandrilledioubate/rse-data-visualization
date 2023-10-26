import streamlit as st
import pandas as pd
import time
from functools import wraps
import logging
from Home import display_home
from Footer import display_footer
from BusinessAnalysis import display_business_analysis
from DataViz import display_dataviz
from Conclusion import display_conclusion

# Configure logging
logging.basicConfig(
    filename='app.log', 
    filemode='a',  
    format='%(asctime)s - %(message)s',
    level=logging.INFO 
)

def log_execution_time(func):
    """
    Décorateur pour enregistrer le temps d'exécution et l'horodatage d'une fonction.
    """
    @wraps(func)  # Cela préserve les métadonnées de la fonction originale
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Capture du temps de début
        result = func(*args, **kwargs)  # Appel de la fonction originale
        end_time = time.time()  # Capture du temps de fin

        execution_time = end_time - start_time  # Calcul du temps d'exécution
        logging.info(f"Temps d'exécution: {execution_time:.2f} secondes")  # Enregistrement du temps d'exécution

        return result  # Retour du résultat de la fonction originale

    return wrapper

@log_execution_time
def expensive_function():
    time.sleep(2)

def display_time():
    st.divider()
    st.markdown("<h3 style='text-align: center;'>⏱️ BONUS : Time ⏱️</h3>", unsafe_allow_html=True)
    if st.button("Execute app"):
        expensive_function()


def main():
    start_time = time.time()
    display_home()
    display_business_analysis()
    display_dataviz()
    display_conclusion()
    display_footer()
    end_time = time.time()

    # Calculate and display the elapsed time
    execution_time = end_time - start_time
    display_time()
    st.write(f"Temps de chargement de l'application : {execution_time:.2f} secondes")


if __name__ == "__main__":
    main()