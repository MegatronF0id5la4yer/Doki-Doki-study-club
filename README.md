# Doki Doki Study Club! (Port Android & Web)

Port interactivo estilo novela visual ambientado en el universo de DDLC, adaptado para Android (vía WebView / Android Studio) y navegadores web, potenciado con inteligencia artificial mediante la API de Google Gemini.

---

## Novedades del Port

* **Soporte Nativo para Android:** Empaquetado como APK utilizando un contenedor WebView optimizado con soporte para llamadas de red locales y permisos de internet.
* **Actualización a Gemini 3.5 Flash:** Conexión directa mediante la API v1beta de Google Generative Language utilizando el modelo de alta velocidad `gemini-3.5-flash`.
* **Soporte para Nuevas Claves de API:** Manejo del encabezado oficial `x-goog-api-key`, compatible con las nuevas claves de Google AI Studio (prefijos `AQ.` y `AIzaSy`).
* **Seguridad de Claves:** El código cliente no almacena llaves hardcodeadas; el usuario ingresa su propia clave desde la interfaz.

---

## Requisitos de Configuración

Para utilizar la función de IA interactiva:

1. Ve a [Google AI Studio](https://aistudio.google.com/).
2. Genera una API Key gratuita en la sección **Get API key**.
3. Ingresa la clave generada directamente en la casilla de configuración dentro del juego.

---

## Estructura del Port Android

* `app/src/main/assets/`: Contiene los archivos estáticos (`index.html`, `ai_services.js`, música y sprites).
* `app/src/main/java/`: Código fuente de `MainActivity.java` configurado para permitir el acceso a red desde archivos locales (`allowUniversalAccessFromFileURLs`).
* `app/src/main/AndroidManifest.xml`: Declaración de permisos de red (`android.permission.INTERNET`).
