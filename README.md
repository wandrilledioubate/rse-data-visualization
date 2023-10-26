**Deadline : Last Session, October 27th**
 
You must present your work during the last session and answer some conceptual and technical  questions.
 
Based on the precedent labs you have done. Build an interactive web application using the streamlit library and the one or two data viz librairies (matplotlib, seaborn, altair, bokeh and plotly).
 
The **main idea** of the project is to choose a dataset from data.gouv.fr and build a dataviz web app to answer some useful questions about it, giving your users useful insights and the possibility to interact with the data.
 
The dataset you choose can have a relation with the RSE theme, it is not mandatory but highly recomanded. This is the link to read about the RSE : https://www.economie.gouv.fr/entreprises/responsabilite-societale-entreprises-rse
 
Technical guidelines :
The streamlit application must respect the following **technical** requirements (you organize them in the way you want, because the most important thing is to bring insights to your users) :
- All the code must be organized in functions, if you can write comments, it is always better. Think modulable code, blocks of data processing, workflow steps. This will help you organize your code in modular functions
- 4 internal streamlit plots : st.line, st.bar_chart, st.scatter_chart, st.map
- 4 different external plots (histograms, Bar, Scatter or Pie charts) integrated with your application from external librairies like matplotlib, seaborn, plotly or Altair
- 4 interactive elements (checkbox, slider ....)
- Cache usage : cache for data loading and pre-processing
- Optional : A decorator that logs in a file the time execution interval in seconds (30 seconds, 2 seconds, 0.01 seconds, ...) and the timestamp of the call ()
- Optional : try to organize your functions calls into a main function in order to have a clear workflow of your application
 
Please keep in mind that the idea is to provied useful insights and draw a story about your data. So you **must** first take a moment to explore, conceive and organise your dashboard by **choosing** the questions you want to answer and the **insights** you want to present.