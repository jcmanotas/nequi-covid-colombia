# NEQUI Proyecto ETL COVID-19 Colombia
Este proyecto tiene como propósito aplicar buenas prácticas de **Ingeniería de Datos** para construir un pipeline ETL completo usando herramientas modernas como **Airbyte**, **Dagster** y **dbt**. Se utiliza **Python** como lenguaje de programacion principal.

---

Este proyecto utiliza las siguientes herramientas y librerías:

- 🐍 **Python**  
- 🐘 **PostgreSQL**
- 📦 **pandas**, **numpy**
- 📊 **seaborn**, **matplotlib**
- 📈 **sweetviz**, **scipy**
- 📁 **dbt (data build tool)**
- 📓 **Jupyter Notebook**  
- 🐳 **Docker** y `docker-compose.yml`
---


## 🧠 Objetivo

- Desarrollar un pipeline de ingesta, transformación y carga de datos.
- Aplicar arquitectura modular, manejo de errores y logs.
- Documentar cada paso con claridad para su fácil comprensión.

---

## 📦 Estructura del Proyecto

```bash
etl-covid-colombia/
├── docker-compose.yml        # PostgreSQL en Docker
├── README.md
├── .gitignore
├── requirements.txt
│
├── docs/                     # Documentación (diagramas, imágenes, referencias)
│   └── diagramas/
│
├── data/                     # Dataset crudo y transformado
│   ├── raw/
│   └── processed/
│
├── notebooks/                # Exploración inicial, EDA
│   └── eda.ipynb
│
├── ingestion/                # Airbyte u otros extractores
│   └── airbyte_config/
│
├── orchestration/           # Dagster pipeline
│   ├── etl_pipeline/
│   └── logs/
│
├── transformation/          # dbt modelos
│   └── dbt_project/
│
├── utils/                   # Manejo de errores, logs, helpers
│   ├── exceptions.py
│   └── logger.py
│
└── tests/                   # Pytest, pruebas de unidad
```

---
# Casos positivos de COVID-19 en Colombia

Este conjunto de datos, publicado por el Instituto Nacional de Salud (INS), proporciona información detallada sobre los casos positivos de COVID-19 en Colombia.

## Descripción

**Información importante:**

- Actualmente, en relación con la transmisión del SARS-CoV-2, el país se encuentra en una zona de seguridad según los umbrales establecidos para este análisis. Sin embargo, este estado ha sido reciente, por lo que aún es prematuro determinar si Colombia ha entrado en una fase endémica.

- Se recomienda a las Entidades Administradoras de Planes de Beneficios (EAPB), Instituciones Prestadoras de Salud (IPS) y a la población en general continuar realizando pruebas diagnósticas a todas las personas con síntomas respiratorios y a sus contactos, siguiendo las directrices del Ministerio de Salud y Protección Social. La detección temprana de casos es fundamental para identificar cambios en la positividad.

**ATENCIÓN:**

- Consulte el nuevo catálogo de variables que entrará en funcionamiento a partir del 29 de octubre: [http://url.ins.gov.co/dataset-covid-info](http://url.ins.gov.co/dataset-covid-info)

## Publicado por

- **Instituto Nacional de Salud (INS)**

# Casos Positivos de COVID-19 en Colombia

Este conjunto de datos contiene información detallada sobre los casos positivos de COVID-19 reportados en Colombia. Es publicado por el Instituto Nacional de Salud (INS) y tiene como objetivo ofrecer datos abiertos y accesibles para el análisis y monitoreo de la pandemia.

## ¿Qué hay en este conjunto de datos?

- **Filas**: 6,390,000+
- **Columnas**: 23

A continuación se describe cada columna del conjunto de datos:

| Nombre de la Columna             | Descripción                                                                                                                                                                                                                         | Nombre del Campo API         | Tipo de Dato |
|----------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------|--------------|
| Fecha de reporte web             | Fecha de publicación en el sitio web                                                                                                                                                                                               | `fecha_reporte_web`          | Texto        |
| ID de caso                       | Identificador único del caso                                                                                                                                                                                                       | `id_de_caso`                 | Número       |
| Fecha de notificación            | Fecha de notificación a SIVIGILA                                                                                                                                                                                                   | `fecha_de_notificaci_n`      | Texto        |
| Código DIVIPOLA departamento     | Código numérico del departamento según DIVIPOLA                                                                                                                                                                                     | `departamento`               | Número       |
| Nombre departamento              | Por seguridad, algunos datos pueden ser limitados para evitar identificación en municipios específicos                                                                                                                             | `departamento_nom`           | Texto        |
| Código DIVIPOLA municipio        | Código numérico del municipio según DIVIPOLA                                                                                                                                                                                        | `ciudad_municipio`           | Número       |
| Nombre municipio                 | Por seguridad, algunos datos pueden ser limitados para evitar identificación en municipios específicos                                                                                                                             | `ciudad_municipio_nom`       | Texto        |
| Edad                             | Edad del paciente                                                                                                                                                                                                                   | `edad`                       | Número       |
| Unidad de medida de edad         | 1 - Años, 2 - Meses, 3 - Días                                                                                                                                                                                                       | `unidad_medida`              | Número       |
| Sexo                             | Género del paciente                                                                                                                                                                                                                 | `sexo`                       | Texto        |
| Tipo de contagio                 | Tipo de transmisión: Relacionado, Importado, En estudio, Comunitario                                                                                                                                                               | `fuente_tipo_contagio`       | Texto        |
| Ubicación del caso               | Estado actual del paciente (ej. Hospital, Casa, Fallecido, etc.). Puede incluir casos no relacionados con COVID-19 o con comorbilidades                                                     | `ubicacion`                  | Texto        |
| Estado                           | Estado clínico del caso (ej. Leve, Moderado, Grave, Fallecido, etc.)                                                                                                                                                               | `estado`                     | Texto        |
| Código ISO del país              | Código ISO del país de viaje si aplica                                                                                                                                                                                              | `pais_viajo_1_cod`           | Número       |
| Nombre del país                  | Nombre del país de viaje si aplica                                                                                                                                                                                                  | `pais_viajo_1_nom`           | Texto        |
| Recuperado                       | Estado de recuperación (Recuperado, Fallecido, N/A). Casos N/A incluyen fallecidos no COVID o recuperados hospitalizados por otras causas                                                  | `recuperado`                 | Texto        |
| Fecha de inicio de síntomas      | Fecha en la que iniciaron los síntomas                                                                                                                                                                                              | `fecha_inicio_sintomas`      | Texto        |
| Fecha de muerte                  | Fecha de fallecimiento del paciente                                                                                                                                                                                                 | `fecha_muerte`               | Texto        |
| Fecha de diagnóstico             | Fecha de confirmación del caso por laboratorio                                                                                                                                                                                      | `fecha_diagnostico`          | Texto        |
| Fecha de recuperación            | Fecha en la que se declaró recuperado                                                                                                                                                                                               | `fecha_recuperado`           | Texto        |
| Tipo de recuperación             | Puede ser por PCR o por Tiempo. PCR indica recuperación confirmada por segunda muestra negativa. Tiempo refiere a 30 días sin síntomas (según criterios específicos)                         | `tipo_recuperacion`          | Texto        |
| Pertenencia étnica               | Codificación étnica: 1-Indígena, 2-ROM, 3-Raizal, 4-Palenquero, 5-Negro, 6-Otro. Sujeta a reporte, autorreconocimiento y censo local                                                        | `per_etn_`                   | Número       |
| Nombre del grupo étnico          | Nombre del grupo étnico al que pertenece la persona                                                                                                                                                                                 | `nom_grupo_`                 | Texto        |

## Advertencias de responsabilidad

- Algunas variables como **etnia** y **ubicación del caso** dependen del correcto diligenciamiento por parte del personal de salud, el autorreconocimiento y los censos regionales. El Instituto Nacional de Salud no es responsable de la calidad de estas variables.
- Para proteger la identidad de los pacientes, cierta información ha sido limitada.

## Fuente

- **Instituto Nacional de Salud (INS)**
- [Ver conjunto de datos en datos.gov.co](https://www.datos.gov.co/Salud-y-Protecci-n-Social/Casos-positivos-de-COVID-19-en-Colombia-/gt2j-8ykr/about_data)

---

# ⚙️ Configuración del Entorno PostgreSQL con Docker

## 1. Ejecutar el contenedor de PostgreSQL

Ejecuta el siguiente comando para iniciar el contenedor:

```bash
docker-compose up -d
```

Esto creará una base de datos llamada `covid_db`, accesible en el puerto `35432` con las siguientes credenciales:

- **Usuario**: `covid_user`
- **Contraseña**: `covid_pass`
- **Base de datos**: `covid_db`

---

# 🛠 Configuración de dbt

El archivo `profiles.yml` necesario para la configuración de dbt se encuentra en:

```bash
transformation/dbt_project/profiles.yml
```

### Conexión dbt

- **Host**: `localhost`
- **Puerto**: `35432`
- **Usuario**: `covid_user`
- **Contraseña**: `covid_pass`
- **Base de datos**: `covid_db`
- **Esquema**: `raw_data`

### Comandos para iniciar y ejecutar modelos dbt

```bash
cd transformation/dbt_project

dbt debug                             # Verificar conexión
dbt run                               # Ejecutar modelos
dbt docs generate && dbt docs serve  # Generar y servir documentación
```

---

# 🧠 Notas

- Dedemos asegurarnos que el esquema `raw_data` exista en la base de datos PostgreSQL. Si no existe lo podemos crear manualmente.
- Podemos conectarnos manualmente a la base de datos utilizando herramientas como **DBeaver**, **pgAdmin** o vía línea de comandos con `psql`:

```bash
psql -h localhost -p 35432 -U covid_user -d covid_db
```
