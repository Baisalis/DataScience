# ml_component/server/util.py
from joblib import load
import pandas as pd 
import os


curr_dir = os.path.dirname(os.path.realpath(__file__))
model_path = 'lib/SpotifyKDTree.joblib'
csv_path = 'lib/spotify_standardized.csv'
Spot_KDTree = load(os.path.join(curr_dir, model_path))
df_import = pd.read_csv(os.path.join(curr_dir, csv_path), index_col=0)

def nearest_by_id(id, k=11):
    result = Spot_KDTree.query(df_import.loc[[id]], k=k)[1]
    return df_import.iloc[result[0]].index.tolist()