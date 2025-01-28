# Análisis Comparativo de Rendimiento entre PostgreSQL y PySpark

## Descripción
Este proyecto evalúa el rendimiento de PostgreSQL y PySpark en la carga inicial de datos y la inserción masiva de filas, utilizando un dataset real de símbolos de Yahoo Finance.

GRUPO 2 - NAZARENO SOLIS JAIR - KATHERINE MUÑOZ - LUIS SANCHEZ


DOCUMENTACIÓN

1. Configuración Inicial
Instalación de PostgreSQL y PySpark:

PostgreSQL fue instalado y configurado como el motor de base de datos (usando PgAdmin4 v8)
Se configuró el entorno de PySpark v2.4.5 , asegurando dependencias como Docker y Spark.
Preparación del Dataset:

Se utilizó el archivo yahoo-symbols-201709.csv, un dataset con más de 100,000 registros de datos financieros.
Se verificó que los datos estuvieran correctamente formateados para evitar errores durante la carga (se usó Excel para ajustes).

2. Procesos en PostgreSQL
Creación de la Tabla:

En PostgreSQL, se definió la tabla con los tipos de datos correspondientes.
Ejemplo del comando SQL:
CREATE TABLE yahoo_symbols (
  ticker VARCHAR(100),
  name VARCHAR(100),
  exchange VARCHAR(100),
  category_name VARCHAR(100),
  country VARCHAR(100)
);

2.1 Importación de datos - Postgresql
Descargar los datos limpios y cargarlo como archivo csv, con delimitante de punto y coma (;) 


3. Proceso en Pyspark
   El archivo CSV fue cargado en PySpark:
   
df = spark.read.csv("ruta/del/archivo/yahoo-symbols-201709.csv", header=True, inferSchema=True)

   
