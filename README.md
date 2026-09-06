# 🌸 Doki Doki Study Club! (Port Android & Web) 🧁✨

[![Doki Doki Study Club tutorial](https://img.youtube.com/vi/jBb_K5g2S1E/hqdefault.jpg)](https://youtube.com/shorts/jBb_K5g2S1E)

¡Bienvenido al club de literatura más caótico y educativo del ciberespacio!  
**Doki Doki Study Club!** es una adaptación interactiva inspirada en el universo de *Doki Doki Literature Club!*, reconstruida para ejecutarse como aplicación nativa en dispositivos modernos con **Android 14 (API 34) o superior**, además de correr directamente en cualquier navegador web.

Elige a tu tutora académica favorita (**Natsuki**, **Yuri**, **Monika**, **Sayori** o slots personalizados), cada una con sus propios estados emocionales dinámicos, respuestas canónicas y cerebro impulsado directamente por el modelo **Gemini 3.5 Flash** de Google.

---

## 🎀 Descarga Directa (APK y Recursos)

Para instalar el juego en tu teléfono sin necesidad de compilar código:

* 📂 **Descargar APK y Assets:** [Google Drive - Doki Doki Study Club](https://drive.google.com/drive/folders/1wVzSWswDoSXXZhhiDiPahXRp2Vf75-rl?usp=drive_link)

1. Descarga el paquete `.apk` desde el enlace de Drive.
2. Ábrelo en tu dispositivo con **Android 14+**.
3. Concede el permiso para instalar aplicaciones desde fuentes desconocidas si tu sistema te lo solicita y ¡a estudiar!

---

## 🔑 Despertar a las Dokis (Configuración de la API)

El juego procesa las respuestas directamente en tu dispositivo sin servidores intermediarios. Para conectar la IA necesitas una clave de acceso gratuita de Google:

1. Ingresa a **Google AI Studio**: [https://aistudio.google.com/](https://aistudio.google.com/)
2. Inicia sesión con tu cuenta de Google y pulsa el botón **Get API key**.
3. Haz clic en **Create API key** y copia la cadena generada (compatible con el formato clásico `AIzaSy...` y el estándar `AQ...`).
4. Abre la aplicación en tu celular o navegador y ve a la pestaña lateral **Ajustes > IA & Prompts**.
5. Pega tu clave en la casilla **API Key Personal**, selecciona o añade una materia y pulsa **Nueva Lección**.

---

## ⚠️ Autopsia de Errores (Troubleshooting)

Si la sesión colapsa, la tutora en turno o la interfaz escupirán un mensaje de fallo. Aquí tienes la traducción a términos de Logcat y consola web:

* **"El API colapsó en un charco de sangre uwu. Revisa tu llave o tu conexión a internet."**  
  *Causa técnica (`Failed to fetch` / `NetworkError`):* El paquete no llegó al servidor. La petición murió localmente porque el dispositivo no tiene conexión a red, o Android bloqueó el tráfico por faltar el permiso de red en el manifiesto.

* **"Fallo de conexión crítico. Idiota." / "Mi cerebro de silicio está frito uwu."**  
  *Causa técnica (Error HTTP 400 / 403):* La API Key es inválida, le faltan caracteres o el cuerpo JSON de la petición fue rechazado por las políticas de Google AI Studio.

* **"El servidor murió o las API Keys colapsaron uwu."**  
  *Causa técnica (Error HTTP 404 / 503):* El endpoint no encontró el modelo especificado (comprueba que apunte a `gemini-3.5-flash`), o los servidores de Google se encuentran temporalmente saturados.

* **ERR_CLEARTEXT_NOT_PERMITTED (Solo en Android Studio)**  
  El sistema operativo bloqueó la conexión por intentar comunicarse mediante HTTP inseguro. Toda petición debe ir cifrada mediante HTTPS.

---

## 🛠️ Para Desarrolladores y Modders (Compilación Local)

Si deseas modificar los prompts, integrar nuevos trajes, añadir pistas de audio o generar un APK firmado propio:

### 1. Clonar el repositorio
```bash
git clone [https://github.com/MegatronF0id5la4yer/Doki-Doki-study-club.git](https://github.com/MegatronF0id5la4yer/Doki-Doki-study-club.git)
```

### 2. Abrir en Android Studio
1. Abre Android Studio y selecciona **Open**.
2. Elige la carpeta del proyecto para que Gradle sincronice dependencias.
3. Comprueba que la carpeta `assets` contenga todo el frontend (`index.html`, `ai_services.js`, `img/`, `music/`) dentro de:
   ```text
   app/src/main/assets/
   ```

### 3. Compilar el APK
* **Prueba rápida:** Conecta tu dispositivo por depuración USB y presiona **Run 'app'** (`Shift + F10`).
* **Generar binario final:** Ve al menú **Build > Build Bundle(s) / APK(s) > Build APK(s)**.

---

## 📦 Radiografía de los Componentes Clave

```text
DokiDokiStudyClub/
│
├── app/
│   ├── src/main/
│   │   ├── AndroidManifest.xml        # Permisos de red (INTERNET)
│   │   ├── java/.../MainActivity.java  # Contenedor WebView con acceso a assets locales
│   │   ├── res/                       # Iconos de la app y recursos nativos
│   │   └── assets/                    # Núcleo del frontend
│   │       ├── index.html             # Interfaz visual, selector táctico y máquina de estados
│   │       ├── ai_services.js         # Cliente REST modular para Gemini 3.5 Flash
│   │       ├── img/                   # Fondos y carpetas de sprites estructuradas
│   │       │   ├── bg/
│   │       │   ├── natsuki escuela/
│   │       │   ├── natsuki casual/
│   │       │   ├── yuri escuela/
│   │       │   ├── yuri casual/
│   │       │   ├── monika escuela/
│   │       │   ├── sayori escuela/
│   │       │   ├── sayori casual/
│   │       │   └── personaje personalizado 1..5/
│   │       └── music/                 # BGM ambiental y pistas del club
│   └── build.gradle                   # Target para Android 14 (API 34+)
│
└── README.md
```

### Funcionamiento Interno

* **`ai_services.js` (Motor de IA Modular):**  
  Implementa la función asíncrona `enviarMensaje(modelo, apiKey, promptUsuario, promptSistema)`. Prepara el payload `contents`, autentica mediante el encabezado `x-goog-api-key` y entrega el contenido limpio listo para parsear en JSON.
* **`index.html` (Lógica y Máquina de Estados):**  
  Maneja la selección rectangular de tutoras, el cambio dinámico de atuendos escolares/casuales, el mapeo de los 5 estados de ánimo (`normal`, `pensando`, `examen`, `feliz`, `molesta`), la inyección automática del *System Prompt* según el personaje activo y la gestión de niveles por materia.
* **`MainActivity.java` (Puente WebView):**  
  Configura el navegador embebido habilitando JavaScript (`setJavaScriptEnabled(true)`) y otorgando acceso cruzado a los recursos empaquetados (`setAllowFileAccessFromFileURLs(true)` y `setAllowUniversalAccessFromFileURLs(true)`), permitiendo peticiones HTTPS hacia Google AI desde `file:///android_asset/`.
* **`AndroidManifest.xml` (Permisos):**  
  Declara `<uses-permission android:name="android.permission.INTERNET" />` para que el sistema operativo permita la salida de tráfico hacia las APIs de Google.

---

## ⚙️ Ficha Técnica

* **Modelo de IA:** Gemini 3.5 Flash (`gemini-3.5-flash`) mediante conexión directa REST.
* **Formato Gráfico:** WebP (`.webp`) estructurado en 5 emociones por variante de ropa.
* **Compatibilidad:** Android 14.0 (API 34) o superior; navegadores web modernos basados en Chromium o Firefox.
* **Autenticación:** Encabezado HTTP `x-goog-api-key` universal.
* **Seguridad:** Repositorio y binarios limpios de claves; cada usuario gestiona su propia API Key en almacenamiento local (`localStorage`).

---

## 📄 Créditos y Descargo de Responsabilidad

* Personajes, fondos, música y conceptos pertenecen originalmente a **Team Salvato** (*Doki Doki Literature Club!*).
* Este es un proyecto tributo de código abierto, desarrollado sin fines de lucro con propósitos educativos y de entretenimiento. No existe afiliación oficial con Team Salvato ni con Google.
