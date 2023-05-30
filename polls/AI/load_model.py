from joblib import load
import numpy as np
import datetime as datetime
import category_encoders as ce
import pandas as pd

def retornar_riesgo():
    dt = datetime.datetime.now()
    hora = dt.time().strftime("%I:%M:%S %p") 
    fecha = dt.date().strftime("%d/%m/%Y")


    df_tiempo = pd.DataFrame({'fecha':[fecha],'hora':[hora]})
    #print(horaStr)


    encoder = ce.CountEncoder(cols=['fecha', 'hora']) 
    #encoder2 = ce.TargetEncoder(df_numerica.values)
    data_encoded = encoder.fit_transform(df_tiempo)

    print(data_encoded['hora'])

    load_model = load('polls\AI\model.joblib')

    X_origen = np.array([[1,1,27705,25348,2269,-100.4070747,25.73963717]])
    X_destino = np.array([[1,1,1593,204,2269,-100.321654,25.6878179]])

    prediction_origen = load_model.predict(X_origen)
    prediction_destino = load_model.predict(X_destino)

    print(prediction_origen)
    print(prediction_destino)

    riesgo = (prediction_destino + prediction_origen)/2
    riesgo = (riesgo/31545) * 100
    print(riesgo)
    
    return riesgo