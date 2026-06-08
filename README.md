# Personal Data Lake RAW

API base para construir la capa **RAW** de un Data Lake personal, diseñada para centralizar información cruda, registrar metadata técnica y preparar los datos para futuros procesos ETL, automatizaciones, dashboards e inteligencia artificial.

Este proyecto nace como una solución personal de ingeniería de datos para organizar información dispersa de finanzas, productividad, conocimiento e infraestructura, usando una arquitectura simple, trazable y desplegable en entornos reales con Docker y Coolify.

---

## Visión del proyecto

La mayoría de la información personal importante termina distribuida en archivos, correos, capturas, hojas de cálculo, notificaciones, documentos y aplicaciones desconectadas.

El objetivo de este proyecto es construir una primera capa de almacenamiento confiable donde los datos puedan guardarse sin transformación inicial, conservando trazabilidad mediante metadata, hash de archivos y almacenamiento estructurado.

La idea principal es:

> Primero capturar y preservar la información cruda; después limpiarla, clasificarla, analizarla y automatizarla.

---

## Problema que resuelve

Actualmente, la información personal puede estar distribuida en múltiples fuentes:

* Archivos Excel de gastos o presupuestos.
* Correos con facturas, compras o notificaciones.
* Documentos personales.
* Capturas de pantalla.
* Exportaciones de aplicaciones.
* Información de proyectos.
* Datos técnicos de infraestructura personal.
* Registros manuales de productividad o finanzas.

Esto dificulta responder preguntas como:

* ¿Dónde está guardada determinada información?
* ¿Qué archivos fueron cargados y cuándo?
* ¿Cuál es la versión original de un archivo?
* ¿Qué datos pueden ser procesados más adelante?
* ¿Cómo preparar esta información para dashboards o modelos de IA?

---

## Objetivo técnico

Crear una API que permita:

* Recibir archivos desde un cliente o servicio externo.
* Calcular el hash del archivo recibido.
* Almacenar el archivo crudo en MinIO, usando un esquema compatible con S3.
* Registrar metadata en PostgreSQL.
* Preparar la base para futuros procesos ETL.
* Desplegar el sistema en Coolify usando Docker.

---

## Valor para portafolio

Este proyecto demuestra conocimientos aplicados en:

* Diseño de arquitectura backend.
* Construcción de APIs con FastAPI.
* Contenerización con Docker.
* Diseño inicial de un Data Lake.
* Separación entre almacenamiento RAW y catálogo de metadata.
* Uso de PostgreSQL como catálogo estructurado.
* Uso de MinIO como almacenamiento compatible con S3.
* Preparación para despliegue real en Coolify.
* Buenas prácticas de configuración mediante variables de entorno.
* Documentación técnica orientada a evolución del producto.

---

## Estado del proyecto

**Estado actual:** MVP inicial / primer entregable técnico.

La primera versión se enfoca en construir la base del proyecto, validar la ejecución de la API y preparar la estructura para integrar PostgreSQL y MinIO en las siguientes fases.

---

## Alcance inicial

El primer entregable incluye:

* API base en FastAPI.
* Endpoint de salud del servicio.
* Estructura inicial del proyecto.
* Configuración mediante variables de entorno.
* Dockerfile inicial.
* Docker Compose inicial.
* Preparación para conexión con PostgreSQL.
* Preparación para conexión con MinIO.
* Documentación inicial para despliegue en Coolify.

---

## Fuera de alcance inicial

Esta primera versión no incluye:

* Dashboard gráfico.
* Procesamiento financiero.
* Lectura automática de correos.
* OCR.
* Inteligencia artificial.
* Alertas automáticas.
* Limpieza avanzada de datos.
* Modelo final de transacciones.
* Cálculo de presupuesto.
* Cálculo de saldo disponible.
* Automatizaciones externas.

Estas funcionalidades hacen parte de fases futuras del sistema.

---

## Arquitectura general

```text
Usuario / Cliente
        ↓
API FastAPI
        ↓
Validación inicial
        ↓
MinIO Data Lake RAW
        ↓
PostgreSQL Catálogo
        ↓
Procesos ETL futuros
        ↓
Dashboards / Automatizaciones / IA
```

---

## Diseño conceptual

El sistema separa dos responsabilidades principales:

### 1. Almacenamiento RAW

MinIO se utiliza para almacenar los archivos originales sin modificarlos. Esta capa conserva la información tal como fue recibida.

### 2. Catálogo de metadata

PostgreSQL se utiliza para guardar información estructurada sobre cada archivo, como nombre, tipo, tamaño, hash, fecha de carga y ubicación en el almacenamiento.

Esta separación permite mantener trazabilidad y preparar los datos para procesos posteriores sin alterar la fuente original.

---

## Stack tecnológico

| Componente         | Tecnología           |
| ------------------ | -------------------- |
| Backend            | FastAPI              |
| Lenguaje           | Python               |
| Base de datos      | PostgreSQL           |
| Almacenamiento RAW | MinIO                |
| Contenedores       | Docker               |
| Despliegue         | Coolify              |
| Documentación API  | Swagger / OpenAPI    |
| Configuración      | Variables de entorno |

---

## Estructura del proyecto

```text
personal-data-lake/
├── app/
│   ├── main.py
│   ├── config.py
│   ├── routes/
│   │   └── health.py
│   ├── services/
│   ├── database/
│   └── storage/
├── docs/
│   └── 01-primer-entregable.md
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .env.example
└── README.md
```

---

## Endpoints disponibles

### Health check

```http
GET /health
```

Permite validar que la API está funcionando correctamente.

Respuesta esperada:

```json
{
  "status": "ok",
  "service": "personal-data-lake-api"
}
```

---

## Variables de entorno

El proyecto usa variables de entorno para evitar dejar configuraciones sensibles directamente en el código.

Ejemplo:

```env
APP_NAME=personal-data-lake-api
APP_ENV=development
APP_PORT=8000

DATABASE_URL=postgresql://user:password@postgres:5432/personal_data_lake

MINIO_ENDPOINT=minio:9000
MINIO_ACCESS_KEY=change_me
MINIO_SECRET_KEY=change_me
MINIO_BUCKET_RAW=raw
```

Antes de ejecutar el proyecto, se debe crear un archivo `.env` basado en `.env.example`.

---

## Ejecución local con Docker

Construir y levantar los servicios:

```bash
docker compose up -d --build
```

Verificar contenedores activos:

```bash
docker compose ps
```

Ver logs de la API:

```bash
docker compose logs -f api
```

La API estará disponible en:

```text
http://localhost:8000
```

La documentación automática de FastAPI estará disponible en:

```text
http://localhost:8000/docs
```

---

## Despliegue en Coolify

El proyecto está pensado para ser desplegado en Coolify usando Docker.

Flujo esperado:

1. Crear el repositorio en GitHub.
2. Conectar el repositorio en Coolify.
3. Configurar las variables de entorno.
4. Definir el puerto expuesto por la API.
5. Desplegar el servicio.
6. Validar el endpoint `/health`.

---

## Criterios de terminado del primer entregable

El primer entregable se considera completo cuando:

* La API inicia correctamente.
* El endpoint `/health` responde.
* El proyecto corre en Docker.
* Existe estructura base para rutas, configuración, servicios, base de datos y almacenamiento.
* El repositorio tiene documentación inicial.
* El proyecto queda listo para agregar PostgreSQL y MinIO en el siguiente paso.

---

## Roadmap técnico

### Fase 1: Base de la API

* Crear estructura inicial del proyecto.
* Configurar FastAPI.
* Agregar endpoint `/health`.
* Preparar Dockerfile.
* Preparar Docker Compose.
* Documentar ejecución local y despliegue inicial.

### Fase 2: Catálogo de metadata

* Conectar PostgreSQL.
* Crear modelo de metadata de archivos.
* Registrar nombre, tipo, tamaño, hash y fecha de carga.
* Crear endpoint para consultar archivos registrados.

### Fase 3: Almacenamiento RAW

* Conectar MinIO.
* Crear bucket RAW.
* Subir archivos a MinIO desde la API.
* Relacionar archivos almacenados con su metadata en PostgreSQL.

### Fase 4: Ingesta de información

* Crear endpoint para carga de archivos.
* Validar tamaño y tipo de archivo.
* Calcular hash de contenido.
* Registrar trazabilidad básica.
* Preparar estructura para múltiples fuentes de datos.

### Fase 5: Procesamiento futuro

* Clasificación automática de archivos.
* Procesos ETL.
* OCR.
* Lectura de fuentes externas.
* Dashboards financieros y productivos.
* Integración con modelos de inteligencia artificial.

---

## Decisiones de diseño

### Uso de una capa RAW

Se conserva la información original sin modificarla para mantener trazabilidad y permitir reprocesamientos futuros.

### Separación entre archivo y metadata

Los archivos se almacenan en MinIO, mientras que PostgreSQL guarda la metadata necesaria para buscarlos, auditarlos y procesarlos.

### Uso de Docker

Docker permite ejecutar el proyecto de forma consistente en local, VPS o Coolify.

### Uso de FastAPI

FastAPI permite construir una API ligera, documentada automáticamente y preparada para crecer de forma modular.

---

## Posibles casos de uso futuros

* Centralización de documentos personales.
* Registro de archivos financieros.
* Ingesta de comprobantes y facturas.
* Procesamiento de extractos.
* Consolidación de información de productividad.
* Base para un segundo cerebro personal.
* Alimentación de dashboards.
* Preparación de datos para modelos de IA.

---

## Aprendizajes buscados

Este proyecto también funciona como práctica aplicada de:

* Arquitectura de datos.
* Backend moderno con Python.
* Diseño de APIs.
* Buenas prácticas de despliegue.
* Separación de responsabilidades.
* Persistencia de archivos y metadata.
* Preparación de sistemas escalables desde una versión mínima.

---

## Licencia

Proyecto personal en desarrollo.

---

## MinIO RAW Object Storage

The project uses MinIO as the RAW object storage layer.

MinIO is used to store original files before any transformation or ETL process.

Storage health check:

```http
GET /health/storage

More details:

docs/minio-storage.md

