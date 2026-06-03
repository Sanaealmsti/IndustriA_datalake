import pandas as pd
import os

DATA_DIR = "data"

for fichier in os.listdir(DATA_DIR):
    if fichier.endswith(".csv"):
        df = pd.read_csv(os.path.join(DATA_DIR, fichier))
        print(f"\n{fichier}")
        print(df.shape)
        print(df.columns.tolist())
        print(df.head(3))