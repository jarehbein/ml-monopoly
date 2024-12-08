def explore_data_in_chunks(data_chunks):
    """Procesa los datos en chunks y muestra información básica de cada paquete."""
    for i, chunk in enumerate(data_chunks):
        print(f"Chunk {i+1}")
        print(chunk.head())
        break  # Procesar solo el primer chunk para exploración inicial
