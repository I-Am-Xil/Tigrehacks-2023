import pandas as pd

dataset = pd.read_csv('C:/Users/angel/Data/Data_Mty/Incidentes-TestFix.csv')
df = pd.DataFrame(data = dataset)

df.dropna()

df1 = df.iloc[:,:2]

df['fecha'] = pd.to_datetime(df['fecha'])

df['conteo_accidentes_dia'] = df.groupby('fecha')['fecha'].transform('count')

df.to_csv('C:/Users/angel/Data/Data_Mty/Final_data_mty.csv', index=False)