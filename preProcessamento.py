import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.ensemble import HistGradientBoostingClassifier
from imblearn.over_sampling import SMOTE
from sklearn.decomposition import PCA
from scipy.stats import zscore

# Definir o random state
RANDOM_STATE = 42
def removerOutliers(nomeColuna, df):
    coluna = df[nomeColuna]
    Q1 = coluna.quantile(0.25)
    Q3 = coluna.quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    
    # Filtra o DataFrame para manter apenas os valores dentro dos limites
    df_sem_outliers = df[(coluna >= lower_bound) & (coluna <= upper_bound)]
    df_sem_outliers = df[nomeColuna]>=lower_bound
    
    return df_sem_outliers


def remove_outliers_iqr(data, factor=2):
    Q1 = data.quantile(0.25)
    Q3 = data.quantile(0.75)
    IQR = Q3 - Q1
    is_not_outlier = ~((data < (Q1 - factor * IQR)) | (data > (Q3 + factor * IQR))).any(axis=1)
    return data[is_not_outlier]

# Carregar os dados
df = pd.read_csv('DadosBasicos.csv')

# Remover amostras onde não haja resposta numérica na classe "Q00301", diabetes
df = df[pd.to_numeric(df['Q00301'], errors='coerce').notnull()]
variaveisContinuas=['K04302','P00404','P00104','P02002', 'P02001']
for v in variaveisContinuas:
    removerOutliers(v, df)


variavel=df['k0432']