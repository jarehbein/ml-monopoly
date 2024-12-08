"""
This is a boilerplate pipeline 'data_preparation'
generated using Kedro 0.19.9
"""
import pandas as pd
from sklearn.preprocessing import StandardScaler

def clean_and_rename_data(data: pd.DataFrame) -> pd.DataFrame:
    """
    Renombra las columnas y limpia los datos eliminando duplicados, 
    manejando valores nulos y transformando a un formato adecuado.
    """
    # Renombrar columnas utilizando la primera fila del dataset como encabezado
    data.columns = data.iloc[0].astype(str)  # Asegúrate de que los nombres sean strings
    data = data[1:]  # Elimina la fila que ahora es el encabezado
    data.reset_index(drop=True, inplace=True)  # Resetea el índice
    data.columns = [col.strip() for col in data.columns]  # Limpia nombres de columnas
    print("Nuevos nombres de columnas:", data.columns)

    # Limpieza de datos
    print("Columnas disponibles antes de la limpieza:", data.columns)
    print("Tipo de datos recibidos:", type(data))
    print("Datos iniciales:", data.head())

    # Eliminar duplicados
    data = data.drop_duplicates()

    # Reemplazar valores no numéricos con NaN
    for col in data.select_dtypes(include=["object", "string"]).columns:
        data[col] = pd.to_numeric(data[col], errors="coerce")

    # Rellenar valores faltantes con 0
    data = data.fillna(0)
    print("Datos limpios:", data.head())
    print("Columnas disponibles después de la limpieza:", data.columns)

    return data

def create_target(data: pd.DataFrame) -> pd.DataFrame:
    """
    Crea la columna 'target' indicando clientes activos (1) o inactivos (0).
    Regla: Activo si renta > 100,000, inactivo en caso contrario.
    """
    # Verifica que la columna 'Renta' existe
    if 'Renta' not in data.columns:
        raise KeyError("La columna 'Renta' no se encuentra en el dataset.")
    
    # Crear columna target
    data['target'] = (data['Renta'] > 100000).astype(int)
    
    # Validar distribución del target
    print(f"Distribución del target:\n{data['target'].value_counts()}")
    return data


def transform_data(data: pd.DataFrame) -> pd.DataFrame:
    """Aplica transformaciones a los datos."""
    print("Columnas disponibles antes de transformación:", data.columns)
    # Renombrar columnas si es necesario
    if "1.5" in data.columns:
        data.rename(columns={"1.5": "Renta"}, inplace=True)

    if "Renta" in data.columns:
        # Identificar valores no numéricos
        non_numeric = data["Renta"].apply(lambda x: not isinstance(x, (int, float)))
        print("Valores no numéricos en 'Renta':", data[non_numeric]["Renta"].unique())

        # Convertir a numérico, reemplazando no numéricos con 0 o NaN
        data["Renta"] = pd.to_numeric(data["Renta"], errors="coerce")

        # Escalar la columna después de manejar valores no numéricos
        data["Renta"] = (data["Renta"] - data["Renta"].mean()) / data["Renta"].std()

    # Codificación de variables categóricas
    if "Sexo" in data.columns:
        data = pd.get_dummies(data, columns=["Sexo"], drop_first=True)
    print("Columnas disponibles después de transformación:", data.columns)
    return data


def select_features(data: pd.DataFrame) -> pd.DataFrame:
    """Selecciona las columnas relevantes para el modelo."""
    selected_columns = ["Renta", "Edad", "Antiguedad", "target"] 
    print("Seleccionando columnas:", selected_columns)
    data = data[selected_columns]
    print("Datos finales seleccionados:", data.head())
    return data

