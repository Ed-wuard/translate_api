# API de Detección de Idioma y Traducción

Esta es una API simple construida con Flask que proporciona dos endpoints: uno para detectar el idioma de un texto y otro para traducir texto a un idioma específico.

## Requisitos

- Python 3.x
- Flask
- langid
- googletrans

## Instalación

1. Clona el repositorio:

   ```bash
   git clone https://github.com/Ed-wuard/translate_api.git
2. Clona el repositorio:

    ```python
    python -m venv .venv
    .venv\Scripts\activate  # En Windows
    source .venv/bin/activate  # En macOS/Linux

3. Instala las dependencias:

    ```python
    pip install -r requirements.txt

## Uso

Ejecutar la API
Para ejecutar la API, simplemente ejecuta el siguiente comando:

    python app.py

La API estará disponible en http://127.0.0.1:5000/.

## Endpoints
- **POST** /detect_language: *Detectar idioma.*
- **POST** /translate: *Traducir texto.*

## Detectar idioma

**Cuerpo:**

     {
         "text": "aqui el texto"
     }


**Respuesta:**

     {
         "confidence": 1.7387170791625977,
         "language": "es"
     }


## Traducir

**Cuerpo:**

     {
         "text": "aqui el texto",
         "target_language": "en"
     }


**Respuesta:**

        {
            "translated_text": "texto traducido"
        }

## Contribuir
Si deseas contribuir a este proyecto, por favor abre un issue o envía un pull request.

## Licencia
Este proyecto está bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.
