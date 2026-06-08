from sklearn.base import BaseEstimator, TransformerMixin
import pandas as pd

# Création du transformateur personnalisé pour les variables temporelles
class TemporalFeatureExtractor(BaseEstimator, TransformerMixin):
    def __init__(self):
        pass
    
    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        X_out = X.copy()
        X_out['datetime'] = pd.to_datetime(X_out['datetime'])
        
        # Extraction des composantes temporelles clés
        X_out['hour'] = X_out['datetime'].dt.hour
        X_out['month'] = X_out['datetime'].dt.month
        X_out['dayofweek'] = X_out['datetime'].dt.dayofweek
        X_out['year'] = X_out['datetime'].dt.year
        
        # Suppression de la colonne initiale devenue obsolète
        X_out = X_out.drop(columns=['datetime'], errors='ignore')
        return X_out