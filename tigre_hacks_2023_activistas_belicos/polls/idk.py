from joblib import load
import numpy as np


 
load_model = load('model.joblib')
X = np.array([[50,43,1593,25348,1396,-100.3180228,25.68445578]])
#X.reshape(1,-1)
#print(X.view())
 
predictions = [0,0,0,0,0,0,0,0,0,0]
for i in range(len(predictions)):
    predictions[i] = load_model.predict(X)
    print(predictions[i])