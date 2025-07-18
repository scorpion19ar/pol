# ia_modelo.py
from data_service import obtener_resultados_historicos
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import pickle

def entrenar_modelo():
    df = obtener_resultados_historicos()

    # Definir el resultado del partido
    df['resultado'] = df.apply(lambda row: 'local' if row['goles_local'] > row['goles_visitante']
                               else ('visitante' if row['goles_local'] < row['goles_visitante'] else 'empate'), axis=1)

    # Codificar equipos como números
    le = LabelEncoder()
    df['local_encoded'] = le.fit_transform(df['equipo_local'])
    df['visitante_encoded'] = le.fit_transform(df['equipo_visitante'])

    # Entrenamiento
    X = df[['local_encoded', 'visitante_encoded']]
    y = df['resultado']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    modelo = RandomForestClassifier()
    modelo.fit(X_train, y_train)

    # Guardar el modelo
    with open('modelo_entrenado.pkl', 'wb') as f:
        pickle.dump(modelo, f)

    print("Modelo entrenado y guardado.")

if __name__ == "__main__":
    entrenar_modelo()
