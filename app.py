import streamlit as st
import pandas as pd
import numpy as np
import joblib
import sys
from datetime import datetime
from sklearn.base import BaseEstimator, TransformerMixin
from model import TemporalFeatureExtractor

# Configuration de la page
st.set_page_config(
    page_title="Prédiction - Demande de Vélos",
    page_icon="🚲",
    layout="centered"
)

# Chargement du modèle mis en cache (pour éviter de recharger le fichier à chaque clic)
@st.cache_resource
def load_bikeshare_model():
    return joblib.load("bike_sharing_model.joblib")

model = load_bikeshare_model()

# Interface Utilisateur
st.title("🚲 Prédiction de la Demande de Vélos")
st.write("Saisissez les conditions temporelles et météorologiques pour estimer le nombre de locations de vélos.")

st.markdown("---")

# Formulaire organisé en deux colonnes pour rester compact et propre
col1, col2 = st.columns(2)

with col1:
    st.subheader("📅 Paramètres Temporels")
    
    # Choix de la date et de l'heure
    pick_date = st.date_input("Sélectionner une date", datetime.now().date())
    pick_hour = st.slider("Heure de la journée", 0, 23, 12)
    
    # Reconstitution du format datetime attendu par notre Custom Transformer
    combined_datetime = f"{pick_date} {pick_hour:02d}:00:00"
    
    # Choix de la saison (Format natif du dataset : 1 à 4)
    season_labels = {1: "Printemps (1)", 2: "Été (2)", 3: "Automne (3)", 4: "Hiver (4)"}
    season = st.selectbox("Saison", options=list(season_labels.keys()), format_func=lambda x: season_labels[x])
    
    # Jours spéciaux
    holiday = st.checkbox("Jour férié (Holiday)", value=False)
    workingday = st.checkbox("Jour de travail (Working Day)", value=True)

with col2:
    st.subheader("☀️ Conditions Météo")
    
    # Choix de la météo (Format natif du dataset : 1 à 4)
    weather_labels = {
        1: "Dégagé / Peu nuageux (1)",
        2: "Brouillard / Nuageux (2)",
        3: "Légère pluie / Légère neige (3)",
        4: "Forte pluie / Orage / Grêle (4)"
    }
    weather = st.selectbox("Météo", options=list(weather_labels.keys()), format_func=lambda x: weather_labels[x])
    
    # Variables numériques environnementales
    temp = st.slider("Température réelle (°C)", -10.0, 45.0, 20.0, step=0.5)
    atemp = st.slider("Température ressentie (°C)", -10.0, 50.0, 22.0, step=0.5)
    humidity = st.slider("Taux d'humidité (%)", 0, 100, 60)
    windspeed = st.slider("Vitesse du vent (km/h)", 0.0, 60.0, 12.0, step=0.5)

st.markdown("---")

# 4. Logique de Prédiction
if st.button("🚀 Calculer la demande prévisionnelle", type="primary"):
    if model is not None:
        # Création du dictionnaire avec les colonnes exactes de X_train_raw
        input_data = {
            "datetime": [combined_datetime],
            "season": [int(season)],
            "holiday": [1 if holiday else 0],
            "workingday": [1 if workingday else 0],
            "weather": [int(weather)],
            "temp": [float(temp)],
            "atemp": [float(atemp)],
            "humidity": [float(humidity)],
            "windspeed": [float(windspeed)]
        }
        
        # Conversion immédiate en DataFrame
        df_input = pd.DataFrame(input_data)
        
        # Calcul de la prédiction (sur l'échelle log)
        log_prediction = model.predict(df_input)[0]
        
        # Transformation inverse pour repasser sur la vraie échelle (Nombre de vélos)
        final_prediction = np.expm1(log_prediction)
        
        # Sécurité pour éviter d'afficher des valeurs négatives absurdes dues aux arrondis
        final_prediction = max(0, int(round(final_prediction)))
        
        # Affichage du résultat de manière élégante
        st.success("### Résultat de la simulation")
        st.metric(
            label="Nombre total de vélos à mettre à disposition :", 
            value=f"{final_prediction} vélos"
        )
    else:
        st.error("Impossible d'effectuer la prédiction car le modèle n'est pas chargé.")
