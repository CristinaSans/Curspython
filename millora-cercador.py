import streamlit as st
import requests
import pandas as pd

st.title("Cercador d'usuaris")

# Camps de cerca
dni_val = st.text_input("Id")
nom_val = st.text_input("Nom")

# Botó de cerca
if st.button("Cerca"):
    url = "https://gorest.co.in/public/v2/users"
    response = requests.get(url)
    dades = response.json()

    # Filtrar coincidències
    resultats = []
    for dat in dades:
        if (dni_val and str(dat['id']) == dni_val) or (nom_val and nom_val.lower() in dat['name'].lower()):
            resultats.append({
                "Id": dat['id'],
                "Nom": dat['name'],
                "Email": dat['email'],
                "Gènere": dat['gender'],
                "Estat": dat['status']
            })

    if resultats:
        st.subheader("Resultats trobats:")
        df = pd.DataFrame(resultats)
        st.table(df)
    else:
        st.warning("No s'ha trobat cap coincidència")
