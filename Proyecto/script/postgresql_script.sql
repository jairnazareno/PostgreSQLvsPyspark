1.- CARGA INICIAL

 EXPLAIN ANALYZE
 SELECT * FROM yahoo_symbols LIMIT 100000;

-------------------------------------------------------

2.-INSERCIÓN DE DATOS

BEGIN;

DO $$
DECLARE
    i INT;
    start_time TIMESTAMP;
    end_time TIMESTAMP;
    elapsed_time INTERVAL;
BEGIN
    -- Registra el tiempo de inicio
    start_time := clock_timestamp();

    FOR i IN 1..10000 LOOP
        INSERT INTO yahoo_symbols (ticker, name, exchange, category_name, country)
        VALUES (concat('SYM', i), concat('Name', i), 'EX', 'Category', 'USA');
    END LOOP;

    -- Registra el tiempo de fin
    end_time := clock_timestamp();
    elapsed_time := end_time - start_time;

    -- Imprime el tiempo transcurrido
    RAISE NOTICE 'Tiempo de ejecución: %', elapsed_time;
END $$;

COMMIT;
