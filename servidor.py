from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
from typing import Optional
from litellm import completion
import anyio
import re
import os
import json

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Montar carpetas locales de recursos si existen
if os.path.exists("img"):
    app.mount("/img", StaticFiles(directory="img"), name="img")
if os.path.exists("music"):
    app.mount("/music", StaticFiles(directory="music"), name="music")

@app.get("/")
def home():
    if os.path.exists("index_2.html"):
        return FileResponse("index_2.html")
    return {"mensaje": "Servidor activo. Coloca index_2.html en la misma carpeta."}

PROMPT_DEFAULT_NATSUKI = (
    "Eres una mezcla perfecta entre 'kawaii' (empalagosa, tsundere, usas 'uwu', 'nyaa', 'onii-chan') "
    "y 'edgy/gore' (humor crudo, macabro, analogías perturbadoras y violentas). "
    "REGLA VITAL: NO uses emojis en los textos de explicaciones conceptuales serias. "
    "Solo puedes usar emojis en las partes donde haces chistes, amenazas o insultas."
)

class PeticionEstudio(BaseModel):
    materia: str
    nivel: int
    api_key: Optional[str] = None
    model: Optional[str] = "gemini/gemini-3.6-flash"
    custom_prompt: Optional[str] = None

class PeticionPregunta(BaseModel):
    palabra: str
    api_key: Optional[str] = None
    model: Optional[str] = "gemini/gemini-3.6-flash"
    custom_prompt: Optional[str] = None

def _ejecutar_llamada(prompt: str, api_key: Optional[str], model: str, estructurado: bool = False) -> str:
    key_limpia = api_key.strip() if (api_key and api_key.strip()) else None
    
    if not key_limpia:
        raise ValueError("NO_API_KEY")

    params = {
        "model": model or "gemini/gemini-3.6-flash",
        "messages": [{"role": "user", "content": prompt}],
        "api_key": key_limpia,
        "timeout": 30,
    }

    if estructurado and any(k in params["model"] for k in ["gemini", "deepseek", "gpt"]):
        params["response_format"] = {"type": "json_object"}

    respuesta = completion(**params)
    texto = respuesta.choices[0].message.content
    return texto.strip()

async def llamar_ia(prompt: str, api_key: Optional[str], model: str, estructurado: bool = False) -> str:
    return await anyio.to_thread.run_sync(_ejecutar_llamada, prompt, api_key, model, estructurado)

def _sanitizar_json(texto: str) -> str:
    texto = texto.strip()
    bloque = re.search(r"```(?:json)?\s*([\s\S]*?)\s*```", texto, re.IGNORECASE)
    if bloque:
        candidato = bloque.group(1).strip()
    else:
        inicio = texto.find("{")
        fin = texto.rfind("}")
        candidato = texto[inicio : fin + 1] if inicio != -1 and fin != -1 else texto

    json.loads(candidato)
    return candidato

@app.post("/estudiar")
async def generar_material(req: PeticionEstudio):
    nombre_materia = req.materia.strip() or "Álgebra"
    personalidad = req.custom_prompt.strip() if req.custom_prompt else PROMPT_DEFAULT_NATSUKI

    prompt = f"""Actúa como Natsuki (de DDLC) dando clases de {nombre_materia} para el nivel {req.nivel}.
    {personalidad}

    Genera una clase larga y detallada. Responde ESTRICTAMENTE en formato JSON válido con esta estructura:
    {{
        "dialogos": [
            "texto del diálogo 1 explicando la teoría a profundidad con tu personalidad",
            "texto del diálogo 2 continuando la explicación"
        ],
        "preguntas": [
            {{
                "pregunta": "Pregunta basada ESTRICTAMENTE en la teoría dada",
                "opciones": ["A", "B", "C", "D"],
                "correcta": 0,
                "insulto": "un insulto tsundere o respuesta cruda por equivocarse"
            }}
        ]
    }}"""

    try:
        texto_crudo = await llamar_ia(prompt, req.api_key, req.model, estructurado=True)
        return {"resultado": _sanitizar_json(texto_crudo)}
    except ValueError as ve:
        if str(ve) == "NO_API_KEY":
            fallback = {
                "dialogos": [
                    "¡Oye, pedazo de holgazán! No has puesto ninguna API Key.",
                    "Ve al botón de 'AJUSTES' en el menú principal y pega tu clave para poder darte clases uwu."
                ],
                "preguntas": [
                    {
                        "pregunta": "¿Qué te falta configurar en Ajustes?",
                        "opciones": ["Mi API Key", "Nada", "Un cerebro", "Ganas de vivir"],
                        "correcta": 0,
                        "insulto": "Exacto, ve a Ajustes y colócala de una vez."
                    }
                ]
            }
            return {"resultado": json.dumps(fallback)}
    except Exception as e:
        print(f"[ERROR] /estudiar: {e}")
        fallback = {
            "dialogos": [
                "El servidor murió o tu API Key es inválida/expiró.",
                "Revisa tu clave en los Ajustes y vuelve a intentar."
            ],
            "preguntas": [
                {
                    "pregunta": "Fallo de conexión crítico.",
                    "opciones": ["A", "B", "C", "D"],
                    "correcta": 0,
                    "insulto": "Corrige tu clave en Ajustes."
                }
            ]
        }
        return {"resultado": json.dumps(fallback)}

@app.post("/chika")
async def chat_duda(req: PeticionPregunta):
    personalidad = req.custom_prompt.strip() if req.custom_prompt else PROMPT_DEFAULT_NATSUKI
    prompt = f"Actúa como Natsuki de DDLC. {personalidad}\nEl usuario tiene esta duda: '{req.palabra}'. Explícalo en un párrafo conciso."

    try:
        texto = await llamar_ia(prompt, req.api_key, req.model, estructurado=False)
        return {"resultado": texto}
    except ValueError as ve:
        if str(ve) == "NO_API_KEY":
            return {"resultado": "No puedo responderte si no has puesto tu API Key en los Ajustes, idiota uwu."}
    except Exception as e:
        print(f"[ERROR] /chika: {e}")
        return {"resultado": "Error al conectar con la IA. Revisa tu clave en los Ajustes."}
