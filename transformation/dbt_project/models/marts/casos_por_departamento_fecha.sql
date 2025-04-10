{{ config(materialized='table') }}

WITH base AS (
    SELECT
        departamento_nom AS departamento,
        fecha_de_notificaci_n::DATE AS fecha,
        COUNT(id_de_caso) AS total_casos,
        SUM(CASE WHEN estado ILIKE '%fallecido%' THEN 1 ELSE 0 END) AS total_fallecidos,
        SUM(CASE WHEN recuperado ILIKE '%recuperado%' THEN 1 ELSE 0 END) AS total_recuperados
    FROM {{ source('covid_data', 'casos_covid') }}
    GROUP BY 1, 2
)

SELECT * FROM base
