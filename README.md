# Doki Doki Study Club!

Novela visual interactiva para estudiar cualquier materia mediante explicaciones teóricas y evaluaciones generadas en tiempo real por modelos LLM, con interfaz inspirada en DDLC y tutora personalizada.

---

## Descarga directa (Juego completo)

Para ejecutar el juego con todos los recursos multimedia (imágenes, sprites y música completa en alta fidelidad) sin clonar repositorios ni configurar rutas:

* **Enlace de descarga directa:** [Carpeta completa en Google Drive](https://drive.google.com/drive/folders/1wVzSWswDoSXXZhhiDiPahXRp2Vf75-rl?usp=drive_link)

### Inicio rápido en Windows
1. Descarga el contenido desde el enlace de Google Drive.
2. Si descargaste un `.zip`, descomprímelo en cualquier carpeta de tu disco local.
3. Ejecuta el archivo `DESCARGAR PYTHON CON LAS LIBRE...bat` (o `JUGAR.bat`).
4. El script configurará el entorno e iniciará la aplicación automáticamente en tu navegador (`http://127.0.0.1:8000`).

---

## Cómo obtener las API Keys gratuitas

El juego no incluye claves predeterminadas por seguridad. Se configuran directamente en la interfaz web dentro del menú lateral **AJUSTES > IA & Prompts**.

| Proveedor | Modelo sugerido | Nivel gratuito (Free Tier) | Enlace de registro |
| :--- | :--- | :--- | :--- |
| **Google Gemini** | `gemini/gemini-3.6-flash` | **Gratuito permanente:** 15 peticiones por minuto (RPM) y 1,500 peticiones al día (RPD) sin tarjeta bancaria. | [Google AI Studio](https://aistudio.google.com/app/apikey) |
| **DeepSeek** | `deepseek/deepseek-chat` | **Crédito promocional:** Saldo de bienvenida al registrar cuenta nueva (~$5 USD en tokens). | [DeepSeek Platform](https://platform.deepseek.com/) |
| **Groq** | `groq/llama-3.1-70b-versatile` | **Gratuito permanente:** Acceso veloz con límites por minuto sin costo de suscripción. | [Groq Console](https://console.groq.com/keys) |
| **Moonshot (Kimi)** | `moonshot/moonshot-v1-8k` | **Crédito inicial:** Requiere recarga básica para uso extendido en la plataforma oficial. | [Moonshot Platform](https://platform.moonshot.ai/) |

---

## Instalación manual (Desde código fuente)

### Requisitos previos
* Python 3.10 o superior instalado en el sistema.

### 1. Clonar el repositorio
```bash
git clone [https://github.com/TU_USUARIO/TU_REPOSITORIO.git](https://github.com/TU_USUARIO/TU_REPOSITORIO.git)
cd TU_REPOSITORIO
