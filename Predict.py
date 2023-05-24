import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import joblib


class Predict:
    def __init__(self, da):
        self.da = da

    def predict_backlinks(self):
        # Load the model from file
        rf1 = joblib.load('ML/da-to-backlinks.joblib')
        # Make a prediction for a new data point
        new_data = pd.DataFrame({'DA': [self.da]})
        return round(rf1.predict(new_data)[0])
        # print(f'Predicted Backlinks: {backlinks_pred:.0f}')

    def predict_linking_domains(self):
        # Load the model from file
        rf2 = joblib.load('ML/da-to-linking-domains.joblib')
        # Make a prediction for a new data point
        new_data = pd.DataFrame({'DA': [self.da]})
        return round(rf2.predict(new_data)[0])
        # print(f'Predicted LinkingDomains: {linkingdomains_pred:.0f}')
