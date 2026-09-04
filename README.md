Markdown
# Doki-Doki-study-club

Novela visual interactiva para estudiar cualquier tema mediante teoría estructurada y cuestionarios generados por modelos de lenguaje (LLM). Funciona con un backend en FastAPI que despacha peticiones mediante LiteLLM y un frontend responsivo estilo DDLC con audio dinámico y control de sprites.

---

## Descarga Directa (Juego Completo)

Debido al peso de las pistas en alta fidelidad (.flac/.ogg) y los paquetes de imágenes, los archivos multimedia pesados se encuentran alojados en la nube:

* **Enlace de descarga directa:** [Carpeta completa en Google Drive](https://drive.google.com/drive/folders/1wVzSWswDoSXXZhhiDiPahXRp2Vf75-rl?usp=drive_link)
* **URL:** `https://drive.google.com/drive/folders/1wVzSWswDoSXXZhhiDiPahXRp2Vf75-rl?usp=drive_link`

### Inicio Rápido en Windows
1. Descarga el contenido desde el [enlace de Google Drive](https://drive.google.com/drive/folders/1wVzSWswDoSXXZhhiDiPahXRp2Vf75-rl?usp=drive_link).
2. Si bajaste un archivo `.zip`, descomprímelo en cualquier directorio local.
3. Haz doble clic en el archivo `.bat` instalador/lanzador (`INICIAR.bat` o `DESCARGAR PYTHON CON LAS LIBRE...bat`).
4. El script comprobará si Python está presente en el sistema, instalará las dependencias necesarias mediante `pip` y abrirá la interfaz en tu navegador (`http://127.0.0.1:8000`).

---

## Obtención de API Keys Gratuitas

Por motivos de seguridad, el repositorio no incluye claves preconfiguradas. Puedes ingresar tu clave directamente en la interfaz del juego abriendo el menú lateral **AJUSTES > IA & Prompts**.

| Proveedor | Modelo Recomendado | Nivel Gratuito (Free Tier) | Enlace Oficial |
| :--- | :--- | :--- | :--- |
| **Google Gemini** | `gemini/gemini-3.6-flash` | **Gratuito:** 15 RPM (peticiones por minuto) y 1,500 RPD (peticiones por día) sin ingresar tarjeta. | [Google AI Studio](https://aistudio.google.com/app/apikey) |
| **DeepSeek** | `deepseek/deepseek-chat` | **Crédito inicial:** Saldo promocional de bienvenida para nuevos registros. | [DeepSeek Platform](https://platform.deepseek.com/) |
| **Groq** | `groq/llama-3.1-70b-versatile` | **Gratuito:** Inferencia ultrarrápida con límites por minuto sin costo de suscripción. | [Groq Console](https://console.groq.com/keys) |
| **Moonshot (Kimi)** | `moonshot/moonshot-v1-8k` | **Bono de registro:** Requiere cuenta verificada en su consola de desarrollador. | [Moonshot Platform](https://platform.moonshot.ai/) |

---

## Instalación Manual (Desde Código)

### Requisitos
* Python 3.10 o superior instalado.

### 1. Clonar el repositorio
```bash
git clone [https://github.com/MegatronF0id5la4yer/Doki-Doki-study-club.git](https://github.com/MegatronF0id5la4yer/Doki-Doki-study-club.git)
cd Doki-Doki-study-club
2. Instalar dependencias
Bash
pip install fastapi uvicorn litellm anyio pydantic
3. Descargar carpetas multimedia (Opcional si clonas Git)
El repositorio de Git solo contiene el código. Si no descargaste el juego completo desde el Drive, descarga las carpetas img/ y music/ desde ese mismo enlace y colócalas en la raíz del proyecto.

4. Ejecutar el servidor
Bash
python -m uvicorn servidor:app --reload
Abre tu navegador en http://127.0.0.1:8000.

Estructura del Directorio
Plaintext
Doki-Doki-study-club/
├── index_2.html              # Interfaz gráfica visual novel
├── servidor.py               # Servidor FastAPI + integración LiteLLM
├── INICIAR.bat               # Automatizador de entorno para Windows
├── README.md                 # Documentación técnica
│
├── music/                    # Pistas de audio para cada escena (vía Google Drive)
│   ├── 1-01. Main Theme.flac # Menú Principal
│   ├── map_muzak.ogg         # Fase de lectura / explicación
│   ├── 1-06. Poem Panic!.flac# Fase de examen / cuestionario
│   └── 1-09. My Confession.flac # Pantalla de puntajes
│
└── img/                      # Sprites y fondos (vía Google Drive)
    ├── bg/                   # Fondos del aula y menú principal
    ├── natsuki escuela/      # Sprites con uniforme escolar
    ├── natsuki casual/       # Sprites en ropa de civil
    └── personaje personalizado 1/  (hasta slot 5)
        ├── normal.webp       # Pose neutral
        ├── pensando.webp     # Estado de consulta / dudas
        ├── examen.webp       # Cuestionario activo
        ├── feliz.webp        # Acierto en respuesta
        └── molesta.webp      # Fallo en respuesta
Guía de Resolución de Problemas y Modificación del Código
Si el servidor arroja errores en consola o las llamadas a la IA fallan, sigue estas soluciones:

1. Error 404 de modelo obsoleto o retirado (NotFoundError)
Si en la consola de Python aparece un error indicando que el modelo ya no existe o cambió de versión:

Abre servidor.py y busca la clase:

Python
class PeticionEstudio(BaseModel):
    materia: str
    nivel: int
    api_key: Optional[str] = None
    model: Optional[str] = "gemini/gemini-3.6-flash"  # <-- Cambiar aquí
    custom_prompt: Optional[str] = None
Sustitúyelo por el modelo vigente correspondiente (por ejemplo: gemini/gemini-2.0-flash o deepseek/deepseek-chat).

2. Error 400 por JSON malformado o respuesta vacía
Algunos proveedores no admiten el flag de formato estructurado nativo. Si la respuesta de la IA no se puede procesar:

En servidor.py, busca la función _ejecutar_llamada y comenta estas líneas:

Python
# Si el modelo falla por soporte de json estructurado, comenta estas lineas:
# if estructurado and any(k in params["model"] for k in ["gemini", "deepseek", "gpt"]):
#     params["response_format"] = {"type": "json_object"}
Al comentarlas, el modelo enviará texto estándar y la función _sanitizar_json extraerá el JSON mediante expresiones regulares.

3. Forzar una API Key fija en el servidor
Si prefieres no usar el formulario web de Ajustes y quieres dejar tu clave guardada en el backend:

En servidor.py, modifica _ejecutar_llamada:

Python
def _ejecutar_llamada(prompt: str, api_key: Optional[str], model: str, estructurado: bool = False) -> str:
    # Descomenta y coloca tu clave aqui si deseas ignorar el frontend:
    # key_limpia = "TU_API_KEY_AQUI"
    key_limpia = api_key.strip() if (api_key and api_key.strip()) else None
4. Error de CORS o bloqueo de peticiones fetch
Si levantas el frontend de forma independiente o desde una ruta local distinta a 127.0.0.1:8000:

Python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
Configuración de Avatares Personalizados
Crea una carpeta dentro de img/ llamada exactamente personaje personalizado 1 (hasta el slot 5).

Agrega los 5 archivos en formato .webp con los nombres:

normal.webp

pensando.webp

examen.webp

feliz.webp

molesta.webp

En el juego, accede a AJUSTES > Avatares y haz clic en USAR en el espacio correspondiente.
