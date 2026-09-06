# Doki Doki Study Club! (Port Oficial Android & Web)

**Doki Doki Study Club!** es una novela visual interactiva ambientada en el universo de *Doki Doki Literature Club!*, adaptada para dispositivos móviles mediante un port nativo de Android (WebView) y ejecutable también en navegadores web.

El juego integra a **Natsuki** como tutora de estudio personalizada gracias a la API oficial de **Google Gemini**, adaptando explicaciones académicas, preguntas de opción múltiple y dinámicas de estudio con su personalidad distintiva.

---

## Enlace de Descarga (APK y Recursos)

Para instalar el juego directamente en tu teléfono sin necesidad de compilar nada:

* **Descargar APK y Assets:** [Carpeta Oficial en Google Drive](https://drive.google.com/drive/folders/1wVzSWswDoSXXZhhiDiPahXRp2Vf75-rl?usp=drive_link)

Descarga el archivo `.apk`, ábrelo en tu teléfono Android y permite la instalación de fuentes desconocidas si el sistema lo solicita.

---

## Cómo Configurar la IA para Jugar

Para que Natsuki pueda responder tus mensajes y generar las clases, necesitas una API Key gratuita de Google:

1. Entra a [Google AI Studio](https://aistudio.google.com/).
2. Inicia sesión con tu cuenta de Google y pulsa el botón **Get API key**.
3. Haz clic en **Create API key** y copia la clave generada (funciona tanto con las que inician en `AIzaSy` como con el formato nuevo `AQ...`).
4. Abre la aplicación en tu celular o navegador.
5. Pega la clave en el campo **API Key**, escribe la materia o consulta que quieras y presiona **Enviar Mensaje**.

---

## Detalles Técnicos del Port

* **Modelo:** Gemini 3.5 Flash (`gemini-3.5-flash`) mediante el endpoint REST directo `v1beta`.
* **Seguridad de Llaves:** No contiene credenciales hardcodeadas; el usuario administra su propia clave desde la interfaz.
* **Autenticación:** Encabezado oficial `x-goog-api-key` para compatibilidad universal con las nuevas generaciones de llaves de Google.
* **Android Wrapper:** Android Studio (Java) con WebView configurado con permisos de red (`android.permission.INTERNET`) y bypass local de CORS para ejecutar llamadas HTTP/HTTPS desde `file:///android_asset/`.

---

## Créditos

* Personajes, escenarios y arte original creados por **Team Salvato** (*Doki Doki Literature Club!*).
* Proyecto no oficial desarrollado sin fines de lucro con propósitos educativos.
