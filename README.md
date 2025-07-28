## reto-winter-ai

## Introducción
El proyecto consiste en crear una API de python con un endpoint _/summarize_ que reciba un texto largo y que, integrándolo con la API de Claude, sea capaz de resumirlo brevemente y retornarlo.

## Tecnologías utilizadas
Para el proyecto se utilizaron FastAPI y el SDK de Cliente de Anthropic. 
FastAPI es un framework web que permite la creación de APIs en python mientras que el SDK de Cliente de Anthropic brinda herramientas para la conexión y comunicación con los modelos de IA de Claude para, en nuestro caso, el resumen de los textos.

## Ejecución
<ins>**Nótese que para la ejecución del proyecto se debe contar con una API key de Anthropic configurada**</ins> [(véase API KEY)](#api-key)

Estando en la carpeta principal del proyecto se debe ejecutar el siguiente comando:
> fastapi dev main.py

(se puede verificar su funcionamiento abriendo una página con la url _http://127.0.0.1:8000_)
Una vez hecho esto y teniendo el texto largo a resumir, enviar una solicitud post (a través de, por ejemplo, Postman) a _http://127.0.0.1:8000/summarize_ con un body con el siguiente formato:
> { "text": "El texto que se quiere resumir." }

De funcionar correctamente recibirá una respuesta con el siguiente formato:
> { "resumen": "El resumen resultante dado el texto inicial." }

## API KEY
Para la obtención de la API key de Anthropic se deberá dirigir a _https://console.anthropic.com_ y crearse una cuenta en la plataforma. Una vez hecho, se deberá dirigir a Settings (configuración), API keys y crear su propia API key (nótese que en situaciones convencionales, su cuenta no contará con creditos para utilizar esta API key).

Para la utlización de la API en entorno local se precisará crear un archivo .env agregando dentro la API key de la siguiente manera:
> API_KEY="su API key propia para Claude"
