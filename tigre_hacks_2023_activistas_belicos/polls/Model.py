import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
import sklearn as sk
from sklearn.neural_network import MLPRegressor
from sklearn.preprocessing import OneHotEncoder
import category_encoders as ce
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder
from joblib import dump

dataset = pd.read_csv('C:/Users/angel/Data/Data_Mty/Final_data_mty.csv')
df = pd.DataFrame(data = dataset)

#print(df.info())
df = df.dropna()


df1 = df.iloc[:,:2]
df2 = df.iloc[:,8:11]
df3 = df.iloc[:,11]
df_numerica = df.iloc[:,6:8]

df_numerica = pd.concat([df_numerica,df3], axis=1)
df_categorica = pd.concat([df1,df2], axis=1) 

#encoder = OneHotEncoder(sparse = False)
#data_encoded = encoder.fit_transform(df_categorica.values)

encoder = ce.CountEncoder(cols=['fecha','hora','vehiculo1_tipo','vehiculo1_marca','situacion_climatica']) 
#encoder2 = ce.TargetEncoder(df_numerica.values)
data_encoded = encoder.fit_transform(df_categorica)

data_encoded = pd.DataFrame(data_encoded, columns=encoder.get_feature_names_out())

DataFrame = pd.concat([data_encoded,df_numerica],axis=1)

DataFrame.to_csv('Merged_data_2.csv', index=False)

#print(df_numerica.info())
print(DataFrame.info())
#print(df1.info())
#print("data frame 2")
#print(df_categorica.info())

X = DataFrame.iloc[:,1:].values
y = DataFrame.iloc[:,7].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=42)

print(X_test)

'''regr = MLPRegressor(hidden_layer_sizes = (2,3), activation = 'relu', alpha = 0.0005, verbose = True, max_iter=1500)
regr.fit(X_train,y_train)

regr.score(X_train,y_train)

y_pred = regr.predict(X_test)

print(sk.metrics.mean_absolute_error(y_test, y_pred))
print(sk.metrics.mean_squared_error(y_test,y_pred))

a = plt.axes(aspect='equal')
plt.scatter(y_test[0:200], y_pred[0:200])
plt.xlabel('Accidentes Reales ')
plt.ylabel('Accidentes predichos')
lims = [0,200]
plt.xlim(lims)
plt.ylim(lims)
plt.plot(lims,lims)

dump(regr, 'model.joblib')'''