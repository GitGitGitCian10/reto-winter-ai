import os
from dotenv import load_dotenv
from anthropic import AsyncAnthropic, AuthenticationError, APIConnectionError, APITimeoutError

load_dotenv()

client = AsyncAnthropic(
    api_key=os.getenv("API_KEY"),
)

async def claude_summarize(text: str):
    try:
        message = await client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=1024,
            messages=[
                {"role": "user", "content": "Resume el siguiente texto en no más de 5 oraciones siguiendo una estructura de introducción, desarrollo y conclusión. Escribe solo el contenido del resumen sin identificar las partes."},
                {"role": "user", "content": f"{text}"}
            ]
        )
    except AuthenticationError:
        raise AuthenticationError("La API key de Claude es inválida")
    except APIConnectionError:
        raise APIConnectionError("Error de conexión con la API de Claude")
    except APITimeoutError:
        raise APITimeoutError("Timeout en la solicitud")
    return message.content[0].text