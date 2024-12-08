import pandas as pd

def explore_data_in_chunks(data: pd.DataFrame, chunksize: int = 1000):
    """
    Procesa los datos en chunks y muestra información básica de cada paquete.
    
    Args:
        data: DataFrame con los datos.
        chunksize: Número de filas a procesar por chunk.
    """
    print(f"Cargando datos en chunks de tamaño {chunksize}.")
    
    # Divide el DataFrame en chunks
    for i, chunk in enumerate(range(0, len(data), chunksize)):
        data_chunk = data.iloc[chunk:chunk + chunksize]
        print(f"Chunk {i + 1} - Vista previa:")
        print(data_chunk.head())
        break  # Procesar solo el primer chunk para exploración inicial

