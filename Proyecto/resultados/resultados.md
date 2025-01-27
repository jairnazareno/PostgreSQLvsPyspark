Análisis narrativo
1.Carga inicial 

PostgreSQL demostró completar la operación en una velocidad de 11.828 ms, 
superando a Pyspark que se tomo cerca a los 20.44 ms.

Esto sugiere que PostgreSQL tiene un rendimiento mayor en la carga de datos cuando 
se trabaja con cantidades moderadas. Debido que se puede usar varios tipos de datos 
y las consultas las realiza de manera eficiente para consultas de igualdad y rango. 
PostgreSQL se define por estructuras balanceadas con consultas a alta velocidad.


2.Inserción de datos

En este caso, Pyspark fue más rápido, logrando así completar la tarea en un tiempo de 
25.9084 ms, frente al tiempo empleado de PostgreSQL que fue de 142 ms.

El rendimiento de Pyspark fue totalmente superior en la inserción de datos puede darse 
por su arquitectura distribuida y su capacidad de manejar tareas paralelas 
