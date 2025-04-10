DROP TABLE IF EXISTS raw_data.casos_covid;

CREATE TABLE raw_data.casos_covid (
    id SERIAL PRIMARY KEY,
    fecha_reporte DATE,
    id_departamento TEXT,
    departamento TEXT,
    id_municipio TEXT,
    municipio TEXT,
    edad INT,
    sexo TEXT,
    tipo TEXT,
    estado TEXT,
    pais_viajo TEXT,
    fecha_inicio_sintomas DATE,
    fecha_diagnostico DATE,
    fecha_recuperacion DATE,
    recuperado TEXT
);

-- Copia el CSV limpio (sin encabezado, con delimitador ',')
COPY raw_data.casos_covid(
    fecha_reporte,
    id_departamento,
    departamento,
    id_municipio,
    municipio,
    edad,
    sexo,
    tipo,
    estado,
    pais_viajo,
    fecha_inicio_sintomas,
    fecha_diagnostico,
    fecha_recuperacion,
    recuperado
)
FROM '/app/data/processed/casos_covid_limpios.csv'
DELIMITER ','
CSV HEADER;
