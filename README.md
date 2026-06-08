# 🚲 Projet de Machine Learning - Prédiction de la Demande de Vélos

Ce projet s'inscrit dans le cadre du **Module 5 : Machine Learning (ML)**. L'objectif principal est de prévoir le nombre de vélos loués par heure en fonction de facteurs tels que la date et les conditions météorologiques.

---

## Application en Ligne
L'application interactive a été déployée et est accessible publiquement ici :
🔗 **[https://ehtp-torbi-bikeshare.streamlit.app/](https://ehtp-torbi-bikeshare.streamlit.app/)**

---

## Description du Projet
Le projet suit une démarche rigoureuse d'ingénierie des données et de modélisation statistique divisée en plusieurs phases :
1. **Analyse Exploratoire des Données (EDA) :** Étude des distributions, identification de la cyclicité horaire bimodale et mise en évidence des corrélations météorologiques.
2. **Feature Engineering :** Création d'un transformateur personnalisé Scikit-Learn pour extraire les composantes temporelles et mise en place d'un `ColumnTransformer` (One-Hot Encoding + StandardScaler).
3. **Spot-Checking (10 modèles) :** Évaluation comparative de 10 algorithmes sur 3 métriques (RMSLE, MAE, R²).
4. **Tuning & Sélection :** Optimisation des hyperparamètres par `GridSearchCV` et validation finale du modèle **Hist Gradient Boosting** (R² de **90,50 %** sur le jeu de test, absence d'overfitting validée).
5. **Déploiement :** Création d'une interface utilisateur web avec Streamlit.

---

## Aperçu de l'Application (Captures d'écran)

Voici un aperçu visuel de l'interface utilisateur permettant d'effectuer les simulations en temps réel :

### Formulaire de saisie et paramètres
<img width="1193" height="1364" alt="image" src="https://github.com/user-attachments/assets/15ba9f10-595d-4e21-989e-199a15be19ca" />

### Résultat de la prédiction
<img width="1149" height="1613" alt="image" src="https://github.com/user-attachments/assets/ba1d5fd5-d614-479a-98f6-5e643e5961ae" />

---

## Installation et Lancement Local

Si vous souhaitez exécuter ce projet sur votre machine locale :

1. **Cloner le dépôt :**
   ```bash
   git clone https://github.com/ehtp-torbi/ehtp-projet-ml-bikeshare.git
   cd ehtp-projet-ml-bikeshare
