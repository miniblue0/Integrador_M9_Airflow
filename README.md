# Integrador_M9_Airflow

## Descripcion
Este pipeline cumple con las siguientes tareas:
1. **extract_data**: Genera una lista de numeros simulando una llamada a una API y la pasa a la siguiente tarea mediante XComs.
2. **transform_data**: Calcula el promedio de los numeros extraidos y guarda el resultado en XComs.
3. **print_data**: Recupera el promedio calculado y lo imprime en los logs.

## Requisitos
- Apache Airflow configurado.
- Acceso a la interfaz grafica de Airflow en `http://localhost:8080`.

## Como ejecutar
1. Copia el archivo `dag_integrador.py` en la carpeta `dags` de Airflow.
2. Activa el DAG desde la interfaz grafica.
3. Ejecutarlo y revisar los logs de las tareas.

## Notas
- No se generan ni se almacenan archivos; todo se maneja en memoria.
- Los datos pasan entre tareas usando XComs.
