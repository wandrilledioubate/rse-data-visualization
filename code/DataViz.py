import streamlit as st
import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt
import geopandas as gpd


@st.cache_data(persist="disk")
def load_data():
    data=pd.read_csv("./donnee-dep-data.gouv-2022-geographie2023-produit-le2023-07-17.csv", sep=";")
    data['annee'] = data['annee'].astype(str)
    data['Code.département'] = data['Code.département'].astype(str)
    return data

def display_dataviz():
    st.markdown("<h3 style='text-align: center;'>📈 Data Visualization 📈</h3>", unsafe_allow_html=True)
    st.write(" ")
    number_incident()
    pie_chart_1()
    heatmap_incident() 
    line_chart()
    bar_plot()
    histogram_violence_sexuelles()
    correlation_1()
    pie_chart_2()
    heatmap_correlation()
    st.divider()



@st.cache_data(persist="disk")
def number_incident():
    data=load_data()
    incident_sums = data['faits'].sum()
    nb_incident_per_citizen = round((incident_sums/7)/67000000, 2)
    st.markdown("<h5>0️⃣ Number of incidents per French citizen 🇫🇷</h5>", unsafe_allow_html=True)
    st.write("The number of incidents per French citizen is:")
    st.write(nb_incident_per_citizen)
    st.write("We can therefore conclude that one French in 25 is a victim or involved in an incident each year. This helps to better understand the place of criminality in France.")
    st.write(" ")

@st.cache_data(persist="disk")
def pie_chart_1():
    st.markdown("<h5>1️⃣ Breakdown of incident types 🧀</h5>", unsafe_allow_html=True)
    st.write("To begin, I will visualize the breakdown of incident types. On the one hand, it will allow me to know the different incidents but also to know their distribution.")
    data=load_data()

    incident_sums = data.groupby('classe')['faits'].sum()
    incident_table = incident_sums.reset_index()
    incident_table.columns = ['Class', 'Number of Incidents']
    
    # create pie chart
    fig = plt.figure(figsize=(10, 6))
    incident_sums.plot.pie(autopct='%1.1f%%', startangle=90)
    plt.title('Breakdown of incident types')
    plt.ylabel('') 
    plt.show()
    st.pyplot(fig)

    st.write("It can therefore be observed that theft without violence and destruction and degradation are clearly the majority with more than 20 percent each.")
    st.write(" ")


@st.cache_data(persist="disk")
def heatmap_incident():
    st.markdown("<h5>2️⃣ Heatmap of the number of incidents in France by department 🌍</h5>", unsafe_allow_html=True)
    st.write("Now we will try to see if there are departments in which there is more crime one than in others by making a heatmap.")
    
    # Load data
    data=load_data()

    sum_faits = data.groupby("Code.département")["faits"].sum().reset_index()

    # Chargement du fond de carte
    url = "https://github.com/gregoiredavid/france-geojson/raw/master/departements-version-simplifiee.geojson"
    map_data = gpd.read_file(url)

    # Fusion des données avec le fond de carte
    merged = map_data.set_index('code').join(sum_faits.set_index('Code.département'))

    # Création de la heatmap
    fig, ax = plt.subplots(1, 1, figsize=(6, 6))
    merged.plot(column='faits', cmap='coolwarm', linewidth=0.8, ax=ax, edgecolor='0.8', legend=True)
    ax.set_title("Heatmap of Incidents in France")
    st.pyplot(fig)

    # Fusion des données avec le fond de carte
    merged = map_data.set_index('code').join(sum_faits.set_index('Code.département'))

    # Création de la heatmap
    fig2, ax = plt.subplots(1, 1, figsize=(10, 10))
    merged.plot(column='faits', cmap='coolwarm', linewidth=0.8, ax=ax, edgecolor='0.8', legend=True)


    # Définir les limites pour un zoom sur l'Île-de-France
    idf_bounds = merged[merged["nom"].isin(["Paris", "Seine-et-Marne", "Yvelines", "Essonne", "Hauts-de-Seine", "Seine-Saint-Denis", "Val-de-Marne", "Val-d'Oise"])].total_bounds
    ax.set_xlim(idf_bounds[0], idf_bounds[2])
    ax.set_ylim(idf_bounds[1], idf_bounds[3])
    ax.set_title("Heatmap of Incidents in Île-de-France")
    st.pyplot(fig2) 

    """
    # display table
    department_names = map_data[['code', 'nom']].rename(columns={'code': 'Code.département', 'nom': 'Department Name'})
    incidents_per_department = data.groupby("Code.département")["faits"].sum().reset_index()
    incidents_per_department = incidents_per_department.merge(department_names, on='Code.département', how='left')
    incidents_per_department = incidents_per_department[['Department Name', 'faits']]
    incidents_per_department.columns = ['Department Name', 'Number of Incidents']
    if st.checkbox("Display the table") : 
        st.table(incidents_per_department)
    """

    st.write("So I made a heatmat by highlighting the Ile-de-France region after. We realize directly that crime is increased in the departments of large cities (Paris, Lille, Marseille, Nantes...)")
    st.write("We could therefore make an assumption between population size and crime. The more densely populated a city is, the more crime there will be.")
    st.write("This phenomenon is also explained by the fact that cities are surrounded by suburbs, less affluent where crime is more present.")
    st.write(" ")



def line_chart():
    # Write title and explanation
    st.markdown("<h5>3️⃣ Linechart of the number of incidents in France by year 🔢</h5>", unsafe_allow_html=True)
    st.write("I will now create a line chart of the number of facts according to the year. On the other hand, I chose to use a select box to choose the type of crime.")
    
    # Load data
    data=load_data()

    # Data transformation
    classes_de_crime = data['classe'].unique()
    selected_class = st.selectbox('Select a type of crime', classes_de_crime)
    filtered_data = data[data['classe'] == selected_class]
    total_crimes_par_annee = filtered_data.groupby('annee')['faits'].sum().reset_index()

    # Create line chart
    st.line_chart(total_crimes_par_annee.set_index('annee'))

    # Display dataframe of the concerned data
    if st.checkbox('Display the data'):
        st.write(total_crimes_par_annee)

    st.write("We can notice most crimes are up between 2016 and 2022. On the other hand, we can see that the increase is less significant in 2020. We can explain this by the COVID-19 health crisis.")
    st.write(" ")



def bar_plot():
    # Write title and explanation
    st.markdown("<h5>4️⃣ Percentage of crime between 2016 and 2022 📈</h5>", unsafe_allow_html=True)
    st.write("To better understand the dataset, I decided to create a barplot to visualize the crimes that increased between 2016 and 2022.")
    
    # Load data
    data=load_data()
    data_2016 = data[data['annee'] == '16']
    data_2022 = data[data['annee'] == '22']

    # Merge by class of crime and compute the total for each year
    total_crimes_2016 = data_2016.groupby('classe')['faits'].sum().reset_index()
    total_crimes_2022 = data_2022.groupby('classe')['faits'].sum().reset_index()

    # Merge data for 2016 and 2022
    croissance_crimes = pd.merge(total_crimes_2016, total_crimes_2022, on='classe', suffixes=('_2016', '_2022'))

    # Compute the increase of fact between 2016 and 2022
    croissance_crimes['croissance'] = croissance_crimes['faits_2022'] - croissance_crimes['faits_2016']

    # Rename columns
    croissance_crimes = croissance_crimes.rename(columns={'faits_2016': 'Faits en 2016', 'faits_2022': 'Faits en 2022', 'croissance': 'Croissance'})

    # Compute increase in percentage
    croissance_crimes['Croissance (%)'] = ((croissance_crimes['Faits en 2022'] - croissance_crimes['Faits en 2016']) / croissance_crimes['Faits en 2016']) * 100
    
    # Create bar plot
    fig, ax = plt.subplots(figsize=(10, 6))
    colors = ['red' if x > 0 else 'green' for x in croissance_crimes['Croissance (%)']]


    bars = ax.bar(croissance_crimes['classe'], croissance_crimes['Croissance (%)'], color=colors)

    for bar in bars:
        height = bar.get_height()
        ax.annotate(f'{height:.2f}%',  
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3), 
                    textcoords="offset points",
                    ha='center', va='bottom')

    plt.title('Croissance des crimes entre 2016 et 2022')
    plt.xlabel('Classe de Crime')
    plt.ylabel('Croissance des Faits')

    plt.xticks(rotation=90)  

    st.pyplot(fig)

    afficher_dataframe = st.checkbox('Display the dataframe')

    if afficher_dataframe:
        st.write(croissance_crimes)

    st.write("As can be seen, sexual violence was the crime that increased the most in 6 years with an increase of 125%.")
    st.write(" ")


@st.cache_data(persist="disk")
def histogram_violence_sexuelles():
    st.markdown("<h5>5️⃣ Barplot of the number of violences sexuelles in France by department 🦃</h5>", unsafe_allow_html=True)
    st.write("To better understand the increase in sexual violence, I decided to study the number of sexual violence according to the department.")

    # Load data
    data=load_data()

    violences_sexuelles = data[data['classe'] == 'Violences sexuelles']

    violences_par_departement = violences_sexuelles.groupby('Code.département')['faits'].sum().reset_index()

    violences_par_departement = violences_par_departement.sort_values(by='faits', ascending=False)

    top15_departements = violences_par_departement.head(15)

    fig, ax = plt.subplots(figsize=(10, 6))

    bars = ax.bar(top15_departements['Code.département'], top15_departements['faits'], color='skyblue')

    for bar in bars:
        height = bar.get_height()
        ax.annotate(f'{height}',
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points de décalage vers le haut
                    textcoords="offset points",
                    ha='center', va='bottom')

    plt.title('Nombre de Violences Sexuelles par Département')
    plt.xlabel('Code Département')
    plt.ylabel('Nombre de Violences Sexuelles')

    plt.xticks(rotation=45)  

    st.pyplot(fig)
    st.write(" ")
    st.write(" ")
    st.write(" ")


@st.cache_data(persist="disk")
def correlation_1():
    st.markdown("<h5>6️⃣ Scatter Plot of the facts vs. the population 🇲🇦</h5>", unsafe_allow_html=True)

    # Load data
    data=load_data()

    fig, ax = plt.subplots()
    sns.regplot(x=data['POP'], y=data['faits'], data=data, scatter_kws={"color": "blue"}, line_kws={"color": "red"})

    plt.xlabel('Population')
    plt.ylabel('Nombre de faits')
    plt.title('Corrélation entre la population et le nombre de faits')

    st.pyplot(fig)

    st.write("The red regression line in the graph above illustrates the overall trend of the data. If the line goes up, it indicates a positive correlation, meaning that the population increase is usually associated with an increase in the number of facts. A descending line would indicate the opposite. The slope of the line also provides a visual indication of the strength of the correlation. The steeper the slope (whether ascending or descending), the stronger the correlation.")


def pie_chart_2():
    st.markdown("<h5>7️⃣ Pie chart of the distribution of crimes by department 🦕</h5>", unsafe_allow_html=True)
    data=load_data()

    selected_department = st.selectbox('Choisir un département:', data['Code.département'].unique())
    data = data[data['Code.département'] == selected_department]

    grouped_by_classe_mean = data.groupby('classe')['faits'].mean().reset_index()
    grouped_by_classe_mean = grouped_by_classe_mean.sort_values('faits', ascending=False)

    plt.figure(figsize=(12, 12))
    plt.pie(grouped_by_classe_mean['faits'], labels=grouped_by_classe_mean['classe'], autopct='%1.1f%%', startangle=140)
    plt.axis('equal')
    plt.title('Average distribution of crime types over all years')
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.pyplot()

def heatmap_correlation():
    st.markdown("<h5>8️⃣ Heatmap correlation with population, facts and logements 💂</h5>", unsafe_allow_html=True)

    # Load data
    data=load_data()
    
    dept_options = data['Code.département'].unique()  
    selected_dept = st.selectbox('Choisissez un département:', dept_options)

    dept_data = data[data['Code.département'] == selected_dept]

    if st.checkbox('Display the data of the department'):
        st.write(dept_data)

    corr_matrix = dept_data[['POP', 'millLOG', 'faits']].corr()

    st.subheader('Heatmap de corrélation')
    fig, ax = plt.subplots()
    sns.heatmap(corr_matrix, annot=True, fmt=".2f", cmap='coolwarm', ax=ax)
    st.pyplot(fig)

    st.write("This heatmap shows the correlation between population, housing, and the number of facts for the selected department.")
    st.write("A correlation value close to 1 indicates a strong positive correlation, while a value close to -1 indicates a strong negative correlation.")
    st.write("A value close to 0 suggests that there is no direct correlation. The values are calculated based on the department-specific data you selected.")
